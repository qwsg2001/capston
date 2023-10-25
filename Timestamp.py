import time

class Timestamp():
    def __init__(self):
        self.start = time.time()
        self.p_time = self.start

    def check(self, name = ""):
        stamp = time.time()
        duration = stamp - self.p_time
        print(f'{name} 소요시간 : {duration}')
        self.p_time = stamp

    def checkout(self):
        total_dur = time.time() - self.start
        print(f'총 소요시간 : {total_dur}')