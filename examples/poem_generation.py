from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


class PoemGenerator:
    def __init__(self):
        # TODO: The 'openai.api_key_path' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_key_path=".openai-api-key")'
        # openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def generate_poem(self, theme):
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": "Generate a poem about: "}, {"role": "user", "content": theme}],
        )
        return response.choices[0].message.content


def main():
    generator = PoemGenerator()
    poem = generator.generate_poem("nature")
    print(poem)


if __name__ == "__main__":
    main()
