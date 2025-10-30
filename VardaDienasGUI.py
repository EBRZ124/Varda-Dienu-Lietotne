from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QGridLayout, QVBoxLayout, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import datetime
import dati 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Vārda Dienas")
        self.resize(740, 580)

        self.container = QWidget()
        self.setCentralWidget(self.container)

        self.layout = QVBoxLayout(self.container)

        self.home_page = QWidget()
        self.home_layout = QGridLayout(self.home_page)
        self.layout.addWidget(self.home_page, alignment=Qt.AlignTop)

        self.dienu_kastes()
    
    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
    
    def dienu_kastes(self):
        self.clear_layout(self.home_layout)

        title = QLabel("Šodienas vārda dienas")
        title.setFont(QFont("Comfortaa", 24, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: black; background-color: #E6E6E6;")
        self.home_layout.addWidget(title, 0, 1, 1, 3)     

        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        yesterday = today - datetime.timedelta(days=1)

        key_today = (today.month, today.day)
        key_tomorrow = (tomorrow.month, tomorrow.day)
        key_yesterday = (yesterday.month, yesterday.day)

        formatted_today = today.strftime("%B %d, %Y")
        formatted_tomorrow = tomorrow.strftime("%B %d, %Y")
        formatted_yesterday = yesterday.strftime("%B %d, %Y")

        self.add_day_box(1, 0, key_yesterday, formatted_yesterday, font_size=12)

        self.add_day_box(1, 1, key_today, formatted_today, font_size=16)

        self.add_day_box(1, 2, key_tomorrow, formatted_tomorrow, font_size=12)
    
    def add_day_box(self, row, col, key, date_text, font_size=12):
        if key in dati.datumi_vardi:
            vardi_saralsts = dati.datumi_vardi[key]["vārdi"]

            frame = QFrame()
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setStyleSheet("background-color: white;")
            frame_layout = QVBoxLayout(frame)
            frame_layout.setContentsMargins(20, 20, 20, 20)
            frame_layout.setSpacing(5)

            date_label = QLabel(date_text)
            date_label.setFont(QFont("Comfortaa", font_size, QFont.Bold))
            date_label.setAlignment(Qt.AlignCenter)
            frame_layout.addWidget(date_label)

            for vards in vardi_saralsts:
                name_label = QLabel(vards)
                name_label.setFont(QFont("Comfortaa", font_size))
                name_label.setAlignment(Qt.AlignCenter)
                frame_layout.addWidget(name_label)
            
            self.home_layout.addWidget(frame, row, col)
        
        else:
            empty_label = QLabel("Šodien (kaut kādā veidā) nevienam nav vārda dienas.")
            empty_label.setFont(QFont("Comfortaa", font_size))
            empty_label.setAlignment(Qt.AlignCenter)
            empty_label.setStyleSheet("background-color: white; color: black;")
            self.home_layout.addWidget(empty_label, row, col)


if __name__ == "__main__":
    app = QApplication([])
    with open("/Users/evaldsberzins/Desktop/PYTHON/VardaDienas/style.qss", "r") as f:
        app.setStyleSheet(f.read())
    window = MainWindow()
    window.show()
    app.exec()
