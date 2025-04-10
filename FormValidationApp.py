from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QComboBox, QPushButton, QMessageBox, QFormLayout,
    QFrame, QShortcut, QTextEdit
)
from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtGui import QRegExpValidator, QFont, QKeySequence
import sys


class FormValidationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Validation Application")
        self.setGeometry(100, 100, 450, 650)

        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        self.create_header()
        self.layout.addSpacing(10)

        form_frame = QFrame()
        form_frame.setFrameShape(QFrame.StyledPanel)
        self.form_layout = QFormLayout()
        self.form_layout.setVerticalSpacing(15)
        self.form_layout.setHorizontalSpacing(20)
        form_frame.setLayout(self.form_layout)
        self.layout.addWidget(form_frame)

        self.create_form_fields()
        self.layout.addSpacing(15)
        self.create_buttons()

        close_shortcut = QShortcut(QKeySequence("Q"), self)
        close_shortcut.activated.connect(self.close)

    def create_header(self):
        header = QWidget()
        header_layout = QVBoxLayout()
        header.setLayout(header_layout)

        title = QLabel("Form Validation Application")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #2c3e50;")
        header_layout.addWidget(title)

        student_info = QLabel("Nama: Lalu Restu Bagus Anugrah | NIM: F1D022059")
        student_info.setAlignment(Qt.AlignCenter)
        student_info.setStyleSheet("font-size: 14px; color: #7f8c8d;")
        header_layout.addWidget(student_info)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        header_layout.addWidget(separator)

        required_info = QLabel("* Required fields")
        required_info.setAlignment(Qt.AlignRight)
        required_info.setStyleSheet("font-size: 12px; color: #e74c3c;")
        header_layout.addWidget(required_info)

        self.layout.addWidget(header)

    def create_form_fields(self):
        field_font = QFont()
        field_font.setPointSize(12)

        self.name_field = QLineEdit()
        self.name_field.setPlaceholderText("Enter your full name")
        self.name_field.setFont(field_font)
        self.form_layout.addRow(QLabel("Name*:"), self.name_field)

        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("example@domain.com")
        self.email_field.setFont(field_font)
        email_regex = QRegExp(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        self.email_field.setValidator(QRegExpValidator(email_regex))
        self.form_layout.addRow(QLabel("Email*:"), self.email_field)

        self.age_field = QLineEdit()
        self.age_field.setPlaceholderText("Enter your age (1-120)")
        self.age_field.setFont(field_font)
        age_regex = QRegExp(r'^[0-9]{1,3}$')
        self.age_field.setValidator(QRegExpValidator(age_regex))
        self.form_layout.addRow(QLabel("Age*:"), self.age_field)

        self.phone_field = QLineEdit()
        self.phone_field.setInputMask("+62 999 9999 9999")
        self.phone_field.setPlaceholderText("+62 812 3456 7890")
        self.phone_field.setFont(field_font)
        self.form_layout.addRow(QLabel("Phone*:"), self.phone_field)

        self.address_field = QTextEdit()
        self.address_field.setFont(field_font)
        self.address_field.setPlaceholderText("Enter your complete address")
        self.address_field.setFixedHeight(80)
        self.form_layout.addRow(QLabel("Address*:"), self.address_field)

        self.gender_field = QComboBox()
        self.gender_field.setFont(field_font)
        self.gender_field.addItems(["Select Gender", "Male", "Female", "Other"])
        self.form_layout.addRow(QLabel("Gender*:"), self.gender_field)

        self.education_field = QComboBox()
        self.education_field.setFont(field_font)
        self.education_field.addItems(["Select Education", "High School", "Bachelor", "Master", "PhD"])
        self.form_layout.addRow(QLabel("Education*:"), self.education_field)

    def create_buttons(self):
        button_container = QWidget()
        button_layout = QVBoxLayout()
        button_container.setLayout(button_layout)

        self.save_button = QPushButton("Submit Form")
        self.save_button.clicked.connect(self.validate_form)
        button_layout.addWidget(self.save_button, 0, Qt.AlignCenter)

        self.clear_button = QPushButton("Clear Form")
        self.clear_button.clicked.connect(self.clear_fields)
        button_layout.addWidget(self.clear_button, 0, Qt.AlignCenter)

        shortcut_info = QLabel("Press 'Q' to close the application")
        shortcut_info.setAlignment(Qt.AlignCenter)
        shortcut_info.setStyleSheet("color: #666; font-size: 12px;")
        button_layout.addWidget(shortcut_info)

        self.layout.addWidget(button_container)

    def validate_form(self):
        errors = []
        error_style = "border: 1px solid #e74c3c;"
        default_style = "border: 1px solid #ccc;"

        # Reset styles
        for field in [self.name_field, self.email_field, self.age_field, self.phone_field]:
            field.setStyleSheet(default_style)

        self.address_field.setStyleSheet(default_style)
        self.gender_field.setStyleSheet(default_style)
        self.education_field.setStyleSheet(default_style)

        if not self.name_field.text().strip():
            errors.append("• Name is required")
            self.name_field.setStyleSheet(error_style)

        if not self.email_field.hasAcceptableInput():
            errors.append("• Invalid email format")
            self.email_field.setStyleSheet(error_style)

        if not self.age_field.text().strip():
            errors.append("• Age is required")
            self.age_field.setStyleSheet(error_style)
        elif not self.age_field.hasAcceptableInput() or not (1 <= int(self.age_field.text()) <= 120):
            errors.append("• Age must be between 1 and 120")
            self.age_field.setStyleSheet(error_style)

        if not self.phone_field.hasAcceptableInput():
            errors.append("• Phone number must be complete")
            self.phone_field.setStyleSheet(error_style)

        if not self.address_field.toPlainText().strip():
            errors.append("• Address is required")
            self.address_field.setStyleSheet(error_style)

        if self.gender_field.currentIndex() == 0:
            errors.append("• Gender must be selected")
            self.gender_field.setStyleSheet(error_style)

        if self.education_field.currentIndex() == 0:
            errors.append("• Education must be selected")
            self.education_field.setStyleSheet(error_style)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Validation Error")

        if len(errors) == 1:
            msg.setText(errors[0])
        elif len(errors) > 1:
            msg.setText("All fields are required.")
        else:
            QMessageBox.information(self, "Success", "Form submitted successfully!")
            self.clear_fields()
            return

        msg.exec_()

    def clear_fields(self):
        self.name_field.clear()
        self.email_field.clear()
        self.age_field.clear()
        self.phone_field.clear()
        self.address_field.clear()
        self.gender_field.setCurrentIndex(0)
        self.education_field.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
