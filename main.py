"""
    This is a program that alllows to classify nouns in polish language depending on its gender. 
    It uses simple rules based on common noun endings.
    It is intended for educational purposes only.
    Polish nouns can be tricky, and there are many exceptions to these rules.
    This is a simple implementation and may not cover all cases.
    For example, some masculine nouns can end with "a" or "i" and still be masculine.
    Additionally, some feminine nouns can end with consonants.
"""

def is_noun(word):
    """
    Check if the word is a noun based on its ending.
    """
    
    # Feminine nouns
    if word.endswith(("a", "ni", "ość", "dź")):
        return "Feminine"

    # Neuter nouns
    elif word.endswith(("o", "e", "ę", "um")):
        return "Neuter"

    # Masculine nouns
    elif word.endswith(("b", "p", "c", "d", "f", "g", "r", "s", "ś", "h", "j", "k", "l", "ł", "m", "n", "ń", "t", "w", "x", "z", "ź", "ż")):
        return "Masculine"

    # Masculine nouns - exceptions
    elif word in ["kierowca", "sprzedawca", "wykładowca", "wykonawca", "mężczyzna", "bandyta", "banita", "komunista", "kosmita", "obrońca", "poeta", "starosta", "wojewoda"] or word.endswith("ista") or word.endswith("ysta"):
        return "Masculine"

    return None

def is_adjective(word):
    # Check if the word is most likely an adjective
    if word.endswith(("ny", "na", "ne", "owy", "owe", "owa", "ujący", "ująca", "ujące")):
        return True
    
    return False

def is_verb(word):
    # Check if the word is most likely a verb
    if word.endswith(("ać", "yć", "ić", "ować")):
        return True
        
    return False

def main():
    input_word = input("Please enter your word in the main form: ")

    # Santize the input
    word = input_word.strip().lower()

    gender = is_noun(word)

    if(gender != None):
        print(f"The noun '{word}' is most likely {gender}.")
        return
    
    print("Looks like the word you entered may not be a noun in Polish. Check the word you entered to make sure it is a dictionary form.")

    if is_adjective(word):
        print("The word is probably an adjective.")
        return
    
    if is_verb(word):
        print("The word is probably a verb in its infinitive form.")
        return
    
    print("The word is probably not a noun, adjective, or verb in Polish.")


if __name__ == "__main__":
    main()
    