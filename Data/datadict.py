# from collections import *

 
 
# dict1 = {"a":1, "b":1}
# dict2 = {"a":2,"c":3}
# dict1.update(dict2)
# print(dict1)
 
# #-----------------------------------------
 
# default = {"theme": "light", "font": 12}
# user = {"theme": "dark"}
# ChainMap1 = ChainMap(user, default)
# print(ChainMap1)

# #-------------------------------------------
from collections import OrderedDict
 
data = OrderedDict([('b', 2), ('c', 1)])
 
data.setdefault('a', 5)
data.move_to_end('b')
 
print(data)
 
data.popitem(last=False)
 
print(data)
 
 #---------------------------------------
 