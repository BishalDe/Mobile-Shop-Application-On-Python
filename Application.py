#------MODULES---------
import pickle
import os
import colorama
import csv
import pandas
import time
import mysql.connector
from tqdm import tqdm
from colorama.ansi import Fore
from datetime import date,datetime
from tabulate import tabulate
import pwinput
window_size='mode 190,30'
os.system(window_size)



#---------FUNCTIONS------------
def togetdate():
    today = date.today()
    return today

def togettime():
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    return time
    
def introdetail():
    print()
    print("                    TODAY'S DATE : ",togetdate(),end='                                                                                      ')
    print("CURRENT TIME : ",togettime())
    print("                    GST  ID      : ", "8299260163",end='                                                                                      ')
    print("SHOP ID : ","735226735IN")

def intro():
    
    print(Fore.YELLOW+''' 
         __  __       _     _ _            _____       _               __  __                                                         _       _____           _
        |  \/  |     | |   (_) |          / ____|     | |             |  \/  |                                                       | |     / ____|         | |
        | \  / | ___ | |__  _| | ___     | (___   __ _| | ___  ___    | \  / | __ _ _ __   __ _ _ __   __ _  ___ _ __ ___   ___ _ __ | |_   | (___  _   _ ___| |_ ___ _ __ ___   
        | |\/| |/ _ \| '_ \| | |/ _ \     \___ \ / _` | |/ _ \/ __|   | |\/| |/ _` | '_ \ / _` | '_ \ / _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|   \___ \| | | / __| __/ _ \ '_ ` _ \  
        | |  | | (_) | |_) | | |  __/     ____) | (_| | |  __/\__ \   | |  | | (_| | | | | (_| | | | | (_| |  __/ | | | | |  __/ | | | |_    ____) | |_| \__ \ ||  __/ | | | | | 
        |_|  |_|\___/|_.__/|_|_|\___|    |_____/ \__,_|_|\___||___/   |_|  |_|\__,_|_| |_|\__,_|_| |_|\__, |\___|_| |_| |_|\___|_| |_|\__|  |_____/ \__, |___/\__\___|_| |_| |_| 
                                                                                                      __/  |                                         __/ |
                                                                                                     |____/                                         |____/'''+Fore.LIGHTBLUE_EX)

def payouts(Serial_Number,Mobile_Name,Model_Number,IMEINumberr,Specification,Quantityy,Price,BuyersName,Address,AadharNumber):
    f=open('payouts.csv','a', newline='')
    #heading_list=['Serial_Number','IMEINumberr','Mobile_Name','Model_Number','Specification','Quantity','Price','BuyersName','Address','Quantity','AadharNumber','Purchase Date']
    #print(rec_lis)
    entry=[Serial_Number,Mobile_Name,Model_Number,IMEINumberr,Specification,Quantityy,int(Price)*int(Quantityy),BuyersName,Address,AadharNumber,date.today()]
    lis=[]
    lis.append(entry)
    csvw=csv.writer(f)
    #csvw.writerow(heading_list)
    csvw.writerows(lis)

    f.close()
    print('Entry also done')
    time.sleep(1)
    input()
    maincode()   

def availablephonelist():
    mydb = mysql.connector.connect(
    host="localhost",
    user="bishal",
    password="bishal"
    )

    mycursor = mydb.cursor()
    mycursor.execute('CREATE DATABASE IF NOT EXISTS SHOP_PROJECT')
    mycursor.execute('USE SHOP_PROJECT')
    mycursor.execute("CREATE TABLE IF NOT EXISTS Payouts (Serial_Number VARCHAR(10000) , Mobile_Name VARCHAR(40) , Model_Number VARCHAR(10) , Specification VARCHAR(20) , Quantitiy INTEGER(50), Price INTEGER)")
    mycursor.execute("SELECT * FROM Payouts")
    data=mycursor.fetchall()
    print(tabulate(data, headers=['Serial No.','Mobile Name','Model Number','Specification','Quantity','Price',], tablefmt='psql'))
    mycursor.close()

def loginsss(username):
    fff=open('logins.txt','a') 
    a="Name :--> "+str(username)+"   Date :--> "+str(togetdate())+"   Time :--> "+str(togettime())
    fff.write(a)
    fff.write('\n')
    fff.close()
            
