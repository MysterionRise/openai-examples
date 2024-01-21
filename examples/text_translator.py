from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


class TextTranslator:
    def __init__(self, source_lang, target_lang, text):
        # TODO: The 'openai.api_key_path' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_key_path=".openai-api-key")'
        # openai.api_key_path = ".openai-api-key"
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.text = text

    def translate(self):
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": f"Translate from {self.source_lang} to {self.target_lang}.",
                },
                {"role": "user", "content": self.text},
            ],
        )
        return completion.choices[0].message.content


def test_text_translation():
    translator = TextTranslator("English", "Spanish", "Hello, how are you?")
    print(translator.translate())


if __name__ == "__main__":
    test_text_translation()
