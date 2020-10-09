from PySide2 import QtWidgets
import ba_helper, custom_tools
import sys

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BA Helper")
        self.setGeometry(300,200,500,100)
        self.setup_ui()
        self.setup_connections()
    
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.label_feature = QtWidgets.QLabel("Veuillez préciser le chemin du dossier racine contenant les fichiers .feature")
        self.input_features_filepath = QtWidgets.QLineEdit()

        self.label_java = QtWidgets.QLabel("Veuillez préciser le chemin du dossier racine contenant les fichiers java")
        self.input_java_filepath = QtWidgets.QLineEdit()
        
        self.btn_submit = QtWidgets.QPushButton("Envoyer")
        self.btn_submit.setMaximumWidth(100)

        self.btn_quit = QtWidgets.QPushButton("Quitter")
        self.btn_quit.setMaximumWidth(100)

        self.layout.addWidget(self.label_feature)
        self.layout.addWidget(self.input_features_filepath)

        self.layout.addWidget(self.label_java)
        self.layout.addWidget(self.input_java_filepath)

        self.layout.addWidget(self.btn_submit)
        self.layout.addWidget(self.btn_quit)
    
    def setup_connections(self):
        global app
        self.btn_submit.clicked.connect(self.ba_helper)
        self.btn_quit.clicked.connect(app.exit)

    def ba_helper(self):
        features = self.input_features_filepath.text()
        java = self.input_java_filepath.text()

        try:
            ba_helper.main(features, java)
        except NotADirectoryError:
            self.show_directory_error()
        else:
            self.show_success()

    def show_directory_error(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)

        msgBox.setText("Les chemins spécifiés ne sont pas correct !")
        msgBox.setWindowTitle("Erreur !")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def show_success(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)

        msgBox.setText("Tous les tests ont été traités !")
        msgBox.setWindowTitle("Terminé !")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

app = QtWidgets.QApplication([])
window = App()
window.show()
app.exec_()