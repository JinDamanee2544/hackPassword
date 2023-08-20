import hashlib
from itertools import product

checkHash = "d54cc1fe76f5186380a0939d2fc1723c44e8a5f7"

sub = {
    "o": "0",
    "l": "1",
    "i": "1",
}


def hash(word):
    return hashlib.sha1(word.encode("utf-8")).hexdigest()


def checkHash(text, checkHash=checkHash):
    return hash(text) == checkHash


def genCaseCombination(text):
    char_combinations = [(char.lower(), char.upper()) for char in text]
    combinations = product(*char_combinations)
    return ["".join(item) for item in combinations]


def getSubsitueCombintion(text):
    char_combinations = []
    for char in text:
        if char in sub:
            char_combinations.append((char, sub[char]))
        else:
            char_combinations.append((char,))
    combinations = product(*char_combinations)
    return ["".join(item) for item in combinations]
