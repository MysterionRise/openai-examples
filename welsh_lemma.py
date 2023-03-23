from main import do_action_as_chatgpt

if __name__ == '__main__':
    print(
        do_action_as_chatgpt(
            "You are Welsh language expert",
            "Lemmatise words provided, that are separated by semicolon",
            "Rhedeg; redegog; rhedegog; edryd"
    ))
