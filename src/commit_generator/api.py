import openai


class OpenAIClient:
    def __init_subclass__(self, api_key: str):
        openai.api_key = api_key

    def generate_commit_message(self, prompt: str, max_tokens=100, temperature=0.7) -> str:
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].text.strip()
