def spin_words(sentence):

    new_sen = []
    list = sentence.split()

    for word in list:

        if len(word) >= 5:
            new_sen.append(word[::-1])
        else:
            new_sen.append(word)


    return " ".join(new_sen)

print(spin_words("Welcome"))