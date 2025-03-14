import sys
import importlib
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGroupBox
from PySide6.QtCore import QEvent

from reload_handler import start_watcher
from widgets import my_widget

from console import DBG_PRINT

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt 熱重載 UI 測試")
        self.setGeometry(100, 100, 600, 400)

        # 主視窗 Layout
        main_layout = QVBoxLayout()

        # 上方的按鈕區
        button_layout = QHBoxLayout()
        btn1 = QPushButton("按鈕 1")
        btn2 = QPushButton("按鈕 2")
        btn3 = QPushButton("按鈕 3")
        button_layout.addWidget(btn1)
        button_layout.addWidget(btn2)
        button_layout.addWidget(btn3)
        main_layout.addLayout(button_layout)

        # 下方的 GroupBox 容器
        self.groupbox = QGroupBox("可熱重載 Widget")
        self.groupbox_layout = QVBoxLayout()
        self.groupbox.setLayout(self.groupbox_layout)
        main_layout.addWidget(self.groupbox)

        # 載入可熱重載的 Widget
        self.reload_widget()

        # 設定中央 Widget
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def event(self, event):
        if event.type() == QEvent.User:
            self.reload_widget()
            return True
        return super().event(event)

    def reload_widget(self):
        DBG_PRINT("", tag="reload_widget")

        # 清除舊 Widget
        for i in reversed(range(self.groupbox_layout.count())):
            self.groupbox_layout.itemAt(i).widget().setParent(None)

        """重新載入 GroupBox 內的 Widget"""
        importlib.reload(my_widget)  # 重新載入 UI
        new_widget = my_widget.MyWidget()

        # 加入新 Widget
        self.groupbox_layout.addWidget(new_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    # 啟動監聽（監測 `ui_module.py`，自動重載 Widget）
    start_watcher(window)

    sys.exit(app.exec())
