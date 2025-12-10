from openai import OpenAI
from dotenv import load_dotenv
import os


def basic_checks(text: str) -> bool:
    """Simple rule-based quality checks."""
    if not text:
        return False
    if len(text.split()) < 3:
        return False
    if len(text) > 500:
        return False
    return True


# Optional AI-assisted validation
load_dotenv()
_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ai_validate(summary: str) -> bool:
    """Use the model to validate that the text is a clear one-sentence summary."""
    prompt = f"Is the following text a clear one-sentence summary? Answer only yes or no:\n\n{summary}"

    try:
        response = _client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        answer = response.choices[0].message["content"].strip().lower()
        return "yes" in answer
    except Exception:
        return False


