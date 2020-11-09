from PyQt5.QtWidgets import QMainWindow, QFileDialog
import GlobVar


class FileDialog(QMainWindow):

    def __init__(self):
        super().__init__()

    def showDialog(self):

        GlobVar.Directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
