number = input("PHONE: ")
#Creating a dictionary
digits_mapping = {
        "1": " One ",
        "2": " Two ",
        "3": " Three ",
        "4": " Four "
        }
output = ""
for num in number:
    output += digits_mapping.get(num, "!")
print(output)


