import os
from datetime import datetime
import pandas as pd


def save_results(df: pd.DataFrame, folder: str = "output") -> str:
    """Save pipeline output with a timestamped filename."""
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filepath = f"{folder}/results_{timestamp}.csv"
    df.to_csv(filepath, index=False)
    print(f"Saved results to {filepath}")
    return filepath


def save_log(message: str, folder: str = "logs") -> None:
    """Append a log line to a simple pipeline log file."""
    os.makedirs(folder, exist_ok=True)
    with open(f"{folder}/pipeline.log", "a") as f:
        f.write(message + "\n")


