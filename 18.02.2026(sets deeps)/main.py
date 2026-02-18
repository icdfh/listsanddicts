# Пустой сэт
# s = set()
# print(s)
# print(type(s))

# # Пустой словарь
# x = {}

# nums = [1,2,2,2,3,3,4,5,5]
# s = set(nums)
# print(s)

# t = (10,10,20,30,30,90,40,40)
# print(set(t))

# s = set()
# s.add(5)
# s.add(5)
# s.add(5)
# s.add(6)
# print(s)

# s = {1,2}
# s.update([2,3,4])
# print(s)

# s = {1,2,3}
# s.remove(4)
# s.discard(2)
# s.discard(10)
# s.pop()
# print(s)

# s = {1,2}
# s.clear()
# print(s)
# len, in
# s = {2,4,6}
# print(len(s)) 
# print(4 in s) 
# print(5 in s) 

# Математика

# a = {1,2,3,4}
# b = {3,4,5}
# print(a | b) #union
# print(a & b)
# print(a.intersection(b))
# print(a - b)
# print(b - a)
# print(a.difference(b))

# 1
# nums = [5,5,5,2,2,2,2,4,4,4,1,1,2,3,5,1]
# unique_nums = list(set(nums))
# print(unique_nums)

# 2 Удаление дублей, сохранение порядка
# nums = [5,5,5,2,2,2,2,4,4,4,1,1,2,3,5,1]
# seen = set()
# result = []

# for i in nums:
#     if i not in seen:
#         seen.add(i)
#         result.append(i)
# print(result)

# 3
# blacklist = {"spam", "ads", "scam"}
# msg = "spam scam ads"
# words = msg.split()
# print(words)

# found = False
# for i in words:
#     if i in blacklist:
#         print("Я нашел!", i)
# print("Blocked word: ", found)

# 4
# text = "Hello Python"
# letters = set()

# for i in text.lower():
#     if i != " ":
#         letters.add(i)

# print(letters)
# print("count:", len(letters))

# 5
# nums = [1,2,2,3,4,4,4,5]
# seen = set()
# dups = set()

# for i in nums:
#     if i in seen:
#         dups.add(i)
#     else:
#         seen.add(i)
# print("duplicate: ", dups)

# 6
# a = [1,2,3,4,5]
# b = [4,5,6,7]
# common = set(a) & set(b)
# print(common)

# 7 Кто ушел / Кто пришел(разность)
# old = ["Ayan", "Dana", "Mira", "Ilyas"]
# new = ["Dana", "Mira", "Sasha"]

# old_set = set(old)
# new_set = set(new)

# left = old_set - new_set
# joined = new_set - old_set
# print("left: ", left)
# print("joined: ",joined)

# 8 Уникальные слова + частоты

# text = "cat dog dog bird cat dog" 
# words = text.split()

# unique_words = set(words)
# asd = {}

# for i in words:
#     asd[i] = asd.get(i,0) + 1

#     print("unique:", unique_words)
#     print("Частота:", asd)

# 9 
# logins = ["icdfh", "admin","icdfh","user", "admin"]
# used = set()

# for i in logins:
#     if i in used:
#         print("duplicate", i)
#     else:
#         used.add(i)

# 10
# stop = {"и", "а", "но", "это"}
# words = ["это", "очень", "круто", "и", "полезно"]

# filtered = []
# for i in words:
#     if i not in stop:
#         filtered.append(i)
# print(filtered)

# points = set()
# points.add((10,20))
# points.add((10,20))
# points.add((5,7))

# print(points) #((10,20), (5,7))
# print((5,7) in points) #True

