print('welcome to pycalculator!')#welcome
while True:#loop
    
    op=(input("choose: +,-,*,/,e\n:"))#opretore input
    if op == 'e':#if you enter 'e' program is end
        exit('-------exite-------')#display exite
    
    a=int(input('enter first num:'))#enter number
    b=int(input('enter second num:'))#enter 2nd number
    
    if op== '+':
        c= a + b
        print(f'result:{c}\n-----------')
    
    elif op=='-':
        c= a - b
        print(f'result:{c}\n-----------')
   
    elif op== '*':
        c = a *b
        print(f'result:{c}\n-----------')
    
    elif op == '/':
        if b != 0:  
            c = a / b
            print(f'result:{c}\n-----------')
        
        else:
            print("----Division by zero is not allowed.-------")
    
    else:
        print('please!,choose:+,-,*,/,e')


