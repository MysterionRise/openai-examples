import openai


class FitnessAdvisor:
    def __init__(self):
        openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def provide_fitness_tips(self, goal):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "system", "content": "Provide fitness tips for: "}, {"role": "user", "content": goal}],
        )
        return response["choices"][0]["message"]["content"]


def main():
    advisor = FitnessAdvisor()
    tips = advisor.provide_fitness_tips("weight loss")
    print(tips)


if __name__ == "__main__":
    main()
