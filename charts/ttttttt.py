dct_bd = [{'name_q': 'asdsa', 'date': '123123', 'field_0': 1, 'field_1': 2, 'field_2': 3, 'field_3': 4},
 {'name_q': 'asdsa', 'date': '4235', 'field_0': 5, 'field_1': 6, 'field_2': 7, 'field_3': 8},
 {'name_q': 'asdsa', 'date': '123512', 'field_0': 9, 'field_1': 10, 'field_2': 11, 'field_3': 12}, ]

# [{'asdsa': {'field_0': [1, 5, 9], 'field_1': [2, 6, 10], 'field_2': [3, 7, 11], 'field_3': [4, 8, 12], }}]

lst = {'asdsa': {}}

for i in dct_bd:
    for key, val in i.items():
        lst['asdsa'].setdefault(key, []).append(val)

print(lst)