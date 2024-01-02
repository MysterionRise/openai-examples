import openai


class TextTranslator:
    def __init__(self, source_lang, target_lang, text):
        openai.api_key_path = ".openai-api-key"
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.text = text

    def translate(self):
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": f"Translate from {self.source_lang} to {self.target_lang}.",
                },
                {"role": "user", "content": self.text},
            ],
        )
        return completion.choices[0].message["content"]


def test_text_translation():
    translator = TextTranslator("English", "Spanish", "Hello, how are you?")
    print(translator.translate())


if __name__ == "__main__":
    test_text_translation()
