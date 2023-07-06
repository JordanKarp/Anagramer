from time import time
from threading import Timer


class GameTimer(Timer):
    started_at = None

    def start(self):
        self.started_at = time()
        Timer.start(self)

    @property
    def elapsed(self):
        return time() - self.started_at

    @property
    def remaining(self):
        return round(self.interval - self.elapsed, 1)

    @property
    def expired(self):
        return self.interval - self.elapsed <= 0
