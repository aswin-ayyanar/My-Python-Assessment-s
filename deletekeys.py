# Given dictionary
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["age", "city"]
for i in keys:
    if i in sample_dict:
        del sample_dict[i]
print(sample_dict)