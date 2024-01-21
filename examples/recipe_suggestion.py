from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


class RecipeSuggester:
    def __init__(self):
        # TODO: The 'openai.api_key_path' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_key_path=".openai-api-key")'
        # openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def suggest_recipe(self, ingredients):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Suggest a recipe using these ingredients: ",
                },
                {"role": "user", "content": ingredients},
            ],
        )
        return response.choices[0].message.content


def main():
    suggester = RecipeSuggester()
    recipe = suggester.suggest_recipe("chicken, rice, tomatoes")
    print(recipe)


if __name__ == "__main__":
    main()
