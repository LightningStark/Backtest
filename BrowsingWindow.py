from PyQt5.QtWidgets import QMainWindow, QFileDialog
import UniversalVar


class FileDialog(QMainWindow):

    def __init__(self):
        super().__init__()
        UniversalVar.Directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
