from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


class ImageDescriber:
    def __init__(self):
        # TODO: The 'openai.api_key_path' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(api_key_path=".openai-api-key")'
        # openai.api_key_path = ".openai-api-key"
        self.model = "gpt-4"

    def describe_image(self, image_url):
        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": "Describe the following image: ",
                },
                {"role": "user", "content": image_url},
            ],
        )
        return response.choices[0].message.content


def main():
    describer = ImageDescriber()
    description = describer.describe_image(
        "https://image.jimcdn.com/app/cms/image/transf/none/path"
        "/sa6549607c78f5c11/image/i6de10a2b70b8d17e/version/1586528731/best"
        "-nature-wonders-in-france-plateau-de-valensole-copyright-francois"
        "-roux-european-best-destinations.jpg"
    )
    print(description)


if __name__ == "__main__":
    main()
