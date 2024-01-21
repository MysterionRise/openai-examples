from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


class NewsSummarizer:
    def __init__(self):
        # TODO: The 'openai.api_key_path' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_key_path=".openai-api-key")'
        # openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def summarize_news(self, topic):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Provide a summary of the latest news about: "},
                {"role": "user", "content": topic},
            ],
        )
        return response.choices[0].message.content


def main():
    summarizer = NewsSummarizer()
    summary = summarizer.summarize_news("OpenAI")
    print(summary)


if __name__ == "__main__":
    main()
