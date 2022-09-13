import threading
import time
from src.logger.logger import Logger

TAG = "RepeatedTask"

class RepeatedTask():
    def __init__(self, interval: int, func, *args, **kwargs):
        self.is_running = False
        self.func = func
        self.interval = interval
        self.args = args
        self.kwargs = kwargs

    def start(self):
        Logger.d(TAG, "start")
        self.is_running = True
        self._start()

    def _start(self):
        Logger.d(TAG, f"internal start, should keep running = {self.is_running}")
        if self.is_running:
            self.func(*self.args, **self.kwargs)
            threading.Timer(self.interval, self._start).start()

    def stop(self):
        Logger.d(TAG, "stop")
        self.is_running = False
