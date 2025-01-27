from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
from dul import *

app = QtWidgets.QApplication([])
win = uic.loadUi("Blyda.ui")
Gr = Menu()
print("Всего блюд:", len(Gr.menu_dict)) 

def updateTable():
    win.tableWidget.setRowCount(len(Gr.menu_dict))
    row = 0
    for dish in Gr.menu_dict.values():
        win.tableWidget.setItem(row, 0, QTableWidgetItem(dish.name))
        win.tableWidget.setItem(row, 1, QTableWidgetItem(dish.category))
        win.tableWidget.setItem(row, 2, QTableWidgetItem(str(dish.price)))
        win.tableWidget.setItem(row, 3, QTableWidgetItem(str(dish.weight)))

        for col in range(win.tableWidget.columnCount()):
            win.tableWidget.item(row, col).setTextAlignment(Qt.AlignCenter)
        row += 1

def btnLoadTable():
    updateTable()

def btnAppendTable():
    str = win.lineEdit.text()
    Gr.appendDish(str)
    updateTable()  
    win.lineEdit.clear()  
    

def btnDeleteTable():
    selected_row = win.tableWidget.currentRow()
    if selected_row >= 0:
        selected_name = win.tableWidget.item(selected_row, 0).text()
        Gr.deleteDish(selected_name)
        updateTable()

def btnUpdateTable():
    selected_row = win.tableWidget.currentRow()
    if selected_row >= 0:
        selected_name = win.tableWidget.item(selected_row, 0).text()
        new_name = win.lineEdit_2.text() 
        new_category = win.lineEdit_3.text()  
        new_price = win.lineEdit_4.text()  
        new_weight = win.lineEdit_5.text()  
        Gr.updateDish(selected_name, new_name, new_category, new_price, new_weight)
        updateTable()

win.pushButton_5.clicked.connect(btnUpdateTable)


win.pushButton.clicked.connect(btnLoadTable)
win.pushButton_3.clicked.connect(btnAppendTable)
win.pushButton_4.clicked.connect(btnDeleteTable)



win.show()
sys.exit(app.exec())


"# Bludo" 
