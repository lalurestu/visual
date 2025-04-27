from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Main vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        # Input form grid layout
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        
        # Name input
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.name_input.setObjectName("name_input")
        self.gridLayout.addWidget(self.name_input, 0, 1, 1, 3)
        
        # Lab selection
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lab_combo = QtWidgets.QComboBox(self.centralwidget)
        self.lab_combo.setObjectName("lab_combo")
        self.lab_combo.addItems(["Lab 1", "Lab 2", "Lab 3"])
        self.gridLayout.addWidget(self.lab_combo, 1, 1, 1, 3)
        
        # Date input
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.date_input = QtWidgets.QDateEdit(self.centralwidget)
        self.date_input.setObjectName("date_input")
        self.date_input.setDisplayFormat("dd/MM/yyyy")
        self.date_input.setCalendarPopup(True)
        self.gridLayout.addWidget(self.date_input, 2, 1, 1, 1)
        
        # Day label
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.day_label = QtWidgets.QLabel(self.centralwidget)
        self.day_label.setObjectName("day_label")
        self.day_label.setStyleSheet("font-weight: bold;")
        self.gridLayout.addWidget(self.day_label, 3, 1, 1, 1)
        
        # Time inputs
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.start_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.start_time.setObjectName("start_time")
        self.start_time.setDisplayFormat("HH:mm")
        self.gridLayout.addWidget(self.start_time, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 2, 1, 1)
        self.end_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.end_time.setObjectName("end_time")
        self.end_time.setDisplayFormat("HH:mm")
        self.gridLayout.addWidget(self.end_time, 4, 3, 1, 1)
        
        # Book button
        self.book_button = QtWidgets.QPushButton(self.centralwidget)
        self.book_button.setObjectName("book_button")
        self.book_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; 
                color: white;
                padding: 8px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.gridLayout.addWidget(self.book_button, 5, 0, 1, 4)
        
        self.verticalLayout.addLayout(self.gridLayout)
        
        # Schedule table
        self.schedule_table = QtWidgets.QTableWidget(self.centralwidget)
        self.schedule_table.setObjectName("schedule_table")
        self.schedule_table.setColumnCount(5)
        self.schedule_table.setHorizontalHeaderLabels(["Tanggal", "Lab", "Hari", "Waktu", "Pemesan"])
        self.schedule_table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                font-size: 12px;
            }
            QHeaderView::section {
                background-color: #f2f2f2;
                padding: 5px;
                border: none;
            }
        """)
        self.verticalLayout.addWidget(self.schedule_table)
        
        # Student info
        self.student_info = QtWidgets.QLabel(self.centralwidget)
        self.student_info.setObjectName("student_info")
        self.student_info.setAlignment(QtCore.Qt.AlignCenter)
        self.student_info.setEnabled(False)
        self.student_info.setStyleSheet("font-style: italic; color: #555;")
        self.verticalLayout.addWidget(self.student_info)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Penjadwalan Booking Lab Komputer"))
        self.label.setText(_translate("MainWindow", "Nama Pemesan:"))
        self.label_2.setText(_translate("MainWindow", "Pilih Lab:"))
        self.label_3.setText(_translate("MainWindow", "Tanggal:"))
        self.label_4.setText(_translate("MainWindow", "Hari:"))
        self.label_5.setText(_translate("MainWindow", "Waktu Mulai:"))
        self.label_6.setText(_translate("MainWindow", "Waktu Selesai:"))
        self.book_button.setText(_translate("MainWindow", "Book Lab"))
        self.student_info.setText(_translate("MainWindow", "NIM: F1D022059 | Nama: Lalu. Restu Bagus Anugrah"))