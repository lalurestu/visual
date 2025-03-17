import sys
import random
import os
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"  

class MouseCoordinateLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("x: 0, y: 0")
        self.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setBold(True)   
        self.setFont(font)

    def move_randomly(self):
        window_size = self.parent().size()
        label_size = self.size()

        max_x = window_size.width() - label_size.width()
        max_y = window_size.height() - label_size.height()

        new_x = random.randint(0, max_x)
        new_y = random.randint(0, max_y)

        self.move(new_x, new_y)

    def enterEvent(self, event):
        self.move_randomly()
        super().enterEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Task Week3 - (F1D022059 Lalu. Restu Bagus Anugrah)")
        self.setGeometry(100, 100, 800, 600)

        self.label = MouseCoordinateLabel(self)
        self.label.setFixedSize(200, 50)
        self.label.move(300, 250)

        self.setMouseTracking(True)

    def mouseMoveEvent(self, event):
        x = event.x()
        y = event.y()

        self.label.setText(f"x: {x}, y: {y}")

        if self.label.underMouse():
            self.label.move_randomly()

        super().mouseMoveEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())