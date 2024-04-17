import logging


def get_text(text: str) -> list:
    logging.debug(f'{text is not None} text is {text}')
    return text.split()


def get_lower(text: list):
    return ''.join(text).lower()


logging.basicConfig(filename='test.log', level=logging.DEBUG, filemode="a")

print(get_lower(get_text("text 1 2 3")))
