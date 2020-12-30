#!/usr/bin/env python
# coding: utf-8
import requests
from FASTAG.clearscr import clear as clear
from FASTAG.otpgen import OTP as OTP

url = "https://www.fast2sms.com/dev/bulk"
headers = {
'authorization': "ZJloIiF3AhbUdWnkDfaTepqm2js7BYMVSPyL4C9NzK8xGQR5gcQMFAfTXaungkvBG9OHymIZwqEVYD1h",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}


class User(object):
    name = ''
    ph_no = ''
    balance = 0
    password = ''
    reg_no = ''
    v_type = ''
    def __init__(self, name, ph_no, password, reg_no, v_type):
        self.name = name
        self.ph_no = ph_no
        balance = 0
        self.password = password
        self.reg_no = reg_no
        self.v_type = v_type
        
    def add_bal(self, bal):
        self.balance = self.balance + bal
    def show_bal(self):
        if bal >= 0 :
            print("Your balance is: ", balance)
        else:
            print("Your balance is: ", balance,'\n') 
            print ("Please recharge")
    def change_pass(self, password):
        self.password = password
    def update_name(self, name):
        self.name = name
    



class Police(object):
    username = ''
    password = ''
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def change_pass(self, password):
        self.password = password 




class Toll(object):
    start = ''
    exit = ''
    name = ''
    tri_wheeler = 0
    car = 0
    truck = 0
    def __init__(self, start, exit, tri_wheeler, car, truck):
        self.start = start
        self.exit = exit
        self.tri_wheeler = tri_wheeler
        self.car = car
        self.truck = truck
        self.name = self.start + ' ' + self.exit
    
    def show():
        print (self.start, '_',self.exit, " : fine = ", fine) 




#Challan rates
bike1 = bike2 = bike3 = bike4 = 0
tri_wheel1 = tri_wheel2 = tri_wheel3 = tri_wheel4  = 0
car1 = car2 = car3 = car4 = 0
truck1 = truck2 = truck3 = truck4 = truck5 = 0
admin_pass = 'admin'
dic_user = {}
dic_police = {}
dic_toll = {}



def Update_Fine():
    choice1 = '1'
    while choice1 != '0':
        
        choice1 = input("1. Bike\n2. 3 wheeler\n3. Light motor vehicle\n4. Heavy Vehicle \n0. Back\n")
        clear()
        if choice1 == '1':
            choice2 = input("\n1. No Parking\n2. Overspeeding\n3. Jumping red light\n4. No helmet\n0. Back\n")
            clear()
            if choice2 == '0':
                continue
       
            elif choice2 == '1':
                global bike1
                bike1 = int(input("\nEnter fine amount: \n"))
           
            elif choice2 == '2':
                global bike2
                bike2 = int(input("\nEnter fine amount: \n"))
        
            elif choice2 == '3':
                global bike3
                bike3 = int(input("\nEnter fine amount: \n"))
            
            elif choice2 == '4':
                global bike4
                bike4 =int(input("\nEnter fine amount: \n"))
        
            else:
                print("Invalid choice")
                continue
            input()
            clear()
            
        elif choice1 == '2':
            print("\n1. No Parking\n2. Overspeeding\n3. Jumping red light\n4. Fare meter not installed/working\n0. Back\n")
            choice2 = input()
            clear()
            if choice2 == '0':
                continue
       
            elif choice2 == '1':
                global tri_wheel1
                tri_wheel1 = int(input("\nEnter fine amount: \n"))
           
            elif choice2 == '2':
                global tri_wheel2
                tri_wheel2 = int(input("\nEnter fine amount: \n"))
        
            elif choice2 == '3':
                global tri_wheel3
                tri_wheel3 = int(input("\nEnter fine amount: \n"))
            
            elif choice2 == '4':
                global tri_wheel4
                tri_wheel4 =int(input("\nEnter fine amount: \n"))
        
            else:
                print("Invalid choice")
                continue
            input()
            clear()
            
        elif choice1 == '3':
            print("\n1. No Parking\n2. Overspeeding\n3. Jumping red light\n4. No seatbelt\n0. Back\n")
            choice2 = input()
            clear()
            if choice2 == '0':
                continue
       
            elif choice2 == '1':
                global car1
                car1 =int(input("\nEnter fine amount: \n"))
           
            elif choice2 == '2':
                global car2
                car2 = int(input("\nEnter fine amount: \n"))
        
            elif choice2 == '3':
                global car3
                car3 =int(input("\nEnter fine amount: \n"))
            
            elif choice2 == '4':
                global car4
                car4 = int(input("\nEnter fine amount: \n"))
        
            else:
                print("Invalid choice")
                continue
            input()
            clear()
            
        elif choice1 == '4':
            print("\n1. No Parking\n2. Overspeeding\n3. Jumping red light\n4. No seatbelt\n5. Overloading\n0. Back\n")
            choice2 = input()
            clear()
            if choice2 == '0':
                continue
       
            elif choice2 == '1':
                global truck1
                truck1 = int(input("\nEnter fine amount: \n"))
           
            elif choice2 == '2':
                global truck2
                truck2 =int(input("\nEnter fine amount: \n"))
        
            elif choice2 == '3':
                global truck3
                truck3 =int(input("\nEnter fine amount: \n"))
            
            elif choice2 == '4':
                global truck4
                truck4 =int(input("\nEnter fine amount: \n"))
            
            
            elif choice2 == '5':
                global truck5
                truck5 = int(input("\nEnter fine amount: \n"))
            input()
            clear()
                
        elif choice1 == '0':
            return
        else:
            print("Invalid choice")
            input()
            clear()
            continue
    




