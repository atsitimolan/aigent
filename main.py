import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("Gemini API Key cannot be found.")

client = genai.Client(api_key=api_key)
model = "gemini-2.5-flash"
user_prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

print(f"User prompt: {user_prompt}")

response = client.models.generate_content(
    model=model, contents=user_prompt
)

if (response.usage_metadata == None):
    raise RuntimeError("No usage metadata.")
else:
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
print(f"Response: \n{response.text}")

def main():
    print("Hello from aigent!")


if __name__ == "__main__":
    main()
