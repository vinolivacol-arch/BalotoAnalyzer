from PySide6.QtWidgets import QListWidget


class Sidebar(QListWidget):
    """Menú lateral principal."""

    def __init__(self) -> None:
        super().__init__()

        self.setFixedWidth(220)

        self.addItems(
            [
                "📊 Dashboard",
                "🎰 Histórico",
                "📈 Estadísticas",
                "🎲 Jugadas",
                "⚙ Configuración",
            ]
        )

        self.setCurrentRow(0)
