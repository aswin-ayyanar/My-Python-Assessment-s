dict1 = {'company1': 'Mahindra', 'model1': 'Thar', 'year1': '2010'}
dict2 = {'company2': 'Suzuki', 'model2': 'Gypsy', 'year2': '1985'}
m = {**dict1, **dict2}
#We can combine by unpacking both dictionaries inside another dictionary using the (**) Double Asterisks
print('Merged dictionary is: ', m)