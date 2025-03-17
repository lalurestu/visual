import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton, QPushButton, QLabel, QButtonGroup, QComboBox, QMessageBox
from PyQt5.QtCore import Qt

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle('User Registration Form')
        self.setGeometry(100, 100, 600, 350)

        # Main vertical layout
        main_layout = QVBoxLayout()

        # Identitas section (vertical box layout)
        identitas_layout = QVBoxLayout()
        identitas_layout.addWidget(QLabel('Identitas'))
        identitas_layout.addWidget(QLabel('Nama\t: Lalu Restu Bagus Anugrah'))
        identitas_layout.addWidget(QLabel('Nim\t: F1D022059'))
        identitas_layout.addWidget(QLabel('Kelas\t: C'))
        main_layout.addLayout(identitas_layout)

        # Navigation section (horizontal box layout)
        navigation_layout = QHBoxLayout()
        home_button = QPushButton('Home')
        about_button = QPushButton('About')
        contact_button = QPushButton('Contact')
        navigation_layout.addWidget(home_button)
        navigation_layout.addWidget(about_button)
        navigation_layout.addWidget(contact_button)
        main_layout.addLayout(navigation_layout)

        # Connect navigation buttons to actions
        home_button.clicked.connect(self.show_home_message)
        about_button.clicked.connect(self.show_about_message)
        contact_button.clicked.connect(self.show_contact_message)

        # User Registration section (form layout)
        self.form_layout = QFormLayout()
        self.full_name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.form_layout.addRow('Full Name:', self.full_name_input)
        self.form_layout.addRow('Email:', self.email_input)
        self.form_layout.addRow('Phone:', self.phone_input)

        # Gender radio buttons
        self.gender_group = QButtonGroup()
        gender_layout = QHBoxLayout()
        male_radio = QRadioButton('Male')
        female_radio = QRadioButton('Female')
        self.gender_group.addButton(male_radio)
        self.gender_group.addButton(female_radio)
        gender_layout.addWidget(male_radio)
        gender_layout.addWidget(female_radio)
        self.form_layout.addRow('Gender:', gender_layout)

        # Country combo box
        self.country_combo = QComboBox()
        self.country_combo.addItems(['Indonesia', 'Singapura', 'United Kingdom', 'Australia', 'India'])
        self.form_layout.addRow('Country:', self.country_combo)

        main_layout.addLayout(self.form_layout)

        # Actions section (horizontal box layout)
        actions_layout = QHBoxLayout()
        submit_button = QPushButton('Submit')
        cancel_button = QPushButton('Cancel')
        actions_layout.addWidget(submit_button)
        actions_layout.addWidget(cancel_button)
        main_layout.addLayout(actions_layout)

        # Connect actions to methods
        submit_button.clicked.connect(self.submit_form)
        cancel_button.clicked.connect(self.clear_form)

        # Set main layout
        self.setLayout(main_layout)

    def show_home_message(self):
        QMessageBox.information(self, 'Home', 'Welcome to the Home page!')

    def show_about_message(self):
        QMessageBox.information(self, 'About', 'This is a simple registration form created using PyQt5.')

    def show_contact_message(self):
        QMessageBox.information(self, 'Contact', 'You can contact us at contact@lalurestubagus@gmail.com.')

    def submit_form(self):
        full_name = self.full_name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        gender = 'Male' if self.gender_group.checkedButton().text() == 'Male' else 'Female'
        country = self.country_combo.currentText()

        if not full_name or not email or not phone:
            QMessageBox.warning(self, 'Input Error', 'Please fill in all fields.')
            return

        if '@' not in email or '.' not in email:
            QMessageBox.warning(self, 'Input Error', 'Please enter a valid email address.')
            return

        if not phone.isdigit():
            QMessageBox.warning(self, 'Input Error', 'Please enter a valid phone number.')
            return

        confirmation_message = f"Name: {full_name}\nEmail: {email}\nPhone: {phone}\nGender: {gender}\nCountry: {country}"
        reply = QMessageBox.question(self, 'Confirm Submission', f"Are you sure you want to submit the following information?\n\n{confirmation_message}", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            QMessageBox.information(self, 'Success', 'Your registration has been submitted successfully!')
            self.clear_form()

    def clear_form(self):
        self.full_name_input.clear()
        self.email_input.clear()
        self.phone_input.clear()
        self.gender_group.setExclusive(False)
        for button in self.gender_group.buttons():
            button.setChecked(False)
        self.gender_group.setExclusive(True)
        self.country_combo.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegistrationForm()
    form.show()
    sys.exit(app.exec_())