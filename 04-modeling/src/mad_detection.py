import numpy as np
import pandas as pd

def _mad_mask(x, k=3.0, scale=1.4826):
    x = np.asarray(x, float)
    med = np.nanmedian(x)
    mad = np.nanmedian(np.abs(x - med))
    if not np.isfinite(mad) or mad == 0:
        return np.zeros_like(x, dtype=bool)
    return np.abs(x - med) > (k * scale * mad)
    
def _nan_corr(a, b):
    a = np.asarray(a, float) 
    b = np.asarray(b, float)
    m = np.isfinite(a) & np.isfinite(b)
    if m.sum() < 3:
        return 0.0
    aa, bb = a[m], b[m]
    if np.nanstd(aa) == 0 or np.nanstd(bb) == 0:
        return 0.0
    return float(np.corrcoef(aa, bb)[0, 1])

def _interp_nan(y):
    y = np.asarray(y, dtype=float)
    idx = np.arange(y.size)
    good = np.isfinite(y)
    if good.sum() == 0:
        return y
    if good.sum() == 1:
        y2 = y.copy()
        y2[~good] = y[good][0]
        return y2
    y2 = y.copy()
    y2[~good] = np.interp(idx[~good], idx[good], y[good])
    return y2

def reconstruct_cablecal(df, abrupt_cm=1.0, mad_k=3.0):
    """
    Reconstruct cable calibration time series by correcting discontinuities
    using MAD-based detection. Two candidate reconstructions (A,B) are evaluated,
    and the one that shows stronger correlation with environmental variables
    (temperature, pressure, humidity) is selected.
    
    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe containing columns:
        ['time', 'cablecal', 'temp', 'pressure', 'humid'].
    abrupt_cm : float
        Threshold for abrupt jump detection [cm].
    mad_k : float
        MAD scaling factor for outlier detection.

    Returns
    -------
    df : pandas.DataFrame
        Dataframe with two additional columns:
        'cablecal_baseline' and 'cablecal_clean'.
    """
    df = df.copy()
    df["time"] = pd.to_datetime(df["time"],format="%d-%m-%y %H:%M:%S")
    cablecal = df["cablecal"].values.astype(float)
    temp = df["temp"].values.astype(float)
    pressure = df["pressure"].values.astype(float)
    humid = df["humid"].values.astype(float)

    # 1) candidate discontinuity samples
    mask = _mad_mask(cablecal, k=mad_k)
    for i in range(1, len(mask) - 1):
        if np.isfinite(cablecal[i-1]) and np.isfinite(cablecal[i]) and np.isfinite(cablecal[i+1]):
            if (abs(cablecal[i-1] - cablecal[i]) > abrupt_cm) and (abs(cablecal[i+1] - cablecal[i]) > abrupt_cm):
                mask[i] = True
    
    # 2) split baseline vs step-affected samples
    base = np.full_like(cablecal, np.nan)
    step = np.full_like(cablecal, np.nan)
    base[~mask] = cablecal[~mask]
    step[mask]  = cablecal[mask]
    
    # 3) cleanup step segment again
    step[_mad_mask(step, k=mad_k)] = np.nan

    idx_step = np.where(np.isfinite(step))[0]
    if idx_step.size == 0:
        return _interp_nan(base), base
    
    i_step = idx_step[0]
    if i_step == 0:
        filled = np.where(np.isfinite(base), base, cablecal)
        return _interp_nan(filled), base
    
    idx_ref = np.where(np.isfinite(base[:i_step]))[0] 
    if idx_ref.size == 0:
        filled = np.where(np.isfinite(base), base, cablecal)
        return _interp_nan(filled), base

    i_ref = idx_ref[-1]

    # 4) two reconstructions
    shift_a = step[i_step] - base[i_ref]
    shift_b = -step[i_step] - base[i_ref]

    rec_a = _interp_nan(np.fmax(step - shift_a, base))
    rec_b = _interp_nan(np.fmax(-step - shift_b, base))

    env_corr_a  = abs(_nan_corr(rec_a, temp)) + abs(_nan_corr(rec_a, pressure)) + abs(_nan_corr(rec_a, humid))
    env_corr_b  = abs(_nan_corr(rec_b, temp)) + abs(_nan_corr(rec_b, pressure)) + abs(_nan_corr(rec_b, humid))

    cablecal_reconstructed = rec_a if env_corr_a  >= env_corr_b  else rec_b
    
    df["cablecal_baseline"] = base
    df["cablecal_clean"] = cablecal_reconstructed
    
    return df