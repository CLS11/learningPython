customer = {
        "name": "John Smith", #key
        "age": 30,
        "is_verified": True
        } #dictionary
print(customer.get("bc")) #get doesnt give us error and instead gives none
#giving the non-existent key a default value
print(customer.get("ab", "890"))
#updating the value
customer["name"] = "Joseph"
print(customer["name"])
