import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QSlider, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont

class SliderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Set window properties
        self.setWindowTitle("Font Size and Color Adjuster (F1D022059)")
        self.setGeometry(100, 100, 500, 400)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Student information (replace with your actual name and NIM)
        self.name = "Lalu. Restu Bagus Anugrah"
        self.nim = "F1D022059"  # Replace with your actual NIM
        
        # Create info label
        info_label = QLabel(f"Nama: {self.name} | NIM: {self.nim}")
        info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(info_label)
        
        # Create the main label that will be customized
        self.display_label = QLabel(self.nim)
        self.display_label.setAlignment(Qt.AlignCenter)
        self.display_label.setFont(QFont('Arial', 30))  # Initial font size
        self.display_label.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
        layout.addWidget(self.display_label, 1)
        
        # Create sliders
        self.create_font_size_slider(layout)
        self.create_font_color_slider(layout)
        self.create_bg_color_slider(layout)
        
        # Set initial values
        self.font_size_slider.setValue(30)
        self.font_color_slider.setValue(0)
        self.bg_color_slider.setValue(255)
        
    def create_font_size_slider(self, layout):
        # Font Size Slider (20-60pt)
        font_size_layout = QHBoxLayout()
        
        font_size_label = QLabel("Font Size\t\t:")
        font_size_layout.addWidget(font_size_label)
        
        self.font_size_slider = QSlider(Qt.Horizontal)
        self.font_size_slider.setRange(20, 60)
        self.font_size_slider.valueChanged.connect(self.update_font_size)
        font_size_layout.addWidget(self.font_size_slider)
        
        self.font_size_value = QLabel("30")
        font_size_layout.addWidget(self.font_size_value)
        
        layout.addLayout(font_size_layout)
    
    def create_font_color_slider(self, layout):
        # Font Color Slider (0-255 grayscale)
        font_color_layout = QHBoxLayout()
        
        font_color_label = QLabel("Font Color\t:")
        font_color_layout.addWidget(font_color_label)
        
        self.font_color_slider = QSlider(Qt.Horizontal)
        self.font_color_slider.setRange(0, 255)
        self.font_color_slider.valueChanged.connect(self.update_colors)
        font_color_layout.addWidget(self.font_color_slider)
        
        self.font_color_value = QLabel("0")
        font_color_layout.addWidget(self.font_color_value)
        
        layout.addLayout(font_color_layout)
    
    def create_bg_color_slider(self, layout):
        # Background Color Slider (0-255 grayscale)
        bg_color_layout = QHBoxLayout()
        
        bg_color_label = QLabel("Background Color\t:")
        bg_color_layout.addWidget(bg_color_label)
        
        self.bg_color_slider = QSlider(Qt.Horizontal)
        self.bg_color_slider.setRange(0, 255)
        self.bg_color_slider.valueChanged.connect(self.update_colors)
        bg_color_layout.addWidget(self.bg_color_slider)
        
        self.bg_color_value = QLabel("255")
        bg_color_layout.addWidget(self.bg_color_value)
        
        layout.addLayout(bg_color_layout)
    
    def update_font_size(self, value):
        # Update font size
        font = self.display_label.font()
        font.setPointSize(value)
        self.display_label.setFont(font)
        self.font_size_value.setText(str(value))
    
    def update_colors(self):
        # Get current slider values
        font_color = self.font_color_slider.value()
        bg_color = self.bg_color_slider.value()
        
        # Update display values
        self.font_color_value.setText(str(font_color))
        self.bg_color_value.setText(str(bg_color))
        
        # Update label colors
        self.display_label.setStyleSheet(
            f"background-color: rgb({bg_color}, {bg_color}, {bg_color}); "
            f"color: rgb({font_color}, {font_color}, {font_color});"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderApp()
    window.show()
    sys.exit(app.exec_())