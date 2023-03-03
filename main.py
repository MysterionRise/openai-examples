import random

import openai


def main():
    print(do_action_as_chatgpt())


def get_available_models():
    openai.api_key_path = ".openai-api-key"
    return openai.Model.list()


def generate_tweet(prompt: str = None):
    openai.api_key_path = ".openai-api-key"
    return openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=30,
        temperature=random.randint(0, 5)
    )


def do_action_as_chatgpt(assistant_role: str = None, prompt: str = None):
    openai.api_key_path = ".openai-api-key"
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": "" if assistant_role is None else assistant_role},
            {"role": "user",
             "content": "" if prompt is None else prompt}
        ]
    )

    return completion.choices[0].message


if __name__ == '__main__':
    main()
