

from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
import sys
from pathlib import Path
import GlobVar


class FileDialog(QMainWindow):

    def __init__(self):
        super().__init__()

    def showDialog(self):


        GlobVar.Directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))