def addnewphone():
    mydb = mysql.connector.connect(
    host="localhost",
    user="bishal",
    password="bishal"
    )
    print(Fore.RESET+'')
    Serial_Number=(input('                    ENTER SERIAL NUMBER      :'))
    Mobile_Name=input('                    ENTER BRAND NAME    :')
    Model_Number=input('                    ENTER MODEL NUMBER        :')
    Specification=input('                    SPECIFICATION    :')
    Quantity=(input('                    ENTER QUANTITY       :'))
    Price=(input('                    ENTER PRICE (rupee)      :'))

    text="INSERT INTO Payouts VALUES('"+Serial_Number+"','"+Mobile_Name+"','"+Model_Number+"','"+Specification+"',"+Quantity+","+Price+")"
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS SHOP_PROJECT")
    mycursor.execute('USE SHOP_PROJECT')
    mycursor.execute("CREATE TABLE IF NOT EXISTS Payouts (Serial_Number VARCHAR(10000) , Mobile_Name VARCHAR(40) , Model_Number VARCHAR(10) , Specification VARCHAR(20) , Quantitiy INTEGER(50), Price INTEGER)")
    mycursor.execute(text)
    mydb.commit()
    mycursor.close()
    print('                    Added Successfully.....')
    time.sleep(1)
    maincode()

def purchase():
    ask=input(Fore.LIGHTMAGENTA_EX+'                    Want to Buy A Phone,Type For [ YES-->Y / NO--> N ] : ')
    if ask in  ("y","Y"):
            print('                    ****************')
            o=input('                    Enter Your Choiced Serial Number :')
            mydb = mysql.connector.connect(
            host="localhost",
            user="bishal",
            password="bishal"
            )
            mycursor = mydb.cursor()
            mycursor.execute('USE SHOP_PROJECT')
            mycursor.execute('CREATE TABLE IF NOT EXISTS Payouts')
            mycursor.execute("SELECT * FROM Payouts")
            data=mycursor.fetchall()
            for row in data:
                if row[0] == o :
                    Serial_Number,Mobile_Name,Model_Number,Specification,Quantity,Price=row
                    BuyersName=input('                    ENTER PURCHASER NAME        :')
                    IMEINumberr=input('                    ENTER Mobile IMEI Number        :')
                    Quantityy=input('                    ENTER QUANTITY       :')
                    Address=input('                    ENTER ADDRESS    :')
                    AadharNumber=input('                    ENTER AADHAR NUMBER        :')
                    print()
                    print('                    Thank You....')
                    print('                    Generating Invoice')
                    time.sleep(2)
                    
                    mydb = mysql.connector.connect(
                    host="localhost",
                    user="bishal",
                    password="bishal"
                    )
                    a="UPDATE payouts SET Quantitiy = Quantitiy-"+Quantityy+" WHERE Serial_Number='"+o+"'"
                    

                    mycursor = mydb.cursor()
                    mycursor.execute('USE SHOP_PROJECT')
                    mycursor.execute(a)
                    mydb.commit()
                    mycursor.close()
                    today = date.today()
                    name=str(row[1])+' '+str(row[2])

                    invoice(BuyersName,AadharNumber,today,name,row[3],Quantityy,row[5])

                    
                    payouts(Serial_Number,Mobile_Name,Model_Number,IMEINumberr,Specification,Quantityy,Price,BuyersName,Address,AadharNumber)
                    
                    
                    input()
                    
                else:
                    print('                    No match Found...')
                    print('                    Try Again')
                    time.sleep(1)
                    maincode()
                    
    else:
        maincode()

def sales():
    df = pandas.read_csv('payouts.csv')
    print(Fore.LIGHTBLUE_EX+'                    ------------------------------------------------------------------------------------------------------------------------')
    print()
    print(df)
    print('                    ------------------------------------------------------------------------------------------------------------------------'+Fore.GREEN)
    print()
    input()

def f():
            print()
            print('                   <--- Got Into New User Menu --->')
            print()
            username=input("                    Enter Your Username     -> ")
            password=pwinput.pwinput(prompt='                    Enter Your Password -> : ', mask='X')
            login(username,password)

