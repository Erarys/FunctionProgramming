def get_text(text: str) -> list:
    return text.split()


def get_lower(text: list):
    return ''.join(text).lower()


print(get_lower(get_text("text 1 2 3")))