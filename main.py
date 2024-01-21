import random

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def main():
    print(get_available_models())
    # print(
    #     do_action_as_chatgpt(
    #         "You're chatbot that answers questions from citizens about "
    #         "Ukraine constitution and other laws and regulations in "
    #         "Ukrainian language. Don’t use surgyk please!",
    #         "Response must have links related to parts of the documents"
    #         "Чи потрібно мені прописуватись при проживанні в дачному селищі?",
    #     )
    # )


def get_available_models():
    return client.models.list()


def generate_tweet(prompt: str = None):
    return client.completions.create(
        model="text-davinci-003", prompt=prompt, max_tokens=30, temperature=random.randint(0, 5)
    )


def do_action_as_chatgpt(
    assistant_role1: str = None,
    assistant_role2: str = None,
    prompt: str = None,
):
    temperature = random.random()
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "" if assistant_role1 is None else assistant_role1,
            },
            {
                "role": "system",
                "content": "" if assistant_role2 is None else assistant_role2,
            },
            {"role": "user", "content": "" if prompt is None else prompt},
        ],
        frequency_penalty=2,
        temperature=temperature,
    )
    print(f"temperature - {temperature}")
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


if __name__ == "__main__":
    main()