def login(username,password):
    with open ('password.dat','rb') as Myfile:
        c=0
        l=0
        while True:
            try:
                a=pickle.load(Myfile)
                if a[0]==username and a[1]==password:
                    print()
                    print('                    Access granted')
                    l=l+1
                    loginsss(username)

                else:
                    c=c+1
                    l=l+1

            except EOFError:
                break

    if c==l:
        print('                    No user found')  
        print('                    User Not Found')
        print()
        print('                    Please..Try..Again..!')
        print()
        f()  

def invoice(Customename,phonenumber,purchasedate,mobilename,Specification,Quantity,Price):
    print()
    print(Fore.RESET+"""                                                                   INVOICE
                        -------------------------------------------------------------------------------------------------------
                            Customer Name:   {:<15}                                      Invoice Date:   {}
                            AADHAR Number:   {:<15}                                      Invoice Time:   {}
                            Purchase Date:   {}
                        -------------------------------------------------------------------------------------------------------
                            Item Name                               Quantity                                  Price Per Unit
                        -------------------------------------------------------------------------------------------------------""".format(Customename,date.today(),phonenumber,datetime.now().strftime("%H:%M:%S"),purchasedate))
    print("""                        {:<30}|                           {:<19} |               {:<0}/-
                        -{:<29}|                                               |
                                                      |                                               |
                                                      |                                               |
                        -------------------------------------------------------------------------------------------------------
                                                                                            Net Payable Amount = ₹ {} /-
                        -------------------------------------------------------------------------------------------------------

    """.format(mobilename,Quantity,Price,Specification,int(Price)*int(Quantity)))
    
def admin():
    os.system("cls")
    cmd = 'mode 100,30'
    os.system(cmd)
    colorama.init()
    print(Fore.LIGHTRED_EX+'                                        ADMIN PANEL')
    print()
    print(Fore.LIGHTYELLOW_EX+' 1. Remove All Mobile Frome Stocks')
    print(' 2. See All Login Sessions ')
    print(" 3. See All User's And Pasword")
    print(' 4. Delete All Login Sessions')
    print(' 5. Remove All Users ')
    print(' 6. Return To Back Menu ')
    print('')

    choice=input(Fore.LIGHTBLUE_EX+"Enter Your Choice  ---->")
    if (choice)=='1':
        print(Fore.RESET+'Okay You Selected - 1. Remove All Mobile Frome Stocks ---> ')
        mydb = mysql.connector.connect(
            host="localhost",
            user="bishal",
            password="bishal"
            )
        mycursor = mydb.cursor()
        mycursor.execute('USE SHOP_PROJECT')
        mycursor.execute("CREATE TABLE IF NOT EXISTS Payouts (Serial_Number VARCHAR(10000) , Mobile_Name VARCHAR(40) , Model_Number VARCHAR(10) , Specification VARCHAR(20) , Quantitiy INTEGER(50), Price INTEGER)")
        mycursor.execute('TRUNCATE TABLE Payouts')
        print('Succesfully Cleared Records...')
        time.sleep(2)
        admin()
    
    elif (choice)=='2':
        print(Fore.RESET+'Okay You Selected - 2. See All Login Sessions ')
        print('---------------------------------------------------------------------')
        print(Fore.WHITE+'')    
        with open('logins.txt','r') as f:
            for i in f:
                print(i)
        print('---------------------------------------------------------------------')
        print()
        
        input('Press Enter To Continue -->')
        admin()
    elif (choice)=='3':
        print(Fore.RESET+"Okay You Selected - 3. See All User's And Pasword" )
        print()
        credit=input('Enter Your Unique Verification code -->  ')
        print()
        print('---------------------------------------------------------------------')
        if credit=='XYZ':
            with open('password.dat','rb') as f:
                while True:
                    try:
                        rec=pickle.load(f)
                        print(Fore.LIGHTMAGENTA_EX+'Password :-> {:<15} | Username :-> {:<10}'.format(rec[1],rec[0]))
                    except EOFError:
                        break
            f.close()
            print(Fore.RESET+'---------------------------------------------------------------------')
            input()
            admin()

        else:
            print('Invalid Uniques Verification code')
            time.sleep(1.5)
            admin()

    
    elif(choice)=='4':
        print(Fore.RESET+"Okay You Selected - 4. Delete All Login Sessions" ) 
        with open("logins.txt",'w') as f:
            a=1
            f.close()
            print('Deleted All Login Sessions..')
            time.sleep(2)
            admin()
        
    elif (choice)=='5':
        print(Fore.RESET+"Okay You Selected - 4. Remove All Users" ) 
        with open("password.dat",'w') as f:
            a=1
            f.close()
            print('Removed All Users..')
            time.sleep(2)
            admin()

    elif (choice)=='6':
        maincode()
    else :
        print('                    Invalid entry')
        time.sleep(1)
        admin()

