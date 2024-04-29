#write a python program to create the colon of a tuple.

from copy import deepcopy
t=(1,'apple',['empty'],False,16,26,22.30)
print(t)
tcopy=deepcopy(t)
tcopy[2].append(100.2)
print(tcopy ,"This is  Deepcopy")

