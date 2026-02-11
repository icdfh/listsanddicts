# ages = {
#     "Ali": 18,
#     "Mansur": 21,
#     "Dana":17
# }
# ages["Ali"] = 19
# ages["Qwerty"] = 33
# print(ages)
# print(ages["Ali"],ages["Dana"],ages["Mansur"])
# print(ages["Dana"])
# print(ages["Mansur"])
# print(ages.get("Ali"))
# del ages["Ali"]
# print(ages)

# if "Mansur" in ages:
#     print("Есть")
# else:
#     print("Нет")

ages = {
    "Ali": 18,
    "Mansur": 21,
    "Dana":17
}
# for i in ages:
#     print(i)
# for i in ages.keys():
#     print(i)
# for i in ages.values():
#     print(i)
# for keys,values in ages.items():
#     print("Keys:",keys,"Values:",values)
# ТАК НЕ ДЕЛАЕМ
# a = {
#     "id1": 1, "name":"Ali",
#     "id2": 2, "name":"Ali",
#     "id3": 3, "name":"Ali"
# }

# users = [
#     {"id":1, "name": "Ali"},
#     {"id":2, "name": "Dana"},
#     {"id":3, "name": "Mansur"}
# ]
# users = {
#     1:{"name":"Ali"},
#     2:{"name":"Mansur"},
#     3:{"name":"Dana"}
# }
# print(users[1]["name"])
# print(users[2]["name"])
# print(users[3]["name"])
# user = {
#     "id": 7,
#     "name": "Dana",
#     "skills":["HTML", "CSS", "JS"],
#     "contact": {
#         "phone": "+77077077777",
#         "tg": ["@dana", "@danatunes", "@dana.narxoz"]
#     }
# }
# print(user["contact"]["tg"][2])
# print(user["skills"][0])

# Примеры
# 1) Телефонная книга
# phonebook = {}
# phonebook["Ali"] = "+77017011111"
# phonebook["Dana"] = "+77777414141"
# phonebook["Mansur"] = "+77087088888"
# for name,phone in phonebook.items():
#     print(f"{name} => {phone}")

# 2) Безопасный поиск
# phonebook = {
#     "Ali": "111",
#     "Mansur": "222"
# }
# name = input("Введите имя: ")
# phone = phonebook.get(name)
# if phone is None:
#     print("Нет контакта")
# else:
#     print("Телефон", phone)

# 3) Подсчет частоты
# nums = [1,2,2,3,3,3,5,5]
# asd = {}
# for i in nums:
#     if i in asd:
#         asd[i] += 1
#     else:
#         asd[i] = 1
# print(asd)

nums = [5,5,2,2,2,3,3,3,5,1,1,1,4,4,4,4,4,4]
asd = {}
for i in nums:
    asd[i] = asd.get(i,0) + 1
best_num = None
best_count = -1

for num, count in asd.items():
    if count > best_count or (count == best_count and (best_num is None or num < best_num)):
        best_num = num
        best_count = count
print("asd", asd)
print("most asd =",best_num, "count =",best_count)