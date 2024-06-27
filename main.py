from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
from dul import *

app = QtWidgets.QApplication([])
win = uic.loadUi("Blyda.ui")
Gr = Menu()
print("Всего блюд:", len(Gr.menu_dict))  # Выводим количество блюд

def updateTable():
    win.tableWidget.setRowCount(len(Gr.menu_dict))  # Устанавливаем количество строк в таблице равным количеству блюд
    row = 0
    for dish in Gr.menu_dict.values():
        win.tableWidget.setItem(row, 0, QTableWidgetItem(dish.name))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(dish.category))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(str(dish.price)))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(str(dish.weight)))
       
        for col in range(win.tableWidget.columnCount()):
            win.tableWidget.item(row, col).setTextAlignment(Qt.AlignCenter)
        row += 1

    win.tableWidget.resizeRowsToContents()
    win.tableWidget.resizeColumnsToContents()
    win.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

def btnLoadTable():
    updateTable()

win.pushButton.clicked.connect(btnLoadTable)
win.show()
sys.exit(app.exec())




"# Menu" 
"# mn" 
