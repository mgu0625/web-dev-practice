
def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
    return letters

def count_words(text):
    words = 0
    in_word = False

    for char in text:
        if char.isspace():
            in_word = False
        elif not in_word:
            words += 1
            in_word = True
    return words

def count_sentences(text):
    sentences = 0
    for char in text:
        if char in [".", "!", "?"]:
            sentences += 1
    return sentences

def main():
    text = input("Paste Text to evaluate: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if index < 1:
        print("Before Grade 1")
    elif index >= 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")

main()