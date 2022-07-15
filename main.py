
dict = {
    "1": "Zohaib",
    "2": "Hassan"
}
dict.update({"3": "Awais"})
print(dict)

print(dict["2"])

for values in dict.items():
    print(values)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic4 = {}
for combine in dic1, dic2, dic3:
    dic4.update(combine)

print(dic4)
print(dic4.items(), "\n")

for dic4_keys, dic4_values in dic4.items():
    print(dic4_keys, " ", dic4_values)



"""Create Class and object for checking present values"""

class CheckPresent:

    def is_key_present(self, key):
        if key in dic4.keys():
            print("Key is present in Dictionary")
        else:
            print("Key is not present in Dictionary")

    def is_value_present(self, value):
        if value in dic4.values():
            print("Value is present in Dictionary")
        else:
            print("Value is not present in Dictionary")


object_class = CheckPresent()
object_class.is_key_present(5)
object_class.is_value_present(70)

print("\n")
"""Create dic of x: x*x"""

input_number = int(input("Enter a Number "))
dic = {}
for dictionary in range(1, input_number + 1):
    dic[dictionary] = dictionary*dictionary
print(dic)
print(type(dic))





