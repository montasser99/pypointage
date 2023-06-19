# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QTableView
from PyQt5.QtSql import  QItemDelegate
from PyQt5.QtCore import Qt


class CopySelectedCellsAction(QAction):
    def __init__(self, table_widget):
        if not isinstance(table_widget, QTableView):
            raise ValueError(str('CopySelectedCellsAction must be initialised with a QTableView. A %s was given.' % type(table_widget)))
        super(CopySelectedCellsAction, self).__init__("Copy", table_widget)
        self.setShortcut('Ctrl+C')
        self.triggered.connect(self.copy_cells_to_clipboard)
        self.table_widget = table_widget

    def copy_cells_to_clipboard(self):
        if len(self.table_widget.selectionModel().selectedIndexes()) > 0:
            # sort select indexes into rows and columns
            previous = self.table_widget.selectionModel().selectedIndexes()[0]
            columns = []
            rows = []
            for index in self.table_widget.selectionModel().selectedIndexes():
                if previous.column() != index.column():
                    columns.append(rows)
                    rows = []
                rows.append(index.data())
                previous = index
            columns.append(rows)
            print (columns )

            # add rows and columns to clipboard            
            clipboard = ""
            nrows = len(columns[0])
            ncols = len(columns)
            for r in xrange(nrows):
                for c in xrange(ncols):
                    clipboard += columns[c][r]
                    if c != (ncols-1):
                        clipboard += '\t'
                clipboard += '\n'

            # copy to the system clipboard
            sys_clip = QApplication.clipboard()
            sys_clip.setText(clipboard)

