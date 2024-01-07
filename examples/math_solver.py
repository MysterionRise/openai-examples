import openai


class MathSolver:
    def __init__(self):
        openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def solve_math_problem(self, problem):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Solve the following math problem: ",
                },
                {"role": "user", "content": problem},
            ],
        )
        return response["choices"][0]["message"]["content"]


def main():
    solver = MathSolver()
    solution = solver.solve_math_problem("2*x^2 + 5 = 10")
    print(solution)


if __name__ == "__main__":
    main()
