# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1170, 792)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1181, 731))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("cute-sneakers-1609793057.jpg"))
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 30, 1121, 571))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushexe = QtWidgets.QPushButton(self.tab)
        self.pushexe.setGeometry(QtCore.QRect(180, 50, 71, 31))
        self.pushexe.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 127);\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: lightgreen;\n"
"}")
        self.pushexe.setText("")
        self.pushexe.setObjectName("pushexe")
        self.lable_inputkho = QtWidgets.QLabel(self.tab)
        self.lable_inputkho.setGeometry(QtCore.QRect(20, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lable_inputkho.setFont(font)
        self.lable_inputkho.setObjectName("lable_inputkho")
        self.pushview_all = QtWidgets.QPushButton(self.tab)
        self.pushview_all.setGeometry(QtCore.QRect(980, 0, 131, 51))
        self.pushview_all.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 127);\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}")
        self.pushview_all.setObjectName("pushview_all")
        self.table_kho = QtWidgets.QTableWidget(self.tab)
        self.table_kho.setGeometry(QtCore.QRect(20, 130, 1091, 391))
        self.table_kho.setObjectName("table_kho")
        self.table_kho.setColumnCount(5)
        self.table_kho.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_kho.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kho.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kho.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kho.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_kho.setHorizontalHeaderItem(4, item)
        self.label_kho_head = QtWidgets.QLabel(self.tab)
        self.label_kho_head.setGeometry(QtCore.QRect(340, 90, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_kho_head.setFont(font)
        self.label_kho_head.setObjectName("label_kho_head")
        self.lineEdit_kho = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_kho.setGeometry(QtCore.QRect(30, 50, 131, 31))
        self.lineEdit_kho.setObjectName("lineEdit_kho")
        self.but_edit_upda = QtWidgets.QPushButton(self.tab)
        self.but_edit_upda.setGeometry(QtCore.QRect(630, 60, 93, 31))
        self.but_edit_upda.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 127);\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}")
        self.but_edit_upda.setObjectName("but_edit_upda")
        self.but_edit_dele = QtWidgets.QPushButton(self.tab)
        self.but_edit_dele.setGeometry(QtCore.QRect(830, 60, 101, 31))
        self.but_edit_dele.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 127);\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:hover {\n"
"   background-color: lightgreen;\n"
"}")
        self.but_edit_dele.setObjectName("but_edit_dele")
        self.lineEdit_update = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_update.setGeometry(QtCore.QRect(600, 10, 161, 31))
        self.lineEdit_update.setObjectName("lineEdit_update")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.table_order = QtWidgets.QTableWidget(self.tab_3)
        self.table_order.setGeometry(QtCore.QRect(40, 70, 1031, 431))
        self.table_order.setObjectName("table_order")
        self.table_order.setColumnCount(10)
        self.table_order.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_order.setHorizontalHeaderItem(9, item)
        self.label_order_head = QtWidgets.QLabel(self.tab_3)
        self.label_order_head.setGeometry(QtCore.QRect(480, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_order_head.setFont(font)
        self.label_order_head.setObjectName("label_order_head")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.but_edit_add = QtWidgets.QPushButton(self.tab_2)
        self.but_edit_add.setGeometry(QtCore.QRect(280, 140, 141, 41))
        self.but_edit_add.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 127);\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}")
        self.but_edit_add.setObjectName("but_edit_add")
        self.lineEdit_price = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_price.setGeometry(QtCore.QRect(40, 50, 121, 31))
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.lineEdit_amount = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_amount.setGeometry(QtCore.QRect(40, 140, 121, 31))
        self.lineEdit_amount.setObjectName("lineEdit_amount")
        self.lineEdit_name = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_name.setGeometry(QtCore.QRect(40, 220, 121, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_descri = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_descri.setGeometry(QtCore.QRect(40, 300, 201, 31))
        self.lineEdit_descri.setObjectName("lineEdit_descri")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(70, 20, 55, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(70, 110, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(70, 200, 55, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(60, 270, 111, 20))
        self.label_6.setObjectName("label_6")
        self.label_edit = QtWidgets.QLabel(self.tab_2)
        self.label_edit.setGeometry(QtCore.QRect(40, 390, 361, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_edit.setFont(font)
        self.label_edit.setText("")
        self.label_edit.setObjectName("label_edit")
        self.table_chat = QtWidgets.QTableWidget(self.tab_2)
        self.table_chat.setGeometry(QtCore.QRect(550, 40, 531, 331))
        self.table_chat.setObjectName("table_chat")
        self.table_chat.setColumnCount(4)
        self.table_chat.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_chat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_chat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_chat.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_chat.setHorizontalHeaderItem(3, item)
        self.but_chats = QtWidgets.QPushButton(self.tab_2)
        self.but_chats.setGeometry(QtCore.QRect(750, 430, 171, 51))
        self.but_chats.setStyleSheet("QPushButton {\n"
"    background-color: rgb(170, 170, 127);\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}")
        self.but_chats.setObjectName("but_chats")
        self.tabWidget.addTab(self.tab_2, "")
        self.but_viewpro = QtWidgets.QPushButton(self.centralwidget)
        self.but_viewpro.setGeometry(QtCore.QRect(60, 620, 171, 61))
        self.but_viewpro.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}")
        self.but_viewpro.setObjectName("but_viewpro")
        self.but_editdata = QtWidgets.QPushButton(self.centralwidget)
        self.but_editdata.setGeometry(QtCore.QRect(940, 620, 161, 61))
        self.but_editdata.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}")
        self.but_editdata.setObjectName("but_editdata")
        self.but_order = QtWidgets.QPushButton(self.centralwidget)
        self.but_order.setGeometry(QtCore.QRect(500, 620, 161, 61))
        self.but_order.setStyleSheet("QPushButton {\n"
"    background-color: #2B5DD1;\n"
"    color: #FFFFFF;\n"
"    border-style: outset;\n"
"    padding: 2px;\n"
"    font: bold 20px;\n"
"    border-width: 6px;\n"
"    border-radius: 10px;\n"
"    border-color: #2752B8;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: lightgreen;\n"
"}")
        self.but_order.setObjectName("but_order")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1170, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lable_inputkho.setText(_translate("MainWindow", "INPUT PRODUCT ID"))
        self.pushview_all.setText(_translate("MainWindow", "View all"))
        item = self.table_kho.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product ID"))
        item = self.table_kho.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.table_kho.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.table_kho.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Name"))
        item = self.table_kho.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Description"))
        self.label_kho_head.setText(_translate("MainWindow", "PRODUCTS INFORMATION"))
        self.but_edit_upda.setText(_translate("MainWindow", "Update"))
        self.but_edit_dele.setText(_translate("MainWindow", "Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Products"))
        item = self.table_order.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Order ID"))
        item = self.table_order.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Customer Name"))
        item = self.table_order.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Address"))
        item = self.table_order.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Order State"))
        item = self.table_order.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Order Date"))
        item = self.table_order.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Delivery Date"))
        item = self.table_order.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.table_order.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Amount"))
        item = self.table_order.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Colour"))
        item = self.table_order.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Size"))
        self.label_order_head.setText(_translate("MainWindow", "LATEST ORDERS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Orders"))
        self.but_edit_add.setText(_translate("MainWindow", "Add"))
        self.label_3.setText(_translate("MainWindow", "Price"))
        self.label_4.setText(_translate("MainWindow", "Amount"))
        self.label_5.setText(_translate("MainWindow", "Name"))
        self.label_6.setText(_translate("MainWindow", "Description"))
        item = self.table_chat.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product_name"))
        item = self.table_chat.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "User_name"))
        item = self.table_chat.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Message"))
        item = self.table_chat.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Star"))
        self.but_chats.setText(_translate("MainWindow", "Show feedback"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Add product - Feedbacks"))
        self.but_viewpro.setText(_translate("MainWindow", "Products"))
        self.but_editdata.setText(_translate("MainWindow", "Edit data"))
        self.but_order.setText(_translate("MainWindow", "Orders"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())