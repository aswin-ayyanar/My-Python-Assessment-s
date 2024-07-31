sample_dict = {'a': 100, 'b': 200, 'c': 300}
A = int(input("Value to be check: "))
if A in sample_dict.values():
    print("Value exists in the dictionary.")
else:
    print("Value does not exist in the dictionary.")