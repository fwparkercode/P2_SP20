# Dictionaries (dict)

# str, int, bool, list, tuple, dict, set, object

# Quick look at sets
# not used widely in Python
# sets store UNIQUE values as unordered group
import random

my_set = {1, 2, 3, 4, 4, 5}  # eliminated duplicates
print(my_set)

# one very specific use of a set
my_list = [6, 7, 8, 9, 8, 7]  # list with duplicates
print(set(my_list))

my_list = list(set(my_list))  # list minus the duplicates (UNIQUE)
print(my_list)


# Dictionaries are just unordered collections of key: value info

# Why use a dict over list
mr_lee = ['Aaron', 'Lee', 46, ['Python', 'SQL']]
mr_leed = {'first': 'Aaron', 'last': 'Lee', 'age': 46, 'fav_prog_lang': ['Python', 'SQL']}

# structure {key1: val1, key2: val2...}

# Accessing values
print(mr_leed['age'])  # index a dict using the key
print(mr_leed['fav_prog_lang'][1])

# iterable with the keys
for key in mr_leed:
    print(mr_leed[key])

# adding to a dict
mr_leed['spoken_langs'] = ['English', 'Pig Latin']
print(mr_leed)

# cannot be access by index number
#  print(mr_leed[0])  # gives a keyerror if you don't know the key

# Build a simple dict object

community = {'genre': ['Comedy'],
             'creators': ['Dan Harmon'],
             'starring': ['Joel McHale', 'Gillian Jacobs', 'Danny Pudi'],
             'no_season': 6
             }

community['no_episodes'] = 110
print(community['no_episodes'])

# change items in a dict
community['starring'].append('Alison Brie')
print(community['starring'])

# increment item
community['no_episodes'] += 1
print(community['no_episodes'])

# keys method
print(community.keys())
print(list(community.keys()))

# values method
print(community.values())
print(list(community.values()))

#  dictionary to track values
my_list = [random.choice(['heads', 'tails']) for x in range(50)]
print(my_list)

my_flips_dict = {}

for flip in my_list:
    if flip == 'heads':
        if flip in my_flips_dict:
            my_flips_dict['heads'] += 1
        else:
            my_flips_dict['heads'] = 1
    if flip == 'tails':
        if flip in my_flips_dict:
            my_flips_dict['tails'] += 1
        else:
            my_flips_dict['tails'] = 1



print(my_flips_dict)










