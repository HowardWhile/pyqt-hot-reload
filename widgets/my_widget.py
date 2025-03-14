# ui_module.py
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from console import DBG_PRINT

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.widget_name = "MyWidget A"
        self.init_ui()
        DBG_PRINT(f"{self.widget_name}", tag="__init__")

    def __del__(self):
        DBG_PRINT(f"{self.widget_name}", tag="__del__")

    def init_ui(self):
        layout = QVBoxLayout()
        self.label = QLabel(f"這是可熱重載的 {self.widget_name}", self)
        layout.addWidget(self.label)
        self.setLayout(layout)
        

