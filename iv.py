from time import time
from datetime import datetime

class t:
    def __init__(self):
        self.t0_datetime=datetime.now().strftime("%m-%d %H:%M")
        self.t0=time()
        print(f"{self.t0_datetime} ({self.t0})")
    def __repr__(self):
        t0=self.t0
        t1=time()
        t1_in=datetime.now().strftime("%m-%d %H:%M")
        return f"{self.t0_datetime}->{t1_in} ({round((t1-t0)/60,1)})"
    