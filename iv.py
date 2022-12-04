from time import time
from datetime import datetime

class t:
    def __init__(self):
        self.t0_datetime=datetime.now().strftime("%Y-%m-%d %H:%M")
        self.t0=time()
        print(f"{self.t0_datetime} ({self.t0})")
    def __repr__(self):
        return f"{self.t0_datetime} ({self.t0})"
    def __str__(self):
        return self.t0_datetime,self.t0
    def end(self):
        t0=self.t0
        t1=time()
        return round((t1-t0)/60,1)
    