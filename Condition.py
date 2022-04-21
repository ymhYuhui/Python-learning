#疫情隔离 条件判断
import os #为了满足输入完毕之后的程序结果查看

def Confition_N():    
    print ("Have you been told by NHS Test & Trace that you're a close contant of an infected person?")        
    inputContent=input().upper()
    if inputContent=="YES":
        print("Self isolate for 10 days,Work from home if you can.You Will receive full pay,but will need evidence of your contact with the NHS")
    elif inputContent=="NO":
        print ("Attend work")
    else :
        print('Incorrect Answer,Please use "YES" or "NO" to answer.')
        Confition_N()

def Confition_Y():
    print("Slef-isonlate immediately and book a test")
    print("Positive test for coronavirus:")   
    inputContent=input().upper()
    if inputContent=="YES":
        print("Slef isonlate for 10 days form data of first symptoms or of test,whichever is eraliest")
    elif inputContent=="NO":
        print("Return to work if you are well enough to do so")
    else :
        print('Incorrect Answer,Please use "YES" or "NO" to answer.')
        Confition_Y()

def Confition():
    print("Do you have symptoms?")
    inputContent=input().upper()
    if inputContent=="NO":      
        Confition_N()  
    elif inputContent=="YES":
        Confition_Y()
    else :
        print('Incorrect Answer,Please use "YES" or "NO" to answer.')
        Confition()

#判断 
Confition()
os.system("pause")