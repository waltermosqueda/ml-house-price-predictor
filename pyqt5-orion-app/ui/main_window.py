from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ORION - Gestión de Productos")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Bienvenido al Sistema de Gestión de Productos ORION")
        layout.addWidget(self.label)

        self.add_button = QPushButton("Agregar Producto")
        self.add_button.clicked.connect(self.add_product)
        layout.addWidget(self.add_button)

        self.show_button = QPushButton("Mostrar Productos")
        self.show_button.clicked.connect(self.show_products)
        layout.addWidget(self.show_button)

        self.update_button = QPushButton("Actualizar Producto")
        self.update_button.clicked.connect(self.update_product)
        layout.addWidget(self.update_button)

        self.delete_button = QPushButton("Eliminar Producto")
        self.delete_button.clicked.connect(self.delete_product)
        layout.addWidget(self.delete_button)

        self.search_button = QPushButton("Buscar Producto")
        self.search_button.clicked.connect(self.search_product)
        layout.addWidget(self.search_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_product(self):
        # Logic to add a product
        pass

    def show_products(self):
        # Logic to show products
        pass

    def update_product(self):
        # Logic to update a product
        pass

    def delete_product(self):
        # Logic to delete a product
        pass

    def search_product(self):
        # Logic to search for a product
        pass