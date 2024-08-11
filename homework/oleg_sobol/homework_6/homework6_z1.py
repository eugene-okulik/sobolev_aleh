text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)
words = text.split()
fin_words = []
for word in words:
    if word[-1] in ",.":
        fin_words.append(word[:-1] + "ing" + word[-1])
    else:
        fin_words.append(word + "ing")
print(" ".join(fin_words))
