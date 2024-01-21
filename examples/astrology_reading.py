from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


class AstrologyReader:
    def __init__(self):
        # TODO: The 'openai.api_key_path' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_key_path=".openai-api-key")'
        # openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def get_astrology_reading(self, zodiac_sign):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Provide an astrology reading for: "},
                {"role": "user", "content": zodiac_sign},
            ],
        )
        return response.choices[0].message.content


def main():
    reader = AstrologyReader()
    reading = reader.get_astrology_reading("Leo")
    print(reading)


if __name__ == "__main__":
    main()
