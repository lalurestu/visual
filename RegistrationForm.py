import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton, QPushButton, QLabel, QButtonGroup, QComboBox

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle('User Registration Form')
        self.setGeometry(100, 100, 400, 300)

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
        navigation_layout.addWidget(QPushButton('Home'))
        navigation_layout.addWidget(QPushButton('About'))
        navigation_layout.addWidget(QPushButton('Contact'))
        main_layout.addLayout(navigation_layout)

        # User Registration section (form layout)
        form_layout = QFormLayout()
        form_layout.addRow('Full Name:', QLineEdit())
        form_layout.addRow('Email:', QLineEdit())
        form_layout.addRow('Phone:', QLineEdit())

        # Gender radio buttons
        gender_layout = QHBoxLayout()
        male_radio = QRadioButton('Male')
        female_radio = QRadioButton('Female')
        gender_layout.addWidget(male_radio)
        gender_layout.addWidget(female_radio)
        form_layout.addRow('Gender:', gender_layout)

        # Country combo box
        country_combo = QComboBox()
        country_combo.addItems(['Indonesia', 'Singapura', 'United Kingdom', 'Australia', 'India'])
        form_layout.addRow('Country:', country_combo)

        main_layout.addLayout(form_layout)

        # Actions section (horizontal box layout)
        actions_layout = QHBoxLayout()
        actions_layout.addWidget(QPushButton('Submit'))
        actions_layout.addWidget(QPushButton('Cancel'))
        main_layout.addLayout(actions_layout)

        # Set main layout
        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = RegistrationForm()
    form.show()
    sys.exit(app.exec_())