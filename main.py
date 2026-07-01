import sys

from PySide6.QtWidgets import QApplication

from app.gui.windows.main_window import MainWindow


def main() -> int:
    """Punto de entrada de la aplicación."""
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
