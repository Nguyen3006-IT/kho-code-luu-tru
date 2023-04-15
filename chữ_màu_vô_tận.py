 # ngôn ngữ Python
 # dòng chữ màu vô hạng
 
import random
import datetime
import time

color = ['\033[30m', '\033[31m',
         '\033[32m', '\033[33m',
         '\033[34m', '\033[35m',
         '\033[36m', '\033[37m',
         '\033[38m', '\033[39m',]
              
N = datetime.date(2021, 6, 13)
 
while True:
        i= random.randint(0, 9)
        print(color[i] + N.strftime(" %d-%m-%y"), 
        ': Anh yêu em vô cực - Anh yêu em vô cực - Anh yêu em vô cực - Anh yêu em vô cực',sep="")
        time.sleep(0.01)
        N += datetime.timedelta(days = 1)
