import openai


class AstrologyReader:
    def __init__(self):
        openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def get_astrology_reading(self, zodiac_sign):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Provide an astrology reading for: "},
                {"role": "user", "content": zodiac_sign},
            ],
        )
        return response["choices"][0]["message"]["content"]


def main():
    reader = AstrologyReader()
    reading = reader.get_astrology_reading("Leo")
    print(reading)


if __name__ == "__main__":
    main()
