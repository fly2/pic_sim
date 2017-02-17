#得到汉明距离
import numpy as np
import re
a=np.array([(1,1,0),(1,0,0)])
b=np.array([(1,0,1),(1,1,0)])
print(np.sum((a-b)!=0))
a1=''.join(re.findall('[0-9]*',np.array2string(a, precision=2, separator='',suppress_small=True)))
b1=''.join(re.findall('[0-9]*',np.array2string(b, precision=2, separator='',suppress_small=True)))
bin(int(a1,2)^int(b1,2)).count('1')
