#Arbitrary program to see if I can remoe try except blocks procedurally. 
#Just to see if I can
#phase 1: find the try except block
#phase 2L remove try except lines and de-indent following

import src.throwaway

def main(filename):
    with open(filename,'r') as f:
        lines=f.readlines()
        data= [[ix,line,line.count('    ')] for ix,line in enumerate(lines)]
    newlines=[]
    num2=999
    try1=except1=False
    for datum in data:
        if num2!=datum[2]:    
            if try1==True:
                datum[1]=datum[1].replace((datum[2])*"    ",(datum[2]-1)*"    ")
                newlines.append(datum[1])
            elif except1==True:
                pass
            if "try:" in datum[1]:
                try1=True
                num2=datum[2]
                pass
            if "except" in datum[1]:
                except1=True
                num2=datum[2]
                pass
            if try1+except1<1:
                newlines.append(datum[1])
        else:
            try1=except1=False
            num2=999        
            if "try:" in datum[1]:
                try1=True
                num2=datum[2]
                pass
            if "except" in datum[1]:
                except1=True
                num2=datum[2]
                pass
            if try1+except1<1:
                newlines.append(datum[1])
            print(datum[1])
    with open(filename,'w') as f:
        f.writelines(newlines)
            
            
            
            