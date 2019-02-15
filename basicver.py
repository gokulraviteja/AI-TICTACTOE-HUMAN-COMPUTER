def display(ar):
    print()
    print(".............")
    for i in ar:
        for j in i:
            print(j,end=' ')
        print()
    print()
    print(".............")

def evaluate(ar):
    a=[]
    for i in ar:
        for j in i:
            a.append(j)
    if(a[0]==a[1]==a[2] or a[0]==a[3]==a[6]):
        if(a[0]!=' ' and a[0]==C):
            return 1
        elif(a[0]!=' ' and a[0]==U):
            return -1
        
    if(a[3]==a[4]==a[5] or a[1]==a[4]==a[7]):
        if(a[4]!=' ' and a[4]==C):
            return 1
        elif(a[4]!=' ' and a[4]==U):
            return -1
        
    if(a[6]==a[7]==a[8] or a[2]==a[5]==a[8]):
        if(a[8]!=' ' and a[8]==C):
            return 1
        elif(a[8]!=' ' and a[8]==U):
            return -1
        
    if(a[0]==a[4]==a[8] or a[2]==a[4]==a[6]):
        if(a[4]!=' ' and a[4]==C):
            return 1
        elif(a[4]!=' ' and a[4]==U):
            return -1
        
    return 0


def fact(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s


def fun(a,c):
    #print(a,c)
    if(c==0):
        if(evaluate(a)==1):
            return [1,(-1,-1)]
        elif(evaluate(a)==-1):
            return [-1,(-1,-1)]
        else:
            return [0,(-1,-1)]
            
    filler='X'
    if(c%2==0):
        filler='O'
    pp=[]
    for i in range(3):
        for j in range(3):
            if(a[i][j]=='_'):
                pp.append((i,j))
    #print(pp)
    arr=[]
    for ii in pp:
        achanged=[]
        for i in a:
            kt=[]
            for p in i:
                kt.append(p)
            achanged.append(kt)
        
        achanged[ii[0]][ii[1]]=filler
        kk,xx=fun(achanged,c-1)
        arr.append([kk,ii])
    s=0
    for i in arr:
        s+=i[0]
    

    if(filler==C):
        ma=max(arr)
    else:
        ma=min(arr)
    return s,ma[1]
    
def choose(a):
    c=0
    for i in a:
        for j in i:
            if(j!='_'):
                c+=1
    c=9-c
    pp=fun(a,c)
    return pp[1]
    
            
    
    











a=[]
for i in range(3):
    a.append(['_']*3)
display(a)
user=int(input("1 FOR PLAYER 1"))
looplen=9
U='X'
C='O'
if(user==1):
    looplen=8
    x,y=[int(xx) for  xx in input("X Y").split()]
    a[x-1][y-1]=U
else:
    U,C=C,U

for dci in range(looplen):
    if(dci%2==0):
        #COMPUTER
        x,y=choose(a)
        a[x][y]=C
        if(evaluate(a)==1):
            print("YOU LOSE")
            break
        display(a)
    else:
        #USER
        x,y=[int(xx) for  xx in input("X Y").split()]
        a[x-1][y-1]=U
        if(evaluate(a)==-1):
            print("YOU WIN")
            break
        display(a)
if(evaluate(a)==0):
    print("DRAW")
        
    
    
    
    















    
