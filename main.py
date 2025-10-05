import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]
    if not args:
        print("Missing argument")
        sys.exit(1)

    prompt = args[0]

    messages = [types.Content(role="user", parts=[types.Part(text=prompt)]),]

    response = client.models.generate_content(model='gemini-2.0-flash-001', contents=messages)

    if args[-1] == "--verbose":
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print(response.text)


if __name__ == "__main__":
    main()