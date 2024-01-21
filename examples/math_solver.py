from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


class MathSolver:
    def __init__(self):
        # TODO: The 'openai.api_key_path' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_key_path=".openai-api-key")'
        # openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def solve_math_problem(self, problem):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Solve the following math problem: ",
                },
                {"role": "user", "content": problem},
            ],
        )
        return response.choices[0].message.content


def main():
    solver = MathSolver()
    solution = solver.solve_math_problem("2*x^2 + 5 = 10")
    print(solution)


if __name__ == "__main__":
    main()
