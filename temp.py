#得到汉明距离
import numpy as np
import re
c=np.array([(1,5,3),(2,4,6)])
c[c<np.mean(c)]=0
c[c>0]=1
a=np.array([(1,1,0),(1,0,0)])
b=np.array([(1,0,1),(1,1,0)])
print(np.sum((a-b)!=0))
a1=''.join(re.findall('[0-9]*',np.array2string(a, precision=2, separator='',suppress_small=True)))
b1=''.join(re.findall('[0-9]*',np.array2string(b, precision=2, separator='',suppress_small=True)))
bin(int(a1,2)^int(b1,2)).count('1')
