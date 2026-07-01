from PySide6.QtWidgets import (
    QMainWindow,
    QSplitter,
    QStackedWidget,
    QStatusBar,
)

from app.gui.pages.dashboard_page import DashboardPage
from app.gui.widgets.sidebar import Sidebar


class MainWindow(QMainWindow):
    """Ventana principal de BalotoAnalyzer."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("BalotoAnalyzer")
        self.resize(1200, 800)

        self._create_ui()

    def _create_ui(self) -> None:
        splitter = QSplitter()

        self.sidebar = Sidebar()

        self.pages = QStackedWidget()
        self.pages.addWidget(DashboardPage())

        splitter.addWidget(self.sidebar)
        splitter.addWidget(self.pages)

        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)

        self.setCentralWidget(splitter)

        status = QStatusBar()
        status.showMessage("Listo")
        self.setStatusBar(status)

        self.sidebar.currentRowChanged.connect(self.change_page)

    def change_page(self, index: int) -> None:
        """Cambia la página mostrada."""

        if 0 <= index < self.pages.count():
            self.pages.setCurrentIndex(index)

