"""Learning to Speak Object Oriented"""

import random
from urllib.request import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%)":
        "Make a class named %%% that is-s %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parametrs.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)": 
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

first_phrase = False

if len(sys.argv) == 2 and sys.argv[1] == "english":
    first_phrase = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.decode("utf-8").strip())


def convert(snippet, phrase):
    results = []
    class_names = [w.capitalize() for w in
                   random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until CTRL+D is hit
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)

            if first_phrase:
                question, answer = answer, question

            print(question)

            input("> ")
            print("ANSWER: %s\n\n" % answer)
except EOFError:
    print("\nBye")