def Create_User():
    global dic_user
    type1 = input("Choose vehicle type:\n1. Bike\n2. 3 wheeler\n3. Light motor vehicle\n4. Heavy Vehicle \n0. Back\n")
    if type1 == '0':
        return
    elif type1 == '1':
        type1 = 'bike'
    elif type1 == '2':
        type1 = 'tri_wheeler'
    elif type1 == '3':
        type1 = 'car'
    elif type1 == '4':
        type1 = 'truck'
    else:
        print("Invalid response")
        input()
        return
    ph_no = input("Enter phone_number: ")
    if len(ph_no) == 10:
        pass
    else:
        print("Invalid number")
        input()
        clear()
        return
    print('**Password must be atleast 5 characters in length**')
    password1 = input("Enter Password: ")
    if len(password1) >= 5 :
        pass
    else:
        print('Invalid password')
        input()
        clear()
        return
    password2 = input("Confirm Password: ")
    if password1 != password2 :
        print ("Passwords don't match")
        input()
        return
    dic_user["REG" + ph_no ] = User(input("Enter your name: "), ph_no, password1, "REG" + ph_no, type1)
    print ("Your registration number is: ","REG" + ph_no )
    input()
    




def Create_Police():
    global dic_police
    u_name = input("Enter username: ")
    password1 = input("Enter Password: ")
    password2 = input("Confirm Password: ")
    if password1 != password2 :
        print ("Passwords don't match")
        input()
        return
    dic_police[u_name] = Police(u_name, password1)
    print ("Policeman added")
    input()




def Create_Toll():
    global dic_toll
    start = input("Enter entry point: ")
    exit = input('Enter exit point: ')
    tri_wheeler = input('Enter toll amount for tri_wheeler: ')
    car = input('Enter toll amount for car: ')
    truck = input('Enter toll amount for truck: ')
    dic_toll[start+'_'+exit] = Toll(start, exit, tri_wheeler, car, truck )
    print ("Toll created")
    input()




