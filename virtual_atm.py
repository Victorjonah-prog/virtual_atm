# virtual atm
balance = 10000
count = 0
while count < 5:
	ussd = input("enter ussd code:\n")
	if ussd != "*556#":
		print ("invalid command try again")
	else:	
		
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
		if command == 5:
			break		
		if command == 1:
				
			airtime = int(input("enter amount of airtime to recharge:\n"))
			num = int(input("enter phone number:\n"))
			if airtime > balance:
				print("amount greater than {balance}")
			else:
				print(f"you recharged {airtime} to {num}")
				balance -= airtime
				print(f"your new balance is {balance}")
		if command == 2:
			print(''' 1. 1gb for 300
				  2. 2gb for 500
				  3. 3gb for 1000 

			''')
			data = int(input("enter command:\n"))
			if data < 1 or data > 3:
				print("invalid command")
				
			if data == 1:
				numb = int(input("enter phone number:\n"))
				print(f"you just recieved 1gb data to {numb}")
				balance -= 300
				print(f"your new balance is {balance}")
			if data == 2:
				numb = int(input("enter phone number:\n"))
				print(f"you just recieved 2gb data to {numb}")
				balance -= 500
				print(f"your new balance is {balance}")
			if data == 3:
				numb = int(input("enter phone number:\n"))
				print(f"you just recieved 1gb data to {numb}")
				balance -= 1000
				print(f"your new balance is {balance}")
	


					                                                 
		if command == 3:
			print('''
		       	1. borrow airtime
		       	2. borrow data

		       	''')
			borrow = int(input("enter command:\n"))	
			if borrow < 1 or borrow > 2:
				print("invalid command")
			if borrow == 1:
				airtime_borrow = int(input("enter amount of card you want to borrow:\n"))
				aritime_num = int(input("enter phone number:\n"))
				print(f"you borrowed {airtime_borrow} of airtime")
			
				if borrow == 2:
					data_borrow = int(input("enter amount of data you want to borrow:\n"))
					data_num = int(input("enter phone number:\n"))
					print(f"you borrowed {data_borrow} of data")
		if command == 4:
			print(f"your account balance is {balance}")
			break  
				

		



