def capslock(sentence):
    if len(sentence) > 10:
        return sentence.upper()
    else:
        return sentence

print(capslock("Hello World"))
print(capslock("goodbye"))