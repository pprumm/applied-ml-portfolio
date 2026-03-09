from pathlib import Path
import pandas as pd
from sklearn.metrics import root_mean_squared_error
from src.mad_detection import reconstruct_cablecal
from src.pca_regression import validate_baseline_with_regression

def main():

    raw_path = Path("data/raw")
    processed_path = Path("data/processed")
    processed_path.mkdir(exist_ok=True)

    files = sorted(raw_path.glob("*.csv"))

    for file in files:

        # extract station + date from filename
        name = file.stem
        station, date = name.rsplit("_", 1)
        station = station.replace("_", "-")

        print(f"\nProcessing: {station.upper()} | {date}")

        # load data
        df = pd.read_csv(file)

        # 1 MAD signal cleaning
        df = reconstruct_cablecal(df)

        print("Calibration signal cleaning success.")
        print("")

        # 2 ML baseline validation (prints RMSE inside function)
        print("Baseline regression validation")
        print("------------------------------")
        df = validate_baseline_with_regression(df)
        print("")

        # 3 Reconstruction consistency check (Compare ML baseline prediction with cleaned signal)
        print("Reconstruction consistency check")
        print("--------------------------------")
        
        df_pred_segment = df[df["cablecal_baseline_ml_pred"].notna()]
        
        rmse = root_mean_squared_error(
            df_pred_segment["cablecal_clean"],
            df_pred_segment["cablecal_baseline_ml_pred"]
        )
        
        r = df_pred_segment["cablecal_clean"].corr(
            df_pred_segment["cablecal_baseline_ml_pred"]
        )
        
        print(f"RMSE: {rmse:.2f} cm | r: {r:.2f}")
        print()

        # 4 save processed output
        output_file = processed_path / f"{name}_processed.csv"
        df.to_csv(output_file, index=False)

        print(f"Saved -> {output_file}")
        print("")

if __name__ == "__main__":
    main()