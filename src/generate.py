from openai import OpenAI
from dotenv import load_dotenv
import os
import time
import pandas as pd


load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_summary(prompt: str) -> str:
    """Send a prompt to the model and return the summary text."""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a concise assistant."},
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message["content"]
    except Exception as e:
        # In production, use structured logging instead of print.
        print(f"Error: {e}")
        return ""


def run_model(df: pd.DataFrame) -> pd.DataFrame:
    """Run the model over each prompt in the DataFrame."""
    outputs = []
    for _, row in df.iterrows():
        output = generate_summary(row["prompt"])
        outputs.append(output)
        # Light rate-limiting for safety
        time.sleep(0.2)
    df["summary"] = outputs
    return df


