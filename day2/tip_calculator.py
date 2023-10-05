print("Welcome to tip calculator ")
final_bill=float(input("Please enter your final bill "))
tip=int(input("How Much would you like to tip 10 , 12 , 15 "))
tip=(100+tip)/100
numCustomer=int(input("How Many People to split the bill "))

billDiv=(final_bill/numCustomer)*tip

print(f"Each person should pay:- {billDiv}")