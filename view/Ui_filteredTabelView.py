# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fares/Documents/devel/pypointage2/view/filteredTabelView.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilteredTabelView(object):
    def setupUi(self, FilteredTabelView):
        FilteredTabelView.setObjectName("FilteredTabelView")
        FilteredTabelView.resize(440, 425)
        self.verticalLayout = QtWidgets.QVBoxLayout(FilteredTabelView)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hLayout = QtWidgets.QHBoxLayout()
        self.hLayout.setObjectName("hLayout")
        self.lineEdit_filter = QtWidgets.QLineEdit(FilteredTabelView)
        self.lineEdit_filter.setClearButtonEnabled(True)
        self.lineEdit_filter.setObjectName("lineEdit_filter")
        self.hLayout.addWidget(self.lineEdit_filter)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hLayout.addItem(spacerItem)
        self.lineEdit_limit = QtWidgets.QLineEdit(FilteredTabelView)
        self.lineEdit_limit.setInputMask("")
        self.lineEdit_limit.setText("")
        self.lineEdit_limit.setMaxLength(5)
        self.lineEdit_limit.setObjectName("lineEdit_limit")
        self.hLayout.addWidget(self.lineEdit_limit)
        self.label = QtWidgets.QLabel(FilteredTabelView)
        self.label.setObjectName("label")
        self.hLayout.addWidget(self.label)
        self.toolButtonL = QtWidgets.QToolButton(FilteredTabelView)
        self.toolButtonL.setArrowType(QtCore.Qt.LeftArrow)
        self.toolButtonL.setObjectName("toolButtonL")
        self.hLayout.addWidget(self.toolButtonL)
        self.toolButtonR = QtWidgets.QToolButton(FilteredTabelView)
        self.toolButtonR.setArrowType(QtCore.Qt.RightArrow)
        self.toolButtonR.setObjectName("toolButtonR")
        self.hLayout.addWidget(self.toolButtonR)
        self.verticalLayout.addLayout(self.hLayout)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(FilteredTabelView)
        self.dateTimeEdit.setDate(QtCore.QDate(2021, 2, 3))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.verticalLayout.addWidget(self.dateTimeEdit)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(FilteredTabelView)
        self.dateTimeEdit_2.setDate(QtCore.QDate(2021, 12, 30))
        self.dateTimeEdit_2.setCalendarPopup(True)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.verticalLayout.addWidget(self.dateTimeEdit_2)
        self.tableView = QtWidgets.QTableView(FilteredTabelView)
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(FilteredTabelView)
        QtCore.QMetaObject.connectSlotsByName(FilteredTabelView)

    def retranslateUi(self, FilteredTabelView):
        _translate = QtCore.QCoreApplication.translate
        FilteredTabelView.setWindowTitle(_translate("FilteredTabelView", "Form"))
        self.lineEdit_filter.setPlaceholderText(_translate("FilteredTabelView", "Filter"))
        self.lineEdit_limit.setPlaceholderText(_translate("FilteredTabelView", "limit"))
        self.label.setText(_translate("FilteredTabelView", "1/1"))
        self.toolButtonL.setText(_translate("FilteredTabelView", "..."))
        self.toolButtonR.setText(_translate("FilteredTabelView", "..."))
        self.dateTimeEdit.setDisplayFormat(_translate("FilteredTabelView", "yyyy-MM-dd hh:mm"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("FilteredTabelView", "yyyy-MM-dd hh:mm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FilteredTabelView = QtWidgets.QWidget()
    ui = Ui_FilteredTabelView()
    ui.setupUi(FilteredTabelView)
    FilteredTabelView.show()
    sys.exit(app.exec_())
