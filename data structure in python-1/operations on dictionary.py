my_dict = {}
my_dict = {1 : 'apple', 2 : 'banana', 3 : 'cherry'}
my_dict = {'name ': 'John', 1 : [2, 4, 3]}
my_dict = {'name' : 'Jack', 'age' : 26}
print(my_dict)
print(my_dict['name'])
print(my_dict['age'])
my_dict['age'] = 27
print(my_dict)
my_dict['address'] = 'New York'
print(my_dict)
print('address :', my_dict.get('address'))
my_dict.clear()
print(my_dict)