
# JSON Data Processing Script

## Overview

This Python script is designed for processing a JSON file containing customer orders. The script reads the input JSON file, which contains information about orders including customer names, phone numbers, and items ordered with their prices. It then generates two dictionaries: one mapping customer phone numbers to names, and another summarizing the orders made for each item, including the total number of orders and the price of each item. Finally, it outputs these dictionaries to `customers.json` and `items.json` files, respectively.

## Features

- Reads customer order data from a JSON file.
- Generates a dictionary linking customer phone numbers to their names.
- Creates a summary of items ordered, including their prices and the total number of orders for each item.
- Outputs these dictionaries to `customers.json` and `items.json`.

## Dependencies

Ensure you have Python installed on your system. This script was developed with Python 3.8 but should be compatible with Python 3.6+.

No external libraries are required for the main functionality. The script uses standard Python modules `json` and `sys`.

## How to Run

1. Place your order JSON file in a known directory.
2. Modify the script to point to your JSON file. This can be done by replacing `sys.argv[1]` with the path to your file in quotes, or by passing the file path as an argument when running the script.
3. Open a terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using Python by typing the following command:

   ```sh
   python python_script.py path_to_your_json_file.json
   ```

   Replace `python_script.py` with the name of your Python script and `path_to_your_json_file.json` with the path to your JSON file.

## Output

The script will create or overwrite `customers.json` and `items.json` in the directory where the script is run. These files contain the processed data in JSON format, structured as described in the Features section.

## Contribution

Feel free to fork this repository and submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.

Ensure to update tests as appropriate.