def Admin():
    global admin_pass
    password = input("Enter password: ")
    if password != admin_pass :
        print ("Wrong Password")
        return
    input1 = '1'
    clear()
    
    while input1 != 0:
        
        input1 = input("1. Update_fine\n2. Add user\n3. Add policeman\n4.Add tollbooth\n5. Change admin password\n0. Back\n")
        clear()
        if input1 == '0':
            return
        
        elif input1 == '5':
            passw = input("Enter new password: ")
            passw1 = input("Confirm password: ")
            if passw == passw1:
                admin_pass = passw
                print ("Password changed successfully")
                input()
                clear()
            else:
                print ("Passwords don't match")
                input()
                clear()
                continue
            
                
        elif input1 == '1':
            Update_Fine()
            clear()
            continue
            
        elif input1 == '2':
            Create_User()
            clear()
            continue
        
        elif input1 == '3':
            Create_Police()
            clear()
            continue
        
        elif input1 == '4':
            Create_Toll()
            clear()
            continue
        
        else:
            print ("Invalid choice")
            input()
            clear()
            continue
            
    


def Petrol_Amount():
    global dic_user
    reg_no = input("Scan Fastag\n")
    if reg_no in dic_user:
        pass
    else:
        print ("Invalid registration number")
        input()
        clear()
        return
    amount = input("Enter amount: ")
    if dic_user[reg_no].balance >= int(amount) :
        temp_otp = OTP()
        payload = "sender_id=FSTSMS&message="+"OTP is: "+str(temp_otp)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
        response = requests.request("POST", url, data=payload, headers=headers)
        
        if int(input('Enter OTP: ')) == temp_otp :
            pass
        else:
            print ('OTP dont match')
            input()
            clear()
            return
        
        dic_user[reg_no].balance = dic_user[reg_no].balance - int(amount)
        payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
        response = requests.request("POST", url, data=payload, headers=headers)
    else:
        payload = "sender_id=FSTSMS&message="+"Insufficient balance"+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
        response = requests.request("POST", url, data=payload, headers=headers)
    clear()
    return




def Police_Amount():
    global dic_police
    global dic_user
    usrn = input("Enter username: ")
    if usrn in dic_police:
        pass
    else:
        
        print ("Invalid username")
        input()
        clear()
        return
    pwd = input('Enter password: ')
    
    if dic_police[usrn].password == pwd:
        pass
    else:
        print ("Wrong password")
        input()
        clear()
        return
    
    reg_no = input("Scan Fastag\n")
    if reg_no in dic_user:
        pass
    else:
        print ("Invalid registration number")
        input()
        clear()
        return
    
    if dic_user[reg_no].v_type == 'bike':
            choice2 = input("\n1. No Parking\n2. Overspeeding\n3. Jumping red light\n4. No helmet\n5. Back\n")
            clear()
            if choice2 == '1':
                global bike1
                dic_user[reg_no].balance = dic_user[reg_no].balance - bike1
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
           
            elif choice2 == '2':
                global bike2
                dic_user[reg_no].balance = dic_user[reg_no].balance - bike2
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
        
            elif choice2 == '3':
                global bike3
                dic_user[reg_no].balance = dic_user[reg_no].balance - bike3
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
            
            elif choice2 == '4':
                global bike4
                dic_user[reg_no].balance = dic_user[reg_no].balance - bike4
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
            
            elif choice2 == '5':
                clear()
                return
        
            else:
                print("Invalid choice")
                input()
                clear()
                return
            
            
    elif dic_user[reg_no].v_type == 'car':
            choice2 = input("\n1. No Parking\n2. Overspeeding\n3. Jumping red light\n4. No seatbelt\n5. Back\n")
            clear()
            if choice2 == '1':
                global car1
                dic_user[reg_no].balance = dic_user[reg_no].balance - car1
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
           
            elif choice2 == '2':
                global car2
                dic_user[reg_no].balance = dic_user[reg_no].balance - car2
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
        
            elif choice2 == '3':
                global car3
                dic_user[reg_no].balance = dic_user[reg_no].balance - car3
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
            
            elif choice2 == '4':
                global car4
                dic_user[reg_no].balance = dic_user[reg_no].balance - car4
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
            
            elif choice2 == '5':
                clear()
                return
        
            else:
                print("Invalid choice")
                input()
                clear()
                return
            
            
    elif dic_user[reg_no].v_type == 'tri_wheeler':
            choice2 = input("\n1. No Parking\n2. Overspeeding\n3. Jumping red light\n4. Fare meter not installed/working\n5. Back\n")
            clear()
            if choice2 == '1':
                global tri_wheel1
                dic_user[reg_no].balance = dic_user[reg_no].balance - tri_wheel1
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
           
            elif choice2 == '2':
                global tri_wheel2
                dic_user[reg_no].balance = dic_user[reg_no].balance - tri_wheel2
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
        
            elif choice2 == '3':
                global tri_wheel3
                dic_user[reg_no].balance = dic_user[reg_no].balance - tri_wheel3
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
            
            elif choice2 == '4':
                global tri_wheel4
                dic_user[reg_no].balance = dic_user[reg_no].balance - tri_wheel4
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
            
            elif choice2 == '5':
                clear()
                return 
        
            else:
                print("Invalid choice")
                input()
                return
            clear()
            
    elif dic_user[reg_no].v_type == 'truck':
            choice2 = input("\n1. No Parking\n2. Overspeeding\n3. Jumping red light\n4. No helmet\n5. Overloading\n6. Back\n")
            clear()
            if choice2 == '1':
                global truck1
                dic_user[reg_no].balance = dic_user[reg_no].balance - truck1
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
           
            elif choice2 == '2':
                global truck2
                dic_user[reg_no].balance = dic_user[reg_no].balance - truck2
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
        
            elif choice2 == '3':
                global truck3
                dic_user[reg_no].balance = dic_user[reg_no].balance - truck3
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
            
            elif choice2 == '4':
                global truck4
                dic_user[reg_no].balance = dic_user[reg_no].balance - truck4
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
            elif choice2 == '5':
                global truck5
                dic_user[reg_no].balance = dic_user[reg_no].balance - truck5
                payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[reg_no].balance)+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                return
            
            elif choice2 == '6':
                clear()
                return
            
            else:
                print("Invalid choice")
                input()
                return
            clear()
            
    else: 
        print("Invalid response")
        input()
        clear()
        return
            
        



