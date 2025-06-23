import sys
import sqlite3
import pandas as pd
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem

# Ganti ini dengan nama dan ID kamu
STUDENT_NAME = "Lalu Restu Bagus Anugrah"
STUDENT_ID = "F1D022059"

class TaskManager(QtWidgets.QMainWindow):
    def __init__(self):
        super(TaskManager, self).__init__()
        uic.loadUi("FInalProject_F1D022059/task_manager.ui", self)


        self.initUI()
        self.createDB()
        self.loadData()

    def initUI(self):
        self.statusbar.showMessage(f"{STUDENT_NAME} | ID: {STUDENT_ID}")

        self.addButton.clicked.connect(self.addTask)
        self.actionExport_CSV.triggered.connect(self.exportCSV)
        self.actionExit.triggered.connect(self.close)
        self.actionAbout.triggered.connect(self.showAbout)

        self.taskTable.setColumnCount(5)
        self.taskTable.setHorizontalHeaderLabels(["Judul", "Kategori", "Tanggal", "Status", "Catatan"])

    def createDB(self):
        self.conn = sqlite3.connect("tasks.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                category TEXT,
                date TEXT,
                status TEXT,
                notes TEXT
            )
        """)
        self.conn.commit()

    def loadData(self):
        self.taskTable.setRowCount(0)
        self.cursor.execute("SELECT title, category, date, status, notes FROM tasks")
        for row_idx, row_data in enumerate(self.cursor.fetchall()):
            self.taskTable.insertRow(row_idx)
            for col_idx, col_data in enumerate(row_data):
                self.taskTable.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    def addTask(self):
        title = self.titleEdit.text()
        category = self.categoryEdit.text()
        date = self.dateEdit.date().toString("yyyy-MM-dd")
        status = self.statusCombo.currentText()
        notes = ""

        if not title or not category:
            QMessageBox.warning(self, "Input Error", "Judul dan Kategori harus diisi.")
            return

        self.cursor.execute("INSERT INTO tasks (title, category, date, status, notes) VALUES (?, ?, ?, ?, ?)",
                            (title, category, date, status, notes))
        self.conn.commit()

        self.titleEdit.clear()
        self.categoryEdit.clear()
        self.loadData()

    def exportCSV(self):
        path, _ = QFileDialog.getSaveFileName(self, "Simpan sebagai", "", "CSV Files (*.csv)")
        if path:
            self.cursor.execute("SELECT title, category, date, status, notes FROM tasks")
            data = self.cursor.fetchall()
            df = pd.DataFrame(data, columns=["Judul", "Kategori", "Tanggal", "Status", "Catatan"])
            df.to_csv(path, index=False)
            QMessageBox.information(self, "Sukses", "Data berhasil diekspor ke CSV!")

    def showAbout(self):
        QMessageBox.information(self, "Tentang", "Task Manager PyQt5\nDibuat oleh Lalu Restu Bagus Anugrah\nNIM: F1D022059")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TaskManager()
    window.show()
    sys.exit(app.exec_())
