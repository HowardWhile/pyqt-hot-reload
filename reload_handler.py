# 使用watchdog來觀察資料夾的變動
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from PySide6.QtCore import QCoreApplication, QEvent
from console import DBG_PRINT

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, main_window):
        self.main_window = main_window

    def on_modified(self, event):
        DBG_PRINT(f"is_directory: {event.is_directory}, path: {event.src_path}",tag="on_modified")
        if event.src_path.endswith("my_widget.py"):  # 監測 `my_widget.py` 變動            
            DBG_PRINT(f"{event.src_path} 已變更，重新載入該 Widget...", tag="Reload Handler")     
            QCoreApplication.postEvent(self.main_window, QEvent(QEvent.User))

def start_watcher(main_window):
    event_handler = FileChangeHandler(main_window)
    observer = Observer()
    observer.schedule(event_handler, path="./widgets", recursive=False)
    observer.start()

    # 在主程式結束時停止監聽
    import atexit
    atexit.register(observer.stop)
