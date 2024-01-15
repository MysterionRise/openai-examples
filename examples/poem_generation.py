import openai


class PoemGenerator:
    def __init__(self):
        openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def generate_poem(self, theme):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "system", "content": "Generate a poem about: "}, {"role": "user", "content": theme}],
        )
        return response["choices"][0]["message"]["content"]


def main():
    generator = PoemGenerator()
    poem = generator.generate_poem("nature")
    print(poem)


if __name__ == "__main__":
    main()
