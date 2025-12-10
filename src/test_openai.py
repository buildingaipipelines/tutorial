from openai import OpenAI
from dotenv import load_dotenv
import os


def main() -> None:
    """Quick sanity check that OpenAI access works."""
    load_dotenv()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Say hello in one sentence."}],
    )

    # The tutorial uses the responses-style access; this matches that intent.
    print(response.choices[0].message["content"])


if __name__ == "__main__":
    main()


