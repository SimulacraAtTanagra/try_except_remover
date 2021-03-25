#Arbitrary program to see if I can remoe try except blocks procedurally. 
#Just to see if I can. Also to dunk on someone on reddit. 
#phase 1: find the try except block
#phase 2L remove try except lines and de-indent following
import os 


def get_lines(filename):
    with open(filename,'r') as f:
        lines=f.readlines()
        lines=[line for line in lines if '#' not in line]
        data= [[ix,line,line.count('    ')] for ix,line in enumerate(lines)]
    return(data)
def update_lines(data):
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
    return(newlines)

def write_to_py(newlines,filename):
    with open(filename,'w') as f:
        f.writelines(newlines)

def write_throw():
    throwlines=['#throwaway file to test my new function\n','def throwmane():','\ttry:',
    '\t\tprint("apples are red")','\t\tprint("violets are blue!")','\texcept:',
    '\t\tprint("This is the song that never ends.")','\tprint("Hey now, youre a rockstar")\n',
    'if __name__=="__main__":','\tthrowmane()']
    filename=os.path.join(os.cwd(),'throwaway.py')
    write_to_py(throwlines,filename)
    
def main(filename=None):
    """
    This is the try/except block removal program. If you do not specify a filename,
    the program will assume you want to create and use the 'throwaway.py' test file.
    Else, it will process as usual. This is not a sophisistcated function. It
    will remove ALL instances of try or except (with colons) and their child statements.
    It doesn't ask first and it doesn't require confirmation. This cannot be undone
    using ctrl+z. Make a backup before you run this just in case (or follow proper
    protocol and keep repos for your code, programmer).
    
    Okay.
    
    You've been warned
    """
    if filename:
        filename=filename
    else:
        write_throw()
        filename=os.path.join(os.cwd(),'throwaway.py')
        
    #creating the throwaaway file first

    data=get_lines(filename)
    newlines=update_lines(data)
    write_to_py(newlines,filename)
            
if __name__=='__main__':
    main()
            