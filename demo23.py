import lib.nlp.to_words
import lib.sample
import lib

w = lib.nlp.to_words.to_words(
    "напишіть програму, яка малює будиночок, користуючись розділами по черепашу графіку"
)
print(w)

v = lib.sample.to_words(
    "напишіть програму, яка малює будиночок, користуючись розділами по черепашу графіку"
)
print(v)

u = lib.to_string(v)
print(u)
