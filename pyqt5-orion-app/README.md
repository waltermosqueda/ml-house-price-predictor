# pyqt5-orion-app/pyqt5-orion-app/README.md

# PyQt5 Orion App

## Overview
The PyQt5 Orion App is a graphical user interface application for managing products in an inventory system. It provides functionalities to add, update, delete, and display products using a user-friendly interface.

## Project Structure
```
pyqt5-orion-app
├── ui
│   ├── main_window.py      # Implementation of the main window
│   └── main_window.ui      # Qt Designer file for the main window layout
├── main.py                 # Entry point of the application
├── orion.py                # Logic for managing products
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

## Requirements
To run this application, you need to have Python installed along with the following packages:

- PyQt5
- sqlite3 (included with Python)

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Running the Application
To start the application, run the following command in your terminal:

```
python main.py
```

## Features
- Add new products to the inventory
- Update existing product details
- Delete products from the inventory
- Search for products by name or ID
- Generate reports for low stock items
- Export product data to CSV files

## License
This project is licensed under the MIT License. See the LICENSE file for more details.