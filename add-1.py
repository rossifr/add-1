import time
import random as r

while True:
  a=r.randint(0,9)
  b=r.randint(0,9)
  c=r.randint(0,9)
  d=r.randint(0,9)
  print('\033[91m'+str(a),b,c,str(d)+'\033[0m',end="\r")
  time.sleep(1)
  print("       ",end="\r")
  time.sleep(6)
  print('\033[92m'+str((a+1)%10),(b+1)%10,(c+1)%10,str((d+1)%10)+'\033[0m',end="\r")
  time.sleep(3)
