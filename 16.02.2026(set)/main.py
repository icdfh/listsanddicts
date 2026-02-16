# 1)
# products = [
#     {"title": "Iphone", "category": "mobile"},
#     {"title": "Pixel", "category": "mobile"},
#     {"title": "Macbook", "category": "laptop"},
#     {"title": "Lenovo", "category": "laptop"},
#     {"title": "Ipad", "category": "tablet"}
# ]
# catalog = {}
# for i in products:
#     cat = i["category"]
#     title = i["title"]
#     catalog.setdefault(cat,[]).append(title)
# print(catalog)
# 2)

# products = [
#     {"id": 1, "title":"Iphone", "price": 1000},
#     {"id": 2, "title":"Macbook", "price": 2500},
#     {"id": 3, "title":"Ipad", "price": 900},
# ]

# products_by_id = {}
# for i in products:
#     products_by_id[i["id"]] = i
# print(products_by_id)

# print(products_by_id[2]["title"])


# text = "Hi hi Hello hi Bye  "
# words = text.upper().split()

# freq = {}
# for i in words:
#     freq[i] = freq.get(i,0) + 1
# print(freq)

