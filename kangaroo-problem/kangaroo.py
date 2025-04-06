

def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return"YES" if x1 == x2 else "NO"
    # Calculate in n jumps will they tke the same time and it shd be positive
    if (x2-x1)%(v1-v2) == 0 and (x2-x1)/(v1-v2)<0:
        print("NO")
    elif (x2-x1)%(v1-v2) == 0:
        print("YES")
    else:
        print("NO")

    
kangaroo(0,3,4,2)
kangaroo(0,2,5,3)