def User_Amount():
    global dic_user
    usrn = input("Enter registration number: ")
    if usrn in dic_user:
        pass
    else:
        print("Invalid Reg. No")
        input()
        clear()
        return
    pwd = input("Enter password: ")
    if pwd == dic_user[usrn].password :
        pass
    else:
        print ("Wrong password")
        input()
        clear()
        return
    
    choice = input('1. Add balance\n2. View balance\n3. Back')
    if choice == '1':
        amount = int(input('Enter amount: '))
        if amount >= 1:
            dic_user[usrn].add_bal(amount)
            payload = "sender_id=FSTSMS&message="+"Your updated balance is: "+str(dic_user[usrn].balance)+'&language=english&route=p&numbers='+dic_user[usrn].ph_no
            response = requests.request("POST", url, data=payload, headers=headers)
            input()
            clear()
            return
        else:
            print('Wrong input')
            input()
            clear()
            return
    elif choice == '2':
        print ("Your balance is: ", dic_user[usrn].balance)
        payload = "sender_id=FSTSMS&message="+"Your balance is: "+str(dic_user[usrn].balance)+'&language=english&route=p&numbers='+dic_user[usrn].ph_no
        response = requests.request("POST", url, data=payload, headers=headers)
        input()
        clear()
        return
    
    elif choice == '3' :
        clear()
        return
    else:
        print ('Invalid choice')
        input()
        clear()
        return
    


