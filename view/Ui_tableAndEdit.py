# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/fares/Documents/devel/pypointage2/view/tableAndEdit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableAndEdit(object):
    def setupUi(self, TableAndEdit):
        TableAndEdit.setObjectName("TableAndEdit")
        TableAndEdit.resize(486, 455)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TableAndEdit)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(TableAndEdit)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.widgetForm = QtWidgets.QWidget(self.splitter)
        self.widgetForm.setMinimumSize(QtCore.QSize(200, 0))
        self.widgetForm.setStyleSheet("")
        self.widgetForm.setObjectName("widgetForm")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widgetForm)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.widgetForm)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 412, 343))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.EditB = QtWidgets.QPushButton(self.widgetForm)
        self.EditB.setObjectName("EditB")
        self.gridLayout.addWidget(self.EditB, 0, 3, 1, 1)
        self.SaveB = QtWidgets.QPushButton(self.widgetForm)
        self.SaveB.setObjectName("SaveB")
        self.gridLayout.addWidget(self.SaveB, 0, 4, 1, 1)
        self.DeleteB = QtWidgets.QPushButton(self.widgetForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Buttons/images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.DeleteB.setIcon(icon)
        self.DeleteB.setObjectName("DeleteB")
        self.gridLayout.addWidget(self.DeleteB, 1, 1, 1, 1)
        self.NewB = QtWidgets.QPushButton(self.widgetForm)
        self.NewB.setObjectName("NewB")
        self.gridLayout.addWidget(self.NewB, 1, 3, 1, 1)
        self.CancelB = QtWidgets.QPushButton(self.widgetForm)
        self.CancelB.setObjectName("CancelB")
        self.gridLayout.addWidget(self.CancelB, 0, 1, 1, 1)
        self.ExecB = QtWidgets.QPushButton(self.widgetForm)
        self.ExecB.setObjectName("ExecB")
        self.gridLayout.addWidget(self.ExecB, 1, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addWidget(self.splitter)

        self.retranslateUi(TableAndEdit)
        QtCore.QMetaObject.connectSlotsByName(TableAndEdit)

    def retranslateUi(self, TableAndEdit):
        _translate = QtCore.QCoreApplication.translate
        TableAndEdit.setWindowTitle(_translate("TableAndEdit", "Form"))
        self.EditB.setText(_translate("TableAndEdit", "Edit"))
        self.SaveB.setText(_translate("TableAndEdit", "Save"))
        self.DeleteB.setText(_translate("TableAndEdit", "Delete"))
        self.NewB.setText(_translate("TableAndEdit", "New"))
        self.CancelB.setText(_translate("TableAndEdit", "Cancel"))
        self.ExecB.setText(_translate("TableAndEdit", "Execute"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TableAndEdit = QtWidgets.QWidget()
    ui = Ui_TableAndEdit()
    ui.setupUi(TableAndEdit)
    TableAndEdit.show()
    sys.exit(app.exec_())
