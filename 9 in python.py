import random
x=[ ]
y=[ ]
z=[ ]
a='_'

size=random.randint(10,20)
for i in range(size+1):
    x.append(i)
    y.append(a)
print(x)
print(i)
p1=1
p2=0

while x!=y:
    if p1>p2:
        m=int(input('enter no. of tokens you will choose 1 or 2:'))
        if m==1:
            while True:
                k=int(input('p1:'))
                if k in z:
                    print('someone choose this number before plz choose another number;')
                else:
                    z.append(k)
                    x[k-1]=a
                    p2=p2+2
                    print(x)
                    break
                    
        elif m==2:
            while True:
                k=int(input('p1:'))
                l=int(input('p1:'))
                if l==k+1:
                    if k in z:
                        print('someone choose those numbers before plz choose another number;')
                    elif l in z:
                        print('someone choose those numbers before plz choose another number;')
                        
                    else :
                        z.append(k)
                        z.append(l)
                        x[k-1]=a
                        x[l-1]=a
                        p2=p2+2
                        print(x)
                        break
                else:
                    print('you should choose adjecent tokens;')

                
        else:
            print('you should choose only one or two tokens to remove only')

    
    if x!=y:    
        if p2>p1:
            m=int(input('enter no. of tokens you will choose 1 or 2:'))
            if m==1:
                while True:
                    k=int(input('p2:'))
                    if k in z:
                        print('someone choose this number before plz choose another number;')
                    else:
                        z.append(k)
                        x[k-1]=a
                        p1=p1+2
                        print(x)
                        break
                    
            elif m==2:
                while True:
                    k=int(input('p2:'))
                    l=int(input('p2:'))
                    if l==k+1:
                        if k in z:
                            print('someone choose those numbers before plz choose another number;')
                        elif l in z:
                            print('someone choose those numbers before plz choose another number;')
                        else :
                            z.append(k)
                            z.append(l)
                            x[k-1]=a
                            x[l-1]=a
                            p1=p1+2
                            print(x)
                            break
                    else:
                        print('you should choose adjecent tokens;')

                
            else:
                print('you should choose only one or two tokens to remove only')


if p2>p1:
    print('the first player is the winner')
else:
    print('the second player is the winner ')
    

