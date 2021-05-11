'''
____________Rules for Jungle Language Translator____________
Every vowel becomes its corresponding number from 1 through 5
Every consonant becomes that consonant with 'a' added to it
'''

# Function for translator
def translator(phrase):
    for old, new in (
        # Translation for lower case
        ("a", "1"),
        ("b", "ba"),
        ("c", "ca"),
        ("d", "da"),
        ("e", "2"),
        ("f", "fa"),
        ("g", "ga"),
        ("h", "ha"),
        ("i", "3"),
        ("j", "ja"),
        ("k", "ka"),
        ("l", "la"),
        ("m", "ma"),
        ("n", "na"),
        ("o", "4"),
        ("p", "pa"),
        ("q", "qa"),
        ("r", "ra"),
        ("s", "sa"),
        ("t", "ta"),
        ("u", "5"),
        ("v", "va"),
        ("w", "wa"),
        ("x", "xa"),
        ("y", "ya"),
        ("z", "za"),
        # Translation for upper case
        ("A", "1"),
        ("B", "BA"),
        ("C", "CA"),
        ("D", "DA"),
        ("E", "2"),
        ("F", "FA"),
        ("G", "GA"),
        ("H", "HA"),
        ("I", "3"),
        ("J", "JA"),
        ("K", "KA"),
        ("L", "LA"),
        ("M", "MA"),
        ("N", "NA"),
        ("O", "4"),
        ("P", "PA"),
        ("Q", "QA"),
        ("R", "RA"),
        ("S", "SA"),
        ("T", "TA"),
        ("U", "5"),
        ("V", "VA"),
        ("W", "WA"),
        ("X", "XA"),
        ("Y", "YA"),
        ("Z", "ZA"),
        ):
        phrase = phrase.replace(old, new)
    return phrase


print(translator(input("Enter Word or Sentence: ")))