def maincode():
    cmd = 'mode 160,30'
    os.system(cmd)
    colorama.init()
    print(Fore.GREEN+'''                 
\t\t\t\t\t\t\t█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀
\t\t\t\t\t\t\t▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄             ''')
    print()
    print('\t\t                    1. Available Mobiles', end='         ')
    print('\t\t                    2. Add Mobiles To Stock')
    print('\t\t                    3. Sales Item record',end='         ')
    print('\t\t                    4. Search For Customer')
    print('\t\t                    5. ADMINISTRATOR COMMANDS', end='         ')
    print('\t\t                    6. Quit')
    print('')
    choice=(input('                    Enter Your Choice : '))
    if (choice) == '1':
        print('                    Okay You Selected - 1. Available Mobiles --->'+Fore.RESET)
        availablephonelist()
        purchase()
    elif (choice) == '2':
        print('                    Okay You Selected - 2. Add Mobiles To Stock ---> ')
        addnewphone()
    elif (choice) == '3':
        print('                    Okay You Selected - 3. Sales Item record ---> ')
        sales()
        maincode()
    elif (choice) == '4':
        print('                    Okay You Selected -4. Search For Customer --->')
        e=input('                    Enter IMEI Number :')
        print()
        f=open('payouts.csv','r')
        csw=csv.reader(f)
        c=0
        for i in csw:
            if i[3]==e:
                print('                    Got It..',)
                print(Fore.RESET+'                    ---------------------------------')
                c=c+1
                a=True
                while a:
                    print('                    Serial Number -->',i[0])
                    print('                    Buyers Name -->',i[7])
                    print('                    Aadhar Number -->',i[9])
                    print('                    IMEI Number -->',i[3])
                    print('                    Purchase Date -->',i[10])
                    print('                    Mobile Name -->',i[1])
                    print('                    Model Number -->',i[2])
                    print('                    Specifications -->',i[4])
                    print('                    Quantity -->',i[5])
                    print('                    Price -->',i[6])
                    print('                    Address -->',i[8])
                    print('                    ---------------------------------'+Fore.GREEN)
                    a=False
                    
            else:
                continue
            input()
            maincode()

        if c==0:
            print('                    No Customer Is Found..')
            input()
            maincode()
        
        f.close()
    elif (choice)=='5':
        print('                    Okay You Selected -5. ADMINISTRATOR COMMANDS --->')
        print(Fore.LIGHTWHITE_EX+'                    Loading Commands...')
        admin()
        
    
      
    elif (choice)=='6':
        print()
        print('                    Okay You Selected -6. Quit --->')
        print()
        print(Fore.LIGHTWHITE_EX+'                    CLosing The Application In 2 Seconds.')
        time.sleep(0.5)
   
    else:
        print('                    Invalid Entry...Try Again')
        input()
        maincode()    



#####################__main__##################



intro()
introdetail()

print()
time.sleep(1)
new=input("                    Are You An Existing User...?,Type For [ YES-->Y / NO--> N ] : ")
if new in ("y","Y","N","n"):
    if new in  ("y","Y"):
        f()
        print('                    Everything Looks Good For Now')
        print()
        for i in tqdm(range(3)):
           time.sleep(0.5)
        os.system("cls")
        time.sleep(1)
        maincode()

        
    else:
        print('                    Creating new new id')
        username=input('                    Enter New User Name :')
        password=input('                    Enter New Password :')
        with open('password.dat','ab') as Myfile:
            record=[username,password]        
            pickle.dump(record,Myfile)
            print('                    Welcome...!')
            print('                    Registration Done...')
            print('                    Please Login Again.....')
            print()
            Myfile.close()
            f()
        maincode()
        


else:
    print()
    print("                    Not A Recognised Command.....!")
    print('                    Shutting Down the App in ->2-seconds')
    time.sleep(2)
    
    
    









