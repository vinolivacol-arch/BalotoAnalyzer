from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    """Ventana principal de BalotoAnalyzer."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("BalotoAnalyzer")
        self.resize(1200, 800)

        # Área central
        container = QWidget()
        layout = QVBoxLayout(container)

        title = QLabel("🎲 Bienvenido a BalotoAnalyzer")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addStretch()
        layout.addWidget(title)
        layout.addStretch()

        self.setCentralWidget(container)

        # Barra de estado
        status = QStatusBar()
        status.showMessage("Listo")
        self.setStatusBar(status)
