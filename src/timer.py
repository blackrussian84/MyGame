import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if self.start_time is not None:
            self.elapsed_time += time.time() - self.start_time
            self.start_time = None

    def reset(self):
        self.elapsed_time = 0
        self.start_time = None

    def get_elapsed_time(self):
        if self.start_time is not None:
            return self.elapsed_time + (time.time() - self.start_time)
        return self.elapsed_time

    def countdown(self, seconds):
        self.start()
        while self.get_elapsed_time() < seconds:
            time.sleep(1)
        self.stop()