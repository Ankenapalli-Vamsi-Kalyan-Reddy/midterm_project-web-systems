import json
import sys
#with open(r'C:\Users\customer\Desktop\IS601\midterm_project\example_orders.json', 'r') as f:
with open(sys.argv[1], 'r') as f:
    data = json.load(f)

dictionary1 = {}

#dictionary2 = {}


for i in data:
    if isinstance(i, dict):
        dictionary1[i['phone']] = i['name']
    else:
        print("unexpected data format:", i)
    #for j in i['items']:
        #dictionary2[j['name']] = j['price']
print('==================================================================================================================')
print(dictionary1)

output_dict = {}


for order in data:
    for item in order['items']:
        item_name = item['name'].lower()
        if item_name not in output_dict:
            output_dict[item_name] = {
                'price': item['price'],
                'orders': 1 
            }
        else:
            output_dict[item_name]['orders'] += 1  
print('==================================================================================================================')
print(output_dict)
with open('customers.json', 'w') as f:
    json.dump(dictionary1, f, indent=4)

with open('items.json', 'w') as f:
    json.dump(output_dict, f, indent=4)
