#!/user/bin/env python3

#prompt user input for the property asking price (enter the price between $50,000-$15,000,000):
def enterListedPrice():
    while True:
        try:
            listedPrice =int(input(
                "Please enter the listed price for your target property, between the range of $50,000 - $15,000,000. Listed Price: $"))
        except ValueError:
            print("Input  Error. Please enter number only.")
            continue
        if 50000 < listedPrice < 15000000:
            print("The target property is listed for $ " + str(listedPrice))
            return listedPrice #return act as break out of this loop
        else:
             print("You entered an unlikely price, please re-enter a price between $50,000 and $15,000,000")
# calculate the exact earnest money amount according to the entered percentage
def emCal(emPercentage, lpAmount):
    emExact = emPercentage * lpAmount /100
    return emExact

#prompt for earnest money percentage, return the exact amount (x% of listingPrice)
def earnestMoney(listedPrice):
        while True:
        #using try and except to let program continue to run if entered wrong thing
            try:
                earnestMoney = int(
                    input("Please enter an earnest money percentage amount between 3-100(numbers only. Earnest Money： "))
            except ValueError:
                print("Input  Error. Please enter number only.")
            #using if else to check for int range
            if 2 < earnestMoney < 101:
                print("you are offering " + str(earnestMoney) + "% of earnest money or " + str(emCal(earnestMoney, listedPrice)))
                break
            else:
                print("You entered an unacceptable earnest money amount, please re-enter a number between 3 to 100")


if __name__ == "__main__":
    # Display greeting

    print("Congratulations on making your first step towards buying your dream home")
    listedPrice = enterListedPrice()
    earnestMoney(listedPrice)