def Toll_Amount():
    global dic_toll
    t=1
    for i in dic_toll:
        print (t,'. ',i)
        t = t + 1
    name = ''
    choice3 = int(input())
    t = 1
    for i in dic_toll:
        if t <= choice3:
            name = i
            break
        
        

    clear()
    choice = input('1. Update toll\n2. Toll info\n3. Collect Toll\n4. Back\n')
    clear()
    if choice == '1':
        print ('Enter the toll fares:')
        tri_wheeler = int(input("Three wheeler: "))
        car = int(input('Car: '))
        truck = int(input('Truck: '))
        dic_toll[name].tri_wheeler = tri_wheeler
        dic_toll[name].car = car
        dic_toll[name].truck = truck
        print('Values updated successfully')
        input()
        clear()
        return
    elif choice == '2':
        print ('Toll name: ',dic_toll[name].name,'\n','Tri wheeler: ', dic_toll[name].tri_wheeler, ' \n', 'Car: ',dic_toll[name].car, ' \n' 'Truck: ', dic_toll[name].truck, ' \n' )
        input()
        return
    elif choice == '3':
        global dic_user
        reg_no = input("Scan Fastag\n")
        if reg_no in dic_user:
            pass
        else:
            print ("Invalid registration number")
            input()
            clear()
            return
        if dic_user[reg_no].v_type == 'bike':
            print("No toll for bike")
            input()
            clear()
            return
        elif dic_user[reg_no].v_type == 'car':
            if dic_user[reg_no].balance >= dic_toll[name].car :
                pass
            else:
                print ("Insufficient balance")
                payload = "sender_id=FSTSMS&message="+"Insufficient balance"+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                input()
                clear()
                return
            dic_user[reg_no].balance = dic_user[reg_no].balance - dic_toll[name].car
            payload = "sender_id=FSTSMS&message="+"Updated balance is:"+ str(dic_user[reg_no].balance) +'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
            response = requests.request("POST", url, data=payload, headers=headers)
            print ("Updated balance is: ", dic_user[reg_no].balance)
            input()
            clear()
            return
        elif dic_user[reg_no].v_type == 'tri_wheeler':
            if dic_user[reg_no].balance >= dic_toll[name].tri_wheeler :
                pass
            else:
                print ("Insufficient balance")
                payload = "sender_id=FSTSMS&message="+"Insufficient balance"+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                input()
                clear()
                return
            dic_user[reg_no].balance = dic_user[reg_no].balance - dic_toll[name].tri_wheeler
            payload = "sender_id=FSTSMS&message="+"Updated balance is:"+ str(dic_user[reg_no].balance) +'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
            response = requests.request("POST", url, data=payload, headers=headers)
            print ("Updated balance is: ", dic_user[reg_no].balance)
            input()
            clear()
            return
        elif dic_user[reg_no].v_type == 'truck':
            if dic_user[reg_no].balance >= dic_toll[name].truck :
                pass
            else:
                print ("Insufficient balance")
                payload = "sender_id=FSTSMS&message="+"Insufficient balance"+'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
                response = requests.request("POST", url, data=payload, headers=headers)
                input()
                clear()
                return
            dic_user[reg_no].balance = dic_user[reg_no].balance - dic_toll[name].truck
            payload = "sender_id=FSTSMS&message="+"Updated balance is:"+ str(dic_user[reg_no].balance) +'&language=english&route=p&numbers='+dic_user[reg_no].ph_no
            response = requests.request("POST", url, data=payload, headers=headers)
            print ("Updated balance is: ", dic_user[reg_no].balance)
            input()
            clear()
            return
        
        
    


def System():
    choice1 = '1'
    while choice1 != '6':
        print ("********************      ********************\n********************FasTag********************\n********************      ********************\n\n")
        choice1 = input("1. User\n2. Police\n3. Toll\n4. Petrol Pump\n5. Admin\n6.EXIT\n")
        if choice1 == '1':
            clear()
            User_Amount()
            continue
        elif choice1 == '2' :
            clear()
            Police_Amount()
            continue
        elif choice1 == '3':
            clear()
            Toll_Amount()
            continue
        elif choice1 == '4':
            clear()
            Petrol_Amount()
            continue
        elif choice1 == '5' :
            clear()
            Admin()
            continue
        elif choice1 == '6':
            exit(0)
        else: 
            print('Invalid choice')
            clear()
            continue
            


System()





