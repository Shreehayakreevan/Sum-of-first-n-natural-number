print("Finding sum of first n natural number")
num=int(input("Enter the Number = "))
if num <0:
    print("Negative numbers are not accepted")
else:
    sum=0
    i=num
    #finding the sum
    while(i>0):
        sum+=i
        i-=1
        print(f"sum of first{num} natural number is = ",sum)