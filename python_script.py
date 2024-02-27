import json
# with open(r'C:\Users\customer\Desktop\IS601\midterm_project\example_orders.json', 'r') as f:
#     data = json.load(f)
# #print(data)
# dictionary1 = {}
# for i in data:
#     dictionary1[i['phone']] = i['name']
# # print(dictionary1)

# with open('customers.json', 'w') as f:
#     json.dump(dictionary1, f, indent=4)

# dictionary2 = {}
# for i in data:
#     for j in data:
#         dictionary2[i['items'][0]['name']] = i['items'][0]['price']
# # print(dictionary2)

# with open('items.json', 'w') as f:
#     json.dump(dictionary2, f, indent=4)

with open(r'C:\Users\customer\Desktop\IS601\midterm_project\example_orders.json', 'r') as f:
    data = json.load(f)

dictionary1 = {}
dictionary2 = {}


for i in data:
    dictionary1[i['phone']] = i['name']
    for j in i['items']:
        dictionary2[j['name']] = j['price']
print(dictionary1)
print(dictionary2)
with open('customers.json', 'w') as f:
    json.dump(dictionary1, f, indent=4)

with open('items.json', 'w') as f:
    json.dump(dictionary2, f, indent=4)
