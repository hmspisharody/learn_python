dict_a = {2: 'is', 1: 'Hari', 5: 'boy', 3: 'a', 4: 'good'}

sorted_dict = {x: dict_a[x] for x in sorted(dict_a.keys())}

print(sorted_dict)
