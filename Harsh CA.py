print("=================WELCOME TO HARSH CA=======================")
print("    ")
print("    ")

print("please enter required  details to make your account  ")
print("    ")
print("    ")

name =     input("Enter your name :")
print("        ")
username = input("Enter valid username : ")
print("        ")
password = input("set a complex password : ")
print("       ")
print("your account has been created successfully")
print("       ")
print("please log-in to verify that it's you ")
print("    ")
print("    ")
x = input("Enter your username : ")
print("     ")
y = input("Enter your password : ")
print("     ")
while x!=username or y!=password :
    print("             ")
    print("please enter valid username and password ")
    print("             ")
    x = input("Enter your username : ")
    print("             ")
    y = input("Enter your password : ")
    
print("—————————————you have successfully logged in—————————————")
print("      ")
print("**********Let's start your journey with Harsh CA*********")
print("      ")
nm = input("Tell me what you want i call you to be   : ")
print("      ")
print("ok",nm,"i have memorised your nickname for me ")
print("      ")
print("tell me",nm,"which task can i perform for you :")
print("      ")
print("=========================================================")
print("Enter 1 for calculation ")
print("Enter 2 for storing lending money ")
print("Enter 3 for storing savings ")
print("Enter 4 for watching total budget ")
print("Enter 5 for knowing your monthly expenses ")

print("=========================================================")
print("     ")
task = int(input("Enter the task no. whatever you wants to perform : "))
print("     ")
if task ==1:
   
        print("let's start caculation")
        n1 = int(input("please enter the number 1 : "))
        n2 = int(input("please enter the number 2 : "))
        print("================================================")
        print("Enter 1 for addition")
        print("Enter 2 for multiplication")
        print("Enter 3 for substraction")
        print("Enter 4 for division")
        print("Enter 5 for exponention")
        print("Enter 6 for modulas")
        print("Enter 7 for floor division")
        print("================================================")
        choice = eval(input("Enter your choice : "))
        print("= = = = = = = = =  = = = = = = = = = = = = = =")
        if choice == 1:
            print("the addition of",n1,"and",n2,"is : ",n1+n2)
        elif choice == 2:
            print("the multiplication of",n1,"and",n2,"is : ",n1*n2) 
        elif choice == 3:
            print("the substraction of",n1,"and",n2,"is : ",n1-n2)
        elif choice == 4:
            print("the division of",n1,"and",n2,"is : ",n1/n2)
        elif choice == 5:
            print("the exponention of",n1,"and",n2,"is : ",n1**n2)
        elif choice == 6:
            print("the remainder\\modulus of",n1,"and",n2,"is : ",n1%n2)
        elif choice == 7:
            print("the floor division of",n1,"and",n2,"is : ",n1//n2)
        print("= = = = = = = = = = = = = = = = = = = = = = = = = ")
        print("would you like to continue with calculation or exit ,(t/f) : ")
        a = input()
        while a =="t":
            
            
            print("let's start caculation")
            n1 = int(input("please enter the number 1 : "))
            n2 = int(input("please enter the number 2 : ")) 
                                  
            print("=============================================")
            choice = eval(input("Enter your choice : "))
            print("= = = = = = = = =  = = = = = = = = = =  = = = = = = =")
            if choice == 1:
                print("the addition of",n1,"and",n2,"is : ",n1+n2)
            elif choice == 2:
                print("the multiplication of",n1,"and",n2,"is : ",n1*n2) 
            elif choice == 3:
                print("the substraction of",n1,"and",n2,"is : ",n1-n2)
            elif choice == 4:
                print("the division of",n1,"and",n2,"is : ",n1/n2)
            elif choice == 5:
                print("the exponention of",n1,"and",n2,"is : ",n1**n2)
            elif choice == 6:
                print("the remainder\\modulus of",n1,"and",n2,"is : ",n1%n2)
            elif choice == 7:
                print("the floor division of",n1,"and",n2,"is : ",n1//n2)
            
                print("= = = = = = = = = = = = = = = = = = = = = = = = = ")
            print("would you like to continue with calculation or exit ,(t/f) : ")
            a = input()
                
                
if task == 2:
        print("let's start",nm, "to store lending money  ")
        print("  ")
            
        lender = input("Enter the lender name :")
        amount = input("Enter the lended amount : ")
        print("      ")
        lenders = {}
        lenders[lender] = amount
        print(lenders)
        c = input("Would you need to add more or not(y\\n) : ")
        while c == "y":
            
            print("let's start",nm, "to store lending money  ")
            print("  ")
            
            lender = input("Enter the lender name :")
            amount = input("Enter the lended amount : ")
            print("      ")
            lenders[lender] = amount
            print(lenders)
            c = input("Would you need to add more or not(y\n) : ")
            
if task == 3:
         
      
        print("let's start",nm, "to store saving money  ")
        print("  ")
            
        source = input("Enter the source name :")
        money = input("Enter the saved amount : ")
        print("      ")
        savings = {}
        savings[source]  = money
        print(savings)
        c = input("Would you need to add more or not(y\n) : ")
        while c == "y":
            
            print("let's start",nm, "to store savings money  ")
            print("  ")
            
            source = input("Enter the source name :")
            money = input("Enter the saved amount : ")
            print("      ")
            savings[source] = money
            print(savings)
            c = input("Would you need to add more or not(y\n)")
  
if task==4:
    savings = []
    expenses = []
    choice = input("Savings (S) or Expenses (E): ").upper()
    if choice == "S":
        while True:
            amount = int(input("Enter saving amount: "))
            savings.append(amount)
            if input("Add more? (y/n): ").lower() != "y":
               break

        print("Total Savings =", sum(savings))

    elif choice == "E":
        
       
        while True:
            amount = int(input("Enter expense amount: "))
            expenses.append(amount)

            if input("Add more? (y/n): ").lower() != "y":
                
                break

        print("Total Expenses =", sum(expenses))

    else:
         print("Invalid choice")
if task == 5:
    expenses = []

    while True:
        name = input("Expense name: ")
        amount = float(input("Amount: "))

        expenses.append((name, amount))

        choice = input("Add more? (y/n): ")

        if choice.lower() != "y":
            break

    print("\nExpense Report")
    print("===========================================================")

    total = 0

    for name, amount in expenses:
        print(name, ":", amount)
        total += amount

    print("===========================================================")
    print("Total Monthly Expense:", total)