u_input = input("Enter your favorite quote: ")

def analyzesentence(text):
    # count characters
    count_ch = 0
    for ch in text:
        if ch != " ":
            count_ch += 1

    # count words (spaces + 1)
    count_sp = 0
    for char in text:
        if char == " ":
            count_sp += 1
    word_count = count_sp + 1

    # count vowels
    vowels = "aeiouAEIOU"
    vowel_count = 0
    for ch in text:
        if ch in vowels:
            vowel_count += 1

    # reverse manually
    rev = ""
    for i in range(len(text) - 1, -1, -1):
        rev += text[i]

    return count_ch, word_count, vowel_count, rev


# get values from the function
chars, words, vowels, reversed_sentence = analyzesentence(u_input)

# print results
print("Total characters:", chars)
print("Total words:", words)
print("Vowel count:", vowels)
print("Reversed sentence:", reversed_sentence)
