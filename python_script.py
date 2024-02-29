import json

with open(r'C:\Users\customer\Desktop\IS601\midterm_project\example_orders.json', 'r') as f:
    data = json.load(f)

dictionary1 = {}

#dictionary2 = {}


for i in data:
    dictionary1[i['phone']] = i['name']
    #for j in i['items']:
        #dictionary2[j['name']] = j['price']
print(dictionary1)

output_dict = {}

# Iterate through the data and extract information about each item
for order in data:
    for item in order['items']:
        item_name = item['name'].lower()
        if item_name not in output_dict:
            output_dict[item_name] = {
                'price': item['price'],
                'orders': 1  # Initialize the count to 1 for the first occurrence
            }
        else:
            output_dict[item_name]['orders'] += 1  # Increment the count for subsequent occurrences

# Print the output dictionary
print(output_dict)
with open('customers.json', 'w') as f:
    json.dump(dictionary1, f, indent=4)

with open('items.json', 'w') as f:
    json.dump(output_dict, f, indent=4)
