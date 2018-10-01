def var_test(a,b=2,*xyz, **abc):
    print(a)
    print(b)
    print(xyz)
    print(abc)

ter_a = 1 if 2+2 ==5 else 2
print(ter_a)

var_test(1,3,4,5,6,x=7,y=8)
