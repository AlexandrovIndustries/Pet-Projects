import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import Slot, Qt, QEvent
import webbrowser

class SearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Поисковая строка')
        self.resize(400, 200)

        layout = QVBoxLayout()

        self.title = QLabel('Поиск в браузере')
        self.title.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title)

        self.label = QLabel('Введите запрос:')
        layout.addWidget(self.label)

        self.entry = QLineEdit(self)
        self.entry.returnPressed.connect(self.search) 
        layout.addWidget(self.entry)

        self.button = QPushButton('Поиск', self)
        self.button.clicked.connect(self.search)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress and source is self.entry:
            if event.key() == Qt.Key_Return and event.modifiers() == Qt.ShiftModifier:
                cursor = self.entry.cursorPosition()
                self.entry.insert('\n')
                self.entry.setCursorPosition(cursor + 1)
                return True
        return super().eventFilter(source, event)

    @Slot()
    def search(self):
        query = self.entry.text()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SearchApp()
    ex.show()
    sys.exit(app.exec())