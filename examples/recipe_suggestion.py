import openai


class RecipeSuggester:
    def __init__(self):
        openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def suggest_recipe(self, ingredients):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Suggest a recipe using these ingredients: ",
                },
                {"role": "user", "content": ingredients},
            ],
        )
        return response["choices"][0]["message"]["content"]


def main():
    suggester = RecipeSuggester()
    recipe = suggester.suggest_recipe("chicken, rice, tomatoes")
    print(recipe)


if __name__ == "__main__":
    main()
