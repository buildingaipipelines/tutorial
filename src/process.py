import pandas as pd

from ingest import load_data
from transform import prepare_data
from generate import run_model
from evaluate import basic_checks
from save import save_results


def evaluate_outputs(df: pd.DataFrame) -> pd.DataFrame:
    """Apply basic quality checks to each model output."""
    df["is_valid"] = df["summary"].apply(basic_checks)
    return df


def run_pipeline() -> pd.DataFrame:
    """End-to-end pipeline: load, transform, generate, evaluate, save."""
    df = load_data("data/input.csv")
    df = prepare_data(df)
    df = run_model(df)
    df = evaluate_outputs(df)
    save_results(df)
    return df


if __name__ == "__main__":
    run_pipeline()


