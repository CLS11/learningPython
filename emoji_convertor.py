message = input(">")
words = message.split(' ') #split is used for breaking a string into substrings
def emojis(word):
    if word == ":)":
        return "😄"
    elif word == ":(":
        return "🙁"

output = " ".join([emojis(word) for word in words])
#converted the list to string
print(output)
