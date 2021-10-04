from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QVBoxLayout, QLabel, QMessageBox

from PIL import Image
import numpy as np

from histogram_equalization import histogram_equalization
from Lissage import lissage

class Dialog(QtWidgets.QDialog):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        _translate = QtCore.QCoreApplication.translate

        self.setWindowTitle(_translate("Iris Recognition", "Iris Recognition"))

        self.resize(768, 623)
        self.Recognition = QtWidgets.QPushButton(self)
        self.Recognition.setGeometry(QtCore.QRect(530, 110, 141, 32))
        self.Recognition.setObjectName("Recognition")
        self.Recognition.setText(_translate("Dialog", "Recognition"))
        
        self.upload = QtWidgets.QPushButton(self)
        self.upload.setGeometry(QtCore.QRect(530, 70, 141, 32))
        self.upload.setObjectName("Enrollement")
        self.upload.clicked.connect(self.enrollement)
        self.upload.setText(_translate("Dialog", "Enrollement"))
        
        self.LabelOriginal = QtWidgets.QLabel(self)
        self.LabelOriginal.setGeometry(QtCore.QRect(242, 30, 271, 166))
        self.LabelOriginal.setTextFormat(QtCore.Qt.RichText)
        self.LabelOriginal.setPixmap(QtGui.QPixmap("white.png"))

        self.LabelOriginal.setScaledContents(True)
        self.LabelOriginal.setObjectName("LabelOriginal")
        
        self.Histogram = QtWidgets.QLabel(self)
        self.Histogram.setGeometry(QtCore.QRect(20, 240, 221, 141))
        self.Histogram.setTextFormat(QtCore.Qt.RichText)
        self.Histogram.setPixmap(QtGui.QPixmap("white.png"))

        self.Histogram.setScaledContents(True)
        self.Histogram.setObjectName("Histogram")
        
        self.Lissage = QtWidgets.QLabel(self)
        self.Lissage.setGeometry(QtCore.QRect(270, 240, 221, 141))
        self.Lissage.setTextFormat(QtCore.Qt.RichText)
        self.Lissage.setPixmap(QtGui.QPixmap("white.png"))
        self.Lissage.setScaledContents(True)
        self.Lissage.setObjectName("Lissage")
        
        self.Segmentation = QtWidgets.QLabel(self)
        self.Segmentation.setGeometry(QtCore.QRect(520, 240, 221, 141))
        self.Segmentation.setTextFormat(QtCore.Qt.RichText)
        self.Segmentation.setPixmap(QtGui.QPixmap("white.png"))
        self.Segmentation.setScaledContents(True)
        self.Segmentation.setObjectName("Segmentation")
        
        self.Morphologic = QtWidgets.QLabel(self)
        self.Morphologic.setGeometry(QtCore.QRect(20, 430, 221, 141))
        self.Morphologic.setTextFormat(QtCore.Qt.RichText)
        self.Morphologic.setPixmap(QtGui.QPixmap("white.png"))
        self.Morphologic.setScaledContents(True)
        self.Morphologic.setObjectName("Morphologic")
        
        self.Sift = QtWidgets.QLabel(self)
        self.Sift.setGeometry(QtCore.QRect(270, 430, 221, 141))
        self.Sift.setTextFormat(QtCore.Qt.RichText)
        self.Sift.setPixmap(QtGui.QPixmap("white.png"))
        self.Sift.setScaledContents(True)
        self.Sift.setObjectName("Sift")
        
        self.LabelOriginal_7 = QtWidgets.QLabel(self)
        self.LabelOriginal_7.setGeometry(QtCore.QRect(520, 430, 221, 141))
        self.LabelOriginal_7.setTextFormat(QtCore.Qt.RichText)
        self.LabelOriginal_7.setPixmap(QtGui.QPixmap("white.png"))
        self.LabelOriginal_7.setScaledContents(True)
        self.LabelOriginal_7.setObjectName("LabelOriginal_7")
        
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 390, 58, 16))
        self.label.setObjectName("label")
        self.label.setText(_translate("Dialog", "Histogram"))
        
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(350, 390, 58, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setText(_translate("Dialog", "Lissage"))
        
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(600, 390, 58, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText(_translate("Dialog", "Segmentation by Clustering"))
        
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(360, 590, 58, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText(_translate("Dialog", "Sift"))
        
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(610, 580, 58, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setText(_translate("Dialog", "Distance"))
        
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(100, 590, 58, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setText(_translate("Dialog", "Opérations morphologiques"))
        
        QtCore.QMetaObject.connectSlotsByName(self)
        
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("resultat")
        self.b1.clicked.connect(self.clicked)
        
    
    def clicked(self):
        self.Recognition.setText("NOT MATCHED !!! ") 
    
    
    def processings(self, filepath):
        
        # read image & display
        image = Image.open(filepath[0])
        image = np.asarray(image)
        self.LabelOriginal.setPixmap(self.prepare_image_for_display(image))

        # histogram equalization
        image = histogram_equalization(image)
        self.Histogram.setPixmap(self.prepare_image_for_display(image))

        # Lissage
        image = lissage(image)
        pixmap = QtGui.QPixmap("lissage.bmp")
        self.Lissage.setPixmap(pixmap)
        
        # Segmentation
        pixmap = QtGui.QPixmap("Segmentation.bmp")
        self.Segmentation.setPixmap(pixmap)
        
        #Operation
        pixmap = QtGui.QPixmap("input.jpeg")
        self.Morphologic.setPixmap(pixmap)
        
        # sift 
        
        pixmap = QtGui.QPixmap("matched_images.jpg")
        self.Sift.setPixmap(pixmap)
        
        # Distance 
        pixmap = QtGui.QPixmap("distance.png")
        self.LabelOriginal_7.setPixmap(pixmap)
        
    def prepare_image_for_display(self, image):
        return QPixmap.fromImage(QImage(image, image.shape[1], image.shape[0], QImage.Format_Grayscale8)) 

    
    def enrollement(self):
        # 1. grab filepath
        filepath = QFileDialog.getOpenFileName(None, "Open File", '.', '(*.bmp *.jpg *.png)')
    
        # 2. processings
        self.processings(filepath)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
