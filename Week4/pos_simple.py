import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import (QMainWindow, QApplication, QWidget, QVBoxLayout, 
                            QFormLayout, QHBoxLayout, QGroupBox, QFrame, 
                            QMessageBox, QComboBox, QSpinBox, QPushButton, 
                            QLabel, QTextEdit)

class POSApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Setup data produk
        self.products = {
            "Bimoli": 20000,
            "Beras 5 Kg": 75000,
            "Kecap ABC": 7000,
            "Saos Saset": 2500
        }
        
        # Inisialisasi UI
        self.init_ui()
        self.setup_connections()
        
        # Variabel untuk menyimpan transaksi
        self.cart_items = []
    
    def init_ui(self):
        self.setWindowTitle("Aplikasi POS")
        self.setGeometry(100, 100, 500, 500)
        
        # Widget utama
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Group box untuk form input
        input_group = QGroupBox("Input Produk")
        form_layout = QFormLayout()
        
        # Dropdown produk
        self.cb_product = QComboBox()
        for product, price in self.products.items():
            self.cb_product.addItem(f"{product} (Rp {price:,})", userData=price)
        form_layout.addRow("Produk:", self.cb_product)
        
        # Input jumlah
        self.spin_quantity = QSpinBox()
        self.spin_quantity.setMinimum(1)
        self.spin_quantity.setMaximum(999)
        self.spin_quantity.setValue(1)
        form_layout.addRow("Jumlah:", self.spin_quantity)
        
        # Dropdown diskon
        self.cb_discount = QComboBox()
        discounts = ["0%", "5%", "10%", "15%", "20%"]
        self.cb_discount.addItems(discounts)
        form_layout.addRow("Diskon:", self.cb_discount)
        
        input_group.setLayout(form_layout)
        main_layout.addWidget(input_group)
        
        # Tombol aksi
        button_layout = QHBoxLayout()
        self.btn_add = QPushButton("Tambah ke Keranjang")
        self.btn_clear = QPushButton("Hapus Semua")
        button_layout.addWidget(self.btn_add)
        button_layout.addWidget(self.btn_clear)
        main_layout.addLayout(button_layout)
        
        # Area keranjang belanja
        self.cart_display = QTextEdit()
        self.cart_display.setReadOnly(True)
        self.cart_display.setStyleSheet("""
            font-family: Consolas, monospace;
            font-size: 12px;
            background-color: #f8f9fa;
            border: 1px solid #ddd;
            padding: 8px;
        """)
        main_layout.addWidget(self.cart_display)
        
        # Label total
        self.lbl_total = QLabel("Total: Rp 0")
        self.lbl_total.setAlignment(QtCore.Qt.AlignRight)
        self.lbl_total.setStyleSheet("""
            font-weight: bold; 
            font-size: 16px;
            color: #2c3e50;
            padding: 8px;
            background-color: #e9ecef;
            border: 1px solid #ddd;
        """)
        main_layout.addWidget(self.lbl_total)
    
    def setup_connections(self):
        """Setup signal-slot connections"""
        self.btn_add.clicked.connect(self.add_to_cart)
        self.btn_clear.clicked.connect(self.clear_cart)
    
    def add_to_cart(self):
        product_text = self.cb_product.currentText()
        product_name = product_text.split(" (Rp")[0]
        price = self.cb_product.currentData()
        quantity = self.spin_quantity.value()
        discount_text = self.cb_discount.currentText()
        discount = int(discount_text[:-1]) 
        
        # Validasi input
        if quantity <= 0:
            QMessageBox.warning(self, "Peringatan", "Jumlah harus lebih dari 0!")
            return
        
        # Hitung subtotal dengan diskon
        subtotal = price * quantity
        discounted_price = subtotal * (1 - discount / 100)
        
        # Tambahkan ke keranjang
        self.cart_items.append({
            "name": product_name,
            "price": price,
            "quantity": quantity,
            "discount": discount,
            "subtotal": discounted_price
        })
        
        self.update_cart_display()
        self.spin_quantity.setValue(1)
        self.cb_discount.setCurrentIndex(0)
    
    def update_cart_display(self):
        cart_text = ""
        total = 0
        
        # Generate text untuk setiap item
        for item in self.cart_items:
            line = (f"{item['name']} (Rp {item['price']:,}) - "
                   f"{item['quantity']} x Rp {item['price']:,} "
                   f"(disc {item['discount']}%)\n")
            cart_text += line
            total += item['subtotal']
        
        # Update tampilan
        self.cart_display.setPlainText(cart_text)
        self.lbl_total.setText(f"Total: Rp {total:,.0f}")
    
    def clear_cart(self):
        self.cart_items = []
        self.cart_display.clear()
        self.lbl_total.setText("Total: Rp 0")
        self.spin_quantity.setValue(1)
        self.cb_discount.setCurrentIndex(0)

def main():
    # Untuk menghindari warning scaling
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    
    app = QApplication(sys.argv)
    window = POSApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()