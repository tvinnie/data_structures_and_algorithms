import time

# Sample data
set1 = set(range(1000))
set2 = set(range(500, 1500))
list1 = list(set1)
list2 = list(set2)

# Union
start_time = time.time()
union_set = set1.union(set2)
print("Set Union Time:", time.time() - start_time)

start_time = time.time()
union_list = list(set(list1 + list2))
print("List Union Time:", time.time() - start_time)

# Intersection
start_time = time.time()
intersection_set = set1.intersection(set2)
print("Set Intersection Time:", time.time() - start_time)

start_time = time.time()
intersection_list = [x for x in list1 if x in set2]
print("List Intersection Time:", time.time() - start_time)

# Difference
start_time = time.time()
difference_set = set1.difference(set2)
print("Set Difference Time:", time.time() - start_time)

start_time = time.time()
difference_list = [x for x in list1 if x not in set2]
print("List Difference Time:", time.time() - start_time)


# OUTPUT
"""
Set Union Time: 9.489059448242188e-05
List Union Time: 0.00022459030151367188
Set Intersection Time: 8.058547973632812e-05
List Intersection Time: 0.00015497207641601562
Set Difference Time: 7.700920104980469e-05
List Difference Time: 0.0001628398895263672

"""