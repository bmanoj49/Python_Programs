#reverse_number

user_input=int(input("Enter the number to reverse"))
rev=0
while(user_input > 0):
 dig=user_input%10
 rev=rev*10+dig
 user_input=user_input//10
print("The reversed number is ",rev)
