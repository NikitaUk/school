from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QComboBox, QGridLayout, QWidget
import sys
from data import add_data

class MainWindow(QMainWindow):
    def exit_clicked(self):
        app.exit()
    def add_clicked(self):
        fio = self.lineEdit_addFio.text()
        chclass = self.comboBox_changeClass.currentText()
        index = self.comboBox_changeIndex.currentText()
        add_data(fio, chclass, index)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Добавить ученика")
        self.setFixedSize(400, 150)
        #widgets
        self.lbl_title = QLabel("<center>Добавить ученика</center>")
        self.lbl_addFio = QLabel("Добавить ФИО")
        self.lineEdit_addFio = QLineEdit()
        self.lbl_changeClass = QLabel("Выбрать класс")
        self.comboBox_changeClass = QComboBox()
        self.lbl_changeIndex = QLabel("Выбрать индекс")
        self.comboBox_changeIndex = QComboBox()
        self.btn_exit = QPushButton("Выход")
        self.btn_add = QPushButton("Добавить")
        self.btn_exit.clicked.connect(self.exit_clicked)
        self.btn_add.clicked.connect(self.add_clicked)
        #combobox
        self.comboBox_changeClass.addItem("1")
        self.comboBox_changeClass.addItem("2")
        self.comboBox_changeClass.addItem("3")
        self.comboBox_changeClass.addItem("4")
        self.comboBox_changeClass.addItem("5")
        self.comboBox_changeClass.addItem("6")
        self.comboBox_changeClass.addItem("7")
        self.comboBox_changeClass.addItem("8")
        self.comboBox_changeClass.addItem("9")
        self.comboBox_changeClass.addItem("10")
        self.comboBox_changeClass.addItem("11")
        self.comboBox_changeIndex.addItem("А")
        self.comboBox_changeIndex.addItem("Б")
        self.comboBox_changeIndex.addItem("В")
        self.comboBox_changeIndex.addItem("Г")
        self.comboBox_changeIndex.addItem("Д")
        self.comboBox_changeIndex.addItem("Е")
        #layout
        grid = QGridLayout()
        grid.addWidget(self.lbl_title, 0, 0, 1, 0)
        grid.addWidget(self.lbl_addFio, 1, 0)
        grid.addWidget(self.lineEdit_addFio, 1, 1)
        grid.addWidget(self.lbl_changeClass, 2, 0)
        grid.addWidget(self.comboBox_changeClass, 2, 1)
        grid.addWidget(self.lbl_changeIndex, 3, 0)
        grid.addWidget(self.comboBox_changeIndex, 3, 1)
        grid.addWidget(self.btn_exit, 4, 0)
        grid.addWidget(self.btn_add, 4, 1)
        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)
        with open("style.css") as style:
            self.setStyleSheet(style.read())

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
