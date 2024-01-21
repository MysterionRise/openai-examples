from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


class TravelAdvisor:
    def __init__(self):
        self.model = "gpt-4"

    def get_travel_advice(self, destination):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Provide travel advice for: "},
                {"role": "user", "content": destination},
            ],
        )
        return response.choices[0].message.content


def main():
    advisor = TravelAdvisor()
    advice = advisor.get_travel_advice("Japan")
    print(advice)


if __name__ == "__main__":
    main()
