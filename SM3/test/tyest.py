# import json
#
# with open('cats_json.json') as cat_file:
#     data = json.load(cat_file)
#     print(data)
# for key, value in data.items():
#     if type(value) == list:
#         print(f'{key}: {", ".join(value)}')
#     else:
#         print(f'{key}: {value}')
#
#
# import json
#
# with open('cats_2.json') as cat_file:
#     f = cat_file.read()
#     print(f)
#     data = json.loads(f)
#     print(data)
#     for item in data:
#         for key, value in item.items():
#             if type(value) == list:
#                 print(f'{key}: {", ".join(value)}')
#             else:
#                 print(f'{key}: {value}')
#         print()



# import json
#
# cats_dict = {
#     'name': 'Pushin',
#     'age': 1,
#     'meals': [
#         'Purina', 'Cat Chow', 'Hills'
#     ],
#     'owners': [
#         {
#             'first_name': 'Bill',
#             'last_name': 'Gates'
#         },
#         {
#             'first_name': 'Melinda',
#             'last_name': 'Gates'
#         }
#     ]
# }
#
# with open('cats_3.json', 'w') as cat_file:
#     json.dump(cats_dict, cat_file)


import json

weekdays = {i: day
            for i, day in enumerate(['Sunday',
                                     'Monday',
                                     'Tuesday',
                                     'Wednesday',
                                     'Thursday',
                                     'Friday',
                                     'Saturday'
                                     ])}
data = json.dumps(weekdays)
print(data)
print(type(data))