import sys
import csv
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
                             QMessageBox, QComboBox, QDockWidget, QScrollArea, QStatusBar)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QClipboard
import sqlite3

class EnhancedDatabaseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enhanced Database Application")
        self.setGeometry(100, 100, 900, 700)
        
        # Database setup
        self.conn = sqlite3.connect('data.db')
        self.create_table()
        
        # Clipboard setup
        self.clipboard = QApplication.clipboard()
        
        # Main widget and scroll area
        self.main_widget = QWidget()
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.main_widget)
        self.scroll.setWidgetResizable(True)
        self.setCentralWidget(self.scroll)
        
        # Main layout
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)
        
        # Status bar
        self.setup_status_bar()
        
        # Dock widget for search
        self.setup_search_dock()
        
        # Input form with clipboard integration
        self.setup_input_form()
        
        # Table display with scrolling
        self.setup_table()
        
        # Buttons for delete and export
        self.setup_buttons()
        
        # Load initial data
        self.load_data()
    
    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                year INTEGER,
                status TEXT
            )
        ''')
        self.conn.commit()
    
    def setup_status_bar(self):
        self.statusBar().showMessage("Created by: Your Name | NIM: YourNIM | Status: Ready")
    
    def setup_search_dock(self):
        self.search_dock = QDockWidget("Search Panel", self)
        self.search_dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        
        dock_widget = QWidget()
        dock_layout = QVBoxLayout()
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by name...")
        self.search_input.textChanged.connect(self.search_data)
        dock_layout.addWidget(self.search_input)
        
        # Add help/info label
        help_label = QLabel("Tip: Type in the search box to filter records.\nDouble-click to edit.\nUse buttons to delete or export.")
        help_label.setWordWrap(True)
        dock_layout.addWidget(help_label)
        
        dock_widget.setLayout(dock_layout)
        self.search_dock.setWidget(dock_widget)
        self.addDockWidget(Qt.RightDockWidgetArea, self.search_dock)
    
    def setup_input_form(self):
        form_scroll = QScrollArea()
        form_scroll.setWidgetResizable(True)
        form_widget = QWidget()
        form_layout = QVBoxLayout()
        
        # Name field with clipboard
        name_layout = QHBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        name_layout.addWidget(self.name_input)
        
        paste_button = QPushButton("Paste")
        paste_button.clicked.connect(self.paste_from_clipboard)
        name_layout.addWidget(paste_button)
        form_layout.addLayout(name_layout)
        
        # Category field
        self.category_input = QComboBox()
        self.category_input.addItems(["Personal", "Work", "Education", "Other"])
        form_layout.addWidget(QLabel("Category:"))
        form_layout.addWidget(self.category_input)
        
        # Year field
        self.year_input = QLineEdit()
        self.year_input.setPlaceholderText("Year (YYYY)")
        form_layout.addWidget(QLabel("Year:"))
        form_layout.addWidget(self.year_input)
        
        # Status field
        self.status_input = QComboBox()
        self.status_input.addItems(["Active", "Inactive", "Pending"])
        form_layout.addWidget(QLabel("Status:"))
        form_layout.addWidget(self.status_input)
        
        # Save button
        self.save_button = QPushButton("Save Record")
        self.save_button.clicked.connect(self.save_record)
        form_layout.addWidget(self.save_button)
        
        form_widget.setLayout(form_layout)
        form_scroll.setWidget(form_widget)
        self.layout.addWidget(form_scroll)
    
    def setup_table(self):
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Category", "Year", "Status"])
        self.table.setColumnHidden(0, True)  # Hide ID column
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.doubleClicked.connect(self.edit_record)
        
        # Enable scrolling
        self.table.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        self.layout.addWidget(self.table)
    
    def setup_buttons(self):
        button_layout = QHBoxLayout()
        
        self.delete_button = QPushButton("Delete Selected")
        self.delete_button.clicked.connect(self.delete_record)
        button_layout.addWidget(self.delete_button)
        
        self.export_button = QPushButton("Export to CSV")
        self.export_button.clicked.connect(self.export_to_csv)
        button_layout.addWidget(self.export_button)
        
        self.layout.addLayout(button_layout)
    
    def paste_from_clipboard(self):
        clipboard_text = self.clipboard.text()
        if clipboard_text:
            self.name_input.setText(clipboard_text)
            self.statusBar().showMessage("Text pasted from clipboard", 3000)
        else:
            self.statusBar().showMessage("Clipboard is empty or contains non-text data", 3000)
    
    def load_data(self, filter_text=None):
        cursor = self.conn.cursor()
        
        if filter_text:
            cursor.execute("SELECT * FROM records WHERE name LIKE ?", 
                          (f"%{filter_text}%",))
        else:
            cursor.execute("SELECT * FROM records")
        
        records = cursor.fetchall()
        
        self.table.setRowCount(len(records))
        for row_idx, record in enumerate(records):
            for col_idx, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row_idx, col_idx, item)
    
    def save_record(self):
        name = self.name_input.text().strip()
        category = self.category_input.currentText()
        year = self.year_input.text().strip()
        status = self.status_input.currentText()
        
        if not name or not year:
            QMessageBox.warning(self, "Warning", "Name and Year are required fields!")
            return
        
        try:
            year_int = int(year)
        except ValueError:
            QMessageBox.warning(self, "Warning", "Year must be a number!")
            return
        
        cursor = self.conn.cursor()
        
        # Check if we're editing an existing record
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            record_id = self.table.item(selected_row, 0).text()
            cursor.execute('''
                UPDATE records 
                SET name=?, category=?, year=?, status=?
                WHERE id=?
            ''', (name, category, year_int, status, record_id))
            self.statusBar().showMessage(f"Record {record_id} updated", 3000)
        else:
            cursor.execute('''
                INSERT INTO records (name, category, year, status)
                VALUES (?, ?, ?, ?)
            ''', (name, category, year_int, status))
            self.statusBar().showMessage("New record added", 3000)
        
        self.conn.commit()
        
        # Clear inputs and refresh table
        self.name_input.clear()
        self.year_input.clear()
        self.category_input.setCurrentIndex(0)
        self.status_input.setCurrentIndex(0)
        self.load_data()
    
    def edit_record(self, index):
        row = index.row()
        
        # Get data from selected row
        record_id = self.table.item(row, 0).text()
        name = self.table.item(row, 1).text()
        category = self.table.item(row, 2).text()
        year = self.table.item(row, 3).text()
        status = self.table.item(row, 4).text()
        
        # Populate form with selected data
        self.name_input.setText(name)
        
        category_index = self.category_input.findText(category)
        if category_index >= 0:
            self.category_input.setCurrentIndex(category_index)
        
        self.year_input.setText(year)
        
        status_index = self.status_input.findText(status)
        if status_index >= 0:
            self.status_input.setCurrentIndex(status_index)
        
        self.statusBar().showMessage(f"Editing record {record_id}", 3000)
    
    def delete_record(self):
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Warning", "Please select a record to delete!")
            return
        
        record_id = self.table.item(selected_row, 0).text()
        
        reply = QMessageBox.question(self, 'Confirm Delete', 
                                    'Are you sure you want to delete this record?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            cursor = self.conn.cursor()
            cursor.execute("DELETE FROM records WHERE id=?", (record_id,))
            self.conn.commit()
            self.load_data()
            self.statusBar().showMessage(f"Record {record_id} deleted", 3000)
    
    def search_data(self):
        filter_text = self.search_input.text()
        self.load_data(filter_text)
        self.statusBar().showMessage(f"Searching for: {filter_text}", 3000)
    
    def export_to_csv(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM records")
        records = cursor.fetchall()
        
        if not records:
            QMessageBox.warning(self, "Warning", "No data to export!")
            return
        
        filename, _ = QFileDialog.getSaveFileName(self, "Export to CSV", "", "CSV Files (*.csv)")
        
        if filename:
            try:
                with open(filename, 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    # Write headers
                    writer.writerow(['ID', 'Name', 'Category', 'Year', 'Status'])
                    # Write data
                    writer.writerows(records)
                self.statusBar().showMessage(f"Data exported to {filename}", 5000)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export data: {str(e)}")
    
    def closeEvent(self, event):
        self.conn.close()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EnhancedDatabaseApp()
    window.show()
    sys.exit(app.exec_())