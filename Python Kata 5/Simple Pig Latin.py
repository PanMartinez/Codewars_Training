def pig_it(text):
    list = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in list])

print (pig_it('This is my string !'))