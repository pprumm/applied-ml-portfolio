import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

def validate_baseline_with_regression(df):
    """
    Train PCA + linear regression on baseline reference samples (`cablecal_baseline`)
    using [temp, pressure, humid]. A train/test split on the baseline segment
    reports RMSE as a sanity check. The trained model is then used to predict
    baseline values for rows where `cablecal_baseline` is missing, providing an
    environment-driven estimate that can be compared with the MAD-cleaned reconstruction
    (`cablecal_clean`).
    
    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe containing columns:
        ['time', 'cablecal', 'temp', 'pressure', 'humid',
         'cablecal_baseline', 'cablecal_clean'].

    Returns
    -------
    df : pandas.DataFrame
        Dataframe with 1 additional column:
        'cablecal_baseline_ml_pred'.
    """
    features = ['temp', 'pressure', 'humid']
    
    df = df.copy()

    # split data
    train_df = df[df["cablecal_baseline"].notnull()]
    predict_df = df[df["cablecal_baseline"].isnull()]
    
    X = train_df[features]
    y = train_df["cablecal_baseline"]
    
    # train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # PCA
    pca = PCA(n_components=3)
    X_train = pca.fit_transform(X_train)
    X_test = pca.transform(X_test)
    
    # regression
    model = LinearRegression()
    model.fit(X_train, y_train)

    # evaluation
    train_rmse = root_mean_squared_error(y_train, model.predict(X_train))
    test_rmse = root_mean_squared_error(y_test, model.predict(X_test))

    print(f"Train RMSE: {train_rmse:.2f} cm | Test RMSE: {test_rmse:.2f} cm")

    # predict missing baseline
    X_pred = scaler.transform(predict_df[features])
    X_pred = pca.transform(X_pred)

    df.loc[predict_df.index, "cablecal_baseline_ml_pred"] = model.predict(X_pred)

    return df