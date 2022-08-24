#Class Work 1-3 : Decimal Degree and Sexagesimal Degree
#By 6331117421 Nawapon Nuangjumnong

#define program that convert decimal degree to sexagesimal degree
def dd2dms(dd):
    #devide decimal degree to define in a form degree:minute:second
    degree,minn = divmod(abs(dd),1)
    minute,sec = divmod(minn*60,1)
    second = sec*60
    if dd<0:
        degree *= -1
    degree = '{:.0f}'.format(degree)
    minute = int('{:.0f}'.format(minute))
    if minute < 10:
        minute = str(0)+str(minute)
    second = '{:.2f}'.format(second) #make second has 2 decimal points
    str_dms = '{:}:{:}:{:}'.format(degree,minute,second)
    return str_dms

#define program that convert sexagesimal degree to decimal degree
def dms2dd(dms):
    d,m,s = dms.split(':') #split sexagesimal degree by colon and keep it in variable  d,m and s
    dd = abs(float(d))+float(m)/60+float(s)/3600
    if float(d)<0:
        dd *= -1
    dd = '{:.5f}'.format(dd) #make decimal degree has 5 decimal points
    return dd

res = 'r' #variable for restart a program

print("--------------------------------------------------------")
print(' Class Work 1-3 : Decimal Degree and Sexagesimal Degree ')
while res == 'r':
    print("--------------------------------------------------------")
    print("What are you looking for?")
    print("a : Positive and Negative test.")
    print("b : just convert decimal degree to sexagesimal degree.")
    print("c : see you later")
    Ans = input("Type your answer and press enter: ").strip()

    if Ans == 'a':
        print('Type your decimal degree that you want to test')
        dd = float(input('Your decimal degree: '))
        if dd < 0:
            dd *= -1
        print('--------------------------------------------------------')
        print('•• Test decimal degree without minus:',dd)
        dms_positive = dd2dms(dd)
        new_dd_positive = dms2dd(dms_positive)
        print('convert by dd2dms(dd) :',dms_positive)
        print('convert back by dms2dd(dms) :',new_dd_positive)
        print('--------------------------------------------------------')
        print('•• Test decimal degree with minus',-1*dd)
        dms_negative = dd2dms(-1*dd)
        new_dd_negative = dms2dd(dms_negative)
        print('convert by dd2dms(dd) :',dms_negative)
        print('convert back by dms2dd(dms) :',new_dd_negative)
        print('--------------------------------------------------------')
        res = input('Type r and enter to back to mainmenu: ')
    elif Ans =='b':
        print('Type decimal degree you want to convert')
        dd = float(input('Your decimal degree: '))
        str_dms = dd2dms(dd)
        print('Convert by dd2dms(dd) :',str_dms)
        print('--------------------------------------------------------')
        res = input('Type r and enter to back to mainmenu: ')
    elif Ans == 'c':
        print('--------------------------------------------------------')
        print('Bye!')
        print('--------------------------------------------------------')
        exit()
