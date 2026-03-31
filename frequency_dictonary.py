my_dict = {"Codingal": 3, "is": 2, "best": 2, "for": 2, "Coding": 1}
print(my_dict)
frequency_value = (input("enter the number you want to check the frequency of: "))
frequency = list(my_dict.values()).count(frequency_value)
print(f"The value {frequency_value} appears {frequency} times.")
