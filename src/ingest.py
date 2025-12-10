import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load a CSV and return a DataFrame."""
    df = pd.read_csv(path)
    return df


def validate_input(df: pd.DataFrame) -> None:
    """Optional: light input validation to fail fast on bad schemas."""
    if "text" not in df.columns:
        raise ValueError("Input must contain a 'text' column.")


if __name__ == "__main__":
    df = load_data("data/input.csv")
    print(df.head())


