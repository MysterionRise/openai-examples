from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


class FitnessAdvisor:
    def __init__(self):
        # TODO: The 'openai.api_key_path' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_key_path=".openai-api-key")'
        # openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def provide_fitness_tips(self, goal):
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "system", "content": "Provide fitness tips for: "}, {"role": "user", "content": goal}],
        )
        return response.choices[0].message.content


def main():
    advisor = FitnessAdvisor()
    tips = advisor.provide_fitness_tips("weight loss")
    print(tips)


if __name__ == "__main__":
    main()
