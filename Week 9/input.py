import sys
from PyQt5.QtWidgets import (
    QApplication, QDialog, QInputDialog, QVBoxLayout,
    QLabel, QPushButton, QGroupBox, QGridLayout
)
from PyQt5.QtGui import QFont

class DataInputApp(QDialog):
    def __init__(self):
        super().__init__()
        self.configure_window()
        self.create_widgets()
        self.arrange_layout()
        self.connect_events()

    def configure_window(self):
        self.setWindowTitle('Data Input Application')
        self.resize(450, 250)
        
    def create_widgets(self):
        # Font configurations
        self.standard_font = QFont("Segoe UI", 10)
        self.header_font = QFont("Segoe UI", 12, QFont.Bold)
        
        # Main title
        self.title = QLabel("Input Data Anda")
        self.title.setFont(self.header_font)
        
        # Input widgets
        self.language_label = QLabel("Choose from list:")
        self.language_display = QLabel("Not selected")
        self.language_button = QPushButton("Select")
        
        self.name_label = QLabel("Get name:")
        self.name_display = QLabel("No name entered")
        self.name_button = QPushButton("Enter")
        
        self.number_label = QLabel("Enter an integer:")
        self.number_display = QLabel("No number entered")
        self.number_button = QPushButton("Input")
        
        # Apply fonts to all widgets
        for widget in [self.language_label, self.language_display, self.name_label, 
                      self.name_display, self.number_label, self.number_display]:
            widget.setFont(self.standard_font)
            
    def arrange_layout(self):
        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        main_layout.addWidget(self.title)
        
        # Input group box
        input_group = QGroupBox("Input Section")
        grid = QGridLayout()
        grid.setHorizontalSpacing(15)
        grid.setVerticalSpacing(12)
        
        # Add widgets to grid
        grid.addWidget(self.language_label, 0, 0)
        grid.addWidget(self.language_display, 0, 1)
        grid.addWidget(self.language_button, 0, 2)
        
        grid.addWidget(self.name_label, 1, 0)
        grid.addWidget(self.name_display, 1, 1)
        grid.addWidget(self.name_button, 1, 2)
        
        grid.addWidget(self.number_label, 2, 0)
        grid.addWidget(self.number_display, 2, 1)
        grid.addWidget(self.number_button, 2, 2)
        
        input_group.setLayout(grid)
        main_layout.addWidget(input_group)
        self.setLayout(main_layout)
        
    def connect_events(self):
        self.language_button.clicked.connect(self.select_language)
        self.name_button.clicked.connect(self.enter_name)
        self.number_button.clicked.connect(self.input_number)
        
    def select_language(self):
        options = ("C++", "JavaScript", "Python")
        choice, confirmed = QInputDialog.getItem(
            self, "Language Selection", "Available languages:", 
            options, 0, False
        )
        if confirmed and choice:
            self.language_display.setText(choice)
            
    def enter_name(self):
        name, confirmed = QInputDialog.getText(
            self, "Name Entry", "Please enter your name:"
        )
        if confirmed and name:
            self.name_display.setText(name)
            
    def input_number(self):
        num, confirmed = QInputDialog.getInt(
            self, "Number Input", "Enter any whole number:"
        )
        if confirmed:
            self.number_display.setText(str(num))

if __name__ == "__main__":
    application = QApplication(sys.argv)
    window = DataInputApp()
    window.show()
    sys.exit(application.exec_())