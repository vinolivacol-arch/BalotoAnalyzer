from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class DashboardPage(QWidget):
    """Página principal de la aplicación."""

    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("🎲 BalotoAnalyzer")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
        """)

        subtitle = QLabel(
            "Bienvenido.\n\n"
            "En las próximas versiones podrás:\n"
            "• Descargar sorteos automáticamente\n"
            "• Analizar estadísticas\n"
            "• Generar jugadas\n"
            "• Exportar resultados"
        )

        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(subtitle)
