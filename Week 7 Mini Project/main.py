import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt, QTime, QDate
from lab_scheduler_ui import Ui_MainWindow

class LabSchedulerApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Initialize data
        self.schedule = {
            "Lab 1": {},
            "Lab 2": {},
            "Lab 3": {}
        }
        
        self.day_names = {
            0: "Senin",
            1: "Selasa",
            2: "Rabu",
            3: "Kamis",
            4: "Jumat"
        }
        
        # Set initial time
        self.start_time.setTime(QTime(7, 0))
        self.end_time.setTime(QTime(10, 0))
        self.date_input.setDate(QDate.currentDate())
        
        # Connect signals
        self.date_input.dateChanged.connect(self.update_day_from_date)
        self.book_button.clicked.connect(self.book_lab)
        
        # Initial update
        self.update_day_from_date()
    
    def update_day_from_date(self):
        """Update day based on selected date"""
        date = self.date_input.date()
        day_of_week = date.dayOfWeek() - 1  # Qt: 1=Monday, 7=Sunday
        
        if 0 <= day_of_week <= 4:
            self.day_label.setText(self.day_names[day_of_week])
        else:
            self.day_label.setText("Hari Libur")
            self.day_label.setStyleSheet("color: red; font-weight: bold;")
    
    def book_lab(self):
        name = self.name_input.text()
        lab = self.lab_combo.currentText()
        date = self.date_input.date().toString("dd/MM/yyyy")
        day = self.day_label.text()
        
        # Validate weekday
        if day not in self.day_names.values():
            QMessageBox.warning(self, "Error", "Hanya bisa booking hari Senin-Jumat!")
            return
        
        # Get booking time
        start = self.start_time.time().toString("HH:mm")
        end = self.end_time.time().toString("HH:mm")
        
        # Validation
        if not all([name, date, day]):
            QMessageBox.warning(self, "Error", "Harap lengkapi semua field!")
            return
            
        if self.start_time.time() >= self.end_time.time():
            QMessageBox.warning(self, "Error", "Waktu selesai harus setelah waktu mulai!")
            return
        
        # Check lab availability
        if self.check_availability(lab, date, day, start, end):
            time_slot = f"{start} - {end}"
            if lab not in self.schedule:
                self.schedule[lab] = {}
            if date not in self.schedule[lab]:
                self.schedule[lab][date] = {}
            if day not in self.schedule[lab][date]:
                self.schedule[lab][date][day] = []
                
            self.schedule[lab][date][day].append((time_slot, name))
            self.update_schedule_table()
            QMessageBox.information(self, "Success", 
                f"✅ Booking berhasil!\nTanggal: {date}\nLab: {lab}\nHari: {day}\nWaktu: {time_slot}")
        else:
            QMessageBox.warning(self, "Error", "⛔ Lab sudah dipesan pada waktu tersebut!")
    
    def check_availability(self, lab, date, day, start, end):
        """Check if lab is available at requested time"""
        if lab not in self.schedule or date not in self.schedule[lab] or day not in self.schedule[lab][date]:
            return True
            
        new_start = QTime.fromString(start, "HH:mm")
        new_end = QTime.fromString(end, "HH:mm")
        
        for booking in self.schedule[lab][date][day]:
            booked_time = booking[0].split(" - ")
            booked_start = QTime.fromString(booked_time[0], "HH:mm")
            booked_end = QTime.fromString(booked_time[1], "HH:mm")
            
            # Check time overlap
            if (new_start < booked_end) and (new_end > booked_start):
                return False
                
        return True
    
    def update_schedule_table(self):
        self.schedule_table.setRowCount(0)
        row = 0
        
        for lab, dates in self.schedule.items():
            for date, days in dates.items():
                for day, bookings in days.items():
                    for booking in bookings:
                        self.schedule_table.insertRow(row)
                        self.schedule_table.setItem(row, 0, QTableWidgetItem(date))
                        self.schedule_table.setItem(row, 1, QTableWidgetItem(lab))
                        self.schedule_table.setItem(row, 2, QTableWidgetItem(day))
                        self.schedule_table.setItem(row, 3, QTableWidgetItem(booking[0]))
                        self.schedule_table.setItem(row, 4, QTableWidgetItem(booking[1]))
                        row += 1

if __name__ == "__main__":  
    app = QApplication(sys.argv)
    window = LabSchedulerApp()
    window.show()
    sys.exit(app.exec_())