alphabet = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}


def encode(value, n):
  result = []
  for s in value.lower():
    if s in alphabet:
      s = alphabet[s]
      result.append(
          list(alphabet.keys())[list(alphabet.values()).index((s + n) % 26)])
    else:
      result.append(s)
  return "".join(result)


print(encode("hi", 2))