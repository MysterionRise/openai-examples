import tiktoken


def num_tokens_from_string(string: str, encoding_name: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def encode_for_model(string: str, model: str) -> list:
    enc = tiktoken.encoding_for_model(model)
    return enc.encode(string)


def main():
    print(encode_for_model("hello world!", "gpt-4"))
    print(num_tokens_from_string("hello world!", "cl100k_base"))
    print(num_tokens_from_string("привiт свiт!", "cl100k_base"))


if __name__ == "__main__":
    main()
