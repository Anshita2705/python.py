#Check if a Number is Even or Odd

number=int(input("Enter a number: "))
if number%2==0:
    print(number,"is even number")
else:
    print(number,"is odd number")


#Sum of Integers from 1 to 50 Using a Loop
sum=0
for i in range(1,50):
    sum=sum+i
print("the sum of numbers from 1 to 50 is ",sum)
