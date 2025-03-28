message = input(">")
words = message.split(' ') #split is used for breaking a string into substrings
emojis = {
        ":)": "😄",
        ":(": "🙁",
        }
output = " "
for word in words:
    output += emojis.get(word, word)
print(output)
