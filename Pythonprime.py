def prime():
    try:
        if_prime = int(input("Enter a number"))
    except:
        if_prime = int(input("Enter a valid number"))
        divisor = 2
        Prime_Condition = True
        while divisor < if_prime:
            if if_prime % divisor == 0:
                Prime_Condition = False
                break
            elif if_prime % divisor != 0:
                if divisor == if_prime - 1:
                    Prime_Condition = True
            divisor = divisor + 1
        if Prime_Condition == True:
            print(if_prime,"is a prime number")
        else:
            print(if_prime,"is a composite number")
        return(Prime_Condition)

        if_prime = int(input("Invalid input please try again"))
print(prime())
