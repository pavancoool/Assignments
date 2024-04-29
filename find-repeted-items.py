#write aprogram to find repeated items in a tuple.

t=(1,'pp',3,4,5,'apple',220.0,3,5,5,6,6)
for i in t:
    count=t.count(i)
    if count>1:
        print('count of', i ,'is', count)

    
