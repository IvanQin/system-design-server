import threading
import time

class RepeatedTask():
    def __init__(self, interval: int, func, *args, **kwargs):
        self.is_running = False
        self.func = func
        self.interval = interval
        self.args = args
        self.kwargs = kwargs

    def start(self):
        self.is_running = True
        self._start()

    def _start(self):
        if self.is_running:
            self.func(*self.args, **self.kwargs)
            threading.Timer(self.interval, self._start).start()

    def stop(self):
        self.is_running = False
