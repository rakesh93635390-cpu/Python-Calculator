#Operation

print("---CALCULATOR---\n")
print("Select Your choice")
print("\nChoice-1:Addition\n",
      "Choice-2:Subraction\n",
      "Choice-3:Multiplication\n",
      "Choice-4:Division")
      
  #Userinput    
choice=int(input("Choose:"))
x=int(input("Enter a First number:"))
y=int(input("Enter a Second number:"))

# Result 
if choice == 1:
    print("Your answer is :",x+y)

elif choice == 2:
        print("Your answer is :",x-y)

elif choice == 3:
        print("Your answer is :",x*y)

elif choice == 4:
        if y == 0:
        
            print("Cannot divide by zero")
        else:    
            print("Your answer is :",x/y)

else:
       print("Invalid Choice")
