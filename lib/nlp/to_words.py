import re  # regular expressions


def to_words(long_text):
    return re.split("""[- ,!()"]""", str(long_text))
