dic1={1:'ECE','name':'Ram','list':[1,2,3],'tuple':(4,5,6)}
print(type(dic1))
print(type(dic1['list']))
print(type(dic1['tuple']))
dic2=dict(x=5,y=0) # using keyword args
print(dic2)
dic3=dict({'x':5,'y':11}) # using mapping
print(dic3)
dic4=dict([('x',11),('y',27)]) # using iterable
print(dic4)