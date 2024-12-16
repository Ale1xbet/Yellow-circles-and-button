import sys
import io
from random import randint
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush
from PyQt6.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsEllipseItem, QApplication



class Generator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI_Files/UI.ui", self)
        self.scene = QGraphicsScene(0, 0, 400, 200)
        self.draw_button.clicked.connect(self.draw_yellow_circle)
    
    def draw_yellow_circle(self):
        self.scene.clear()
        rad = randint(10, 50)

        ellipse = QGraphicsEllipseItem(50 - rad, 50 - rad, 50 + rad, 50 + rad)
        ellipse.setPos(50, 50)

        brush = QBrush(Qt.GlobalColor.yellow)
        ellipse.setBrush(brush)
        self.scene.addItem(ellipse)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Generator()
    ex.show()

    sys.exit(app.exec())
