def longest_word(sentence):
    words = sentence.split()
    longest_word = words.pop(0)

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word