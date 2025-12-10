import re
import pandas as pd


def clean_text(text: str) -> str:
    """Basic cleanup for model-ready text."""
    if not isinstance(text, str):
        return ""
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


def create_prompt(cleaned_text: str) -> str:
    """Prepare the prompt template sent to the model."""
    return f"Please summarize the following text in one sentence:\n\n{cleaned_text}"


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    """Apply text cleaning and prompt creation to the dataset."""
    df["cleaned_text"] = df["text"].apply(clean_text)
    df["prompt"] = df["cleaned_text"].apply(create_prompt)
    return df


if __name__ == "__main__":
    df = pd.read_csv("data/input.csv")
    df = prepare_data(df)
    print(df[["text", "cleaned_text", "prompt"]].head())


