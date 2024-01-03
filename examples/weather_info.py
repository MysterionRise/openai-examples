import openai


# NOT_WORKING #
class WeatherInfo:
    def __init__(self):
        openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def get_weather(self, location):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Provide the current weather information for: ",
                },
                {"role": "user", "content": location},
            ],
        )
        return response["choices"][0]["message"]["content"]


def main():
    weather = WeatherInfo()
    current_weather = weather.get_weather("London")
    print(current_weather)


if __name__ == "__main__":
    main()
