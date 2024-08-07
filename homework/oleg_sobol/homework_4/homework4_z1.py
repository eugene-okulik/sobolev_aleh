my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [11, 12, 13, 14, 15],
    'dict': {'a': 21, 'b': 22, 'c': 23, 'd': 24, 'e': 25},
    'set': {31, 32, 33, 34, 35}
}
print(my_dict['tuple'][-1])
my_dict['list'].append(16)
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 26
del my_dict['dict']['a']
my_dict['set'].add(36)
my_dict['set'].discard(31)
for key, value in my_dict.items():
    print(f"{key}: {value}")
