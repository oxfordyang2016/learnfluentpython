#unpack a tuple 's advanced usage
def unpackatuple(a,b,c):
    return(a+b+c)

a=(1,2,3)
print(unpackatuple(*a))
a,b,c=(1,2,3)
#note it is  a tuple
print(a,b,c)
#but in the console,the a,b,c is a tuple,but the above is 1,2,3

#how to split a file path to two part (dir,filename)
#_ like placeholder usage
#unpack a tuple
import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print filename#idrsa.pub


