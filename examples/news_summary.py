import openai


class NewsSummarizer:
    def __init__(self):
        openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def summarize_news(self, topic):
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Provide a summary of the latest news about: "},
                {"role": "user", "content": topic},
            ],
        )
        return response["choices"][0]["message"]["content"]


def main():
    summarizer = NewsSummarizer()
    summary = summarizer.summarize_news("OpenAI")
    print(summary)


if __name__ == "__main__":
    main()
