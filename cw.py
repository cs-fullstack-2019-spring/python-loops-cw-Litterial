def main():
    def quest1():
        #Print -20 to and including 50. Use any loop you want.

        for x in range(-20,51): # uses range function to print from 20 to 50
            print (x)

    def quest2():
        #Create a loop that prints even numbers from 0 to and including 20.
        for x in range(0,21,2):  #use 3rd parameter of range to skip a number each iteration
            print(x)
    def quest3():
        #Prompt the user for 3 numbers. Then print the 3 numbers along with their average after the 3rd number is entered.
        num1=int(input("Enter a number. "))
        num2=int(input("Enter a number. "))
        num3=int(input("Enter a number. "))
        sum = num1+num2+num3   #uses sum to combine the inputs
        print ("The average of ",num1, " + ",num2, " + ",num3, " is ", sum)

    def quest4():
        password= input("Enter your password.")    #asks for password
        while True:    #an infinite loop. The loop breaks once password and otherpass match.
            otherpass= input ("Re-enter your password. ")
            if (password==otherpass):
                print("The passwords match.")
                break
            else:
                print("The passwords do not match.")
    def FIZZBUZZ():
        x= int(input("Enter a number. ")) #ask for user input
        for x in range (1,x+1):
            if x%3==0 and x%5==0:    #checks to see if the number is divisible by both 3 and 5, prints number and FIZZBUZZ
                print(x,"FIZZBUZZ")
            elif x%3==0:              #checks to see if the number is divisible by 3, prints number and FIZZ
                print(x,"FIZZ")
            elif x%5==0:               #checks to see if the number is divisible by  5, prints number and BUZZ
                print(x,"BUZZ")
            else:
                print(x)





    # quest1()
    # quest2()
    #quest3()
    #quest4()
    FIZZBUZZ()

if __name__ == '__main__':
    main()

