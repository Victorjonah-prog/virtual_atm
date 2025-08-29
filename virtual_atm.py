# recharge card app
balance ={"amount": 10000}
counts = {"count":0}
def start():
	while counts["count"] < 5:
		ussd = input("enter ussd code:\n")
		if ussd != "*556#":
			print("invalid command try again!")
			continue
		if ussd == 5:
			break	
		print('''
	     1. Buy airtime
	     2. buy data
	     3. borrow services
	     4. check balance
	     5. stop
               ''')

		command = int(input("enter command:\n"))
		if command < 1 or command > 5:
			print("invalid command")
			continue
		elif command == 5:
			break		
		elif command == 1:
			buy_airtime()
		elif command == 2:
			buy_data()
		elif command ==3:
			borrow_airtime()	
		counts["count"] +=1		


def buy_airtime():
	#balance["amount"] = 10000				
	airtime = int(input("enter amount of airtime to recharge:\n"))
	num = input("enter phone number:\n")
	if  len(num) != 11:
		print("invalid length of number")

	elif airtime > balance["amount"]:
		print(f"amount greater than {balance}")
	else:
		print(f"you recharged {airtime}₦ to {num}")
		balance["amount"] -= airtime
		print(f"your new balance is {balance}")
		



def buy_data():
	print(''' 1. 1gb for 300₦
		  2. 2gb for 500₦
		  3. 3gb for 1000₦ 

		''')
	data = int(input("enter command:\n"))
	if data < 1 or data > 3:
		print("invalid command")
				
	if data == 1:
		numb = input("enter phone number:\n")
		if len(numb) != 11:
			print("invalid length of number")
		
		else:	

			print(f"you just recieved 1gb data to {numb}")
			balance["amount"] -= 300
			print(f"your new balance is {balance["amount"]}")
	if data == 2:
		numb = input("enter phone number:\n")
		if (numb) != 11:
			print("invalid length of number")
		else:	

			print(f"you just recieved 2gb data to {numb}")
			balance["amount"] -= 500
			print(f"your new balance is {balance["amount"]}")
	if data == 3:
		numb = int(input("enter phone number:\n"))
		print(f"you just recieved 3gb data to {numb}")
		balance["amount"] -= 1000
		print(f"your new balance is {balance["amount"]}")
			
	
def borrow_airtime():
		print('''
		1. borrow airtime
		2. borrow data

		''')
		borrow = int(input("enter command:\n"))	
		if borrow < 1 or borrow > 2:
			print("invalid command")
		if borrow == 1:
			airtime_borrow = int(input("enter amount of card you want to borrow:\n"))
			airtime_num = input("enter phone number:\n")
			if len(airtime_num) !=11:
				print("invalid length of number")
				return	
			if airtime_borrow > 5000:
				print("amount cant be greater than 5000")
			else:

				print(f"you borrowed {airtime_borrow} of airtime")
			
		if borrow == 2:
			data_borrow = int(input("enter amount of data you want to borrow:\n"))
			data_num = input("enter phone number:\n")
			if len(data_num) != 11:
				print("invalid length of number")
				return
			if data_borrow > 5000:
				print("amount cant be greater than 5000")
				return
			else:	
				print(f"you borrowed {data_borrow} of data")
'''					
		if command == 4:
			print(f"your account balance is {balance}")
'''			  
start()				

		



