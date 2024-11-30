from PySide6.QtWidgets import QWidget


class Toolbar(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.setStyleSheet("background-color: red; border: 2px solid red;")
        self.setFixedWidth(200)
