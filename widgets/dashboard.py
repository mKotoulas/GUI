from PySide6.QtWidgets import QWidget


class Dashboard(QWidget):
    def __init__(self, parent: QWidget | None = None):
        super().__init__(parent)

        self.setAutoFillBackground(True)

        self.setStyleSheet("background-color: blue")
