import lib.nlp.to_words as qwert
from lib.sample import to_words
import lib

w = qwert.to_words(
    "напишіть програму, яка малює будиночок, користуючись розділами по черепашу графіку"
)
print((w,))

v = to_words(
    "напишіть програму, яка малює будиночок, користуючись розділами по черепашу графіку"
)
print((v,))

u = lib.to_string(v)
print((u,))
