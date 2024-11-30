from PySide6.QtWidgets import QHBoxLayout, QMainWindow, QWidget

from widgets.dashboard import Dashboard
from widgets.toolbar import Toolbar


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setMinimumSize(1000, 800)

        central_widget = QWidget()

        layout = QHBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.toolbar = Toolbar(central_widget)
        self.dashboard = Dashboard(central_widget)

        layout.addWidget(self.toolbar)
        layout.addWidget(self.dashboard)

        self.setCentralWidget(central_widget)
