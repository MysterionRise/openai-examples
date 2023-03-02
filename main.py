import os
import openai


def main():
    print(get_available_models)


def get_available_models():
    openai.api_key_path = ".openai-api-key"
    return openai.Model.list()


if __name__ == '__main__':
    main()
