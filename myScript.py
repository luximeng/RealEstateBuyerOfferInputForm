#!/user/bin/env python3

#Display greeting

print("Congratulations on making your first step towards buying your dream home")


#prompt user input for the property asking price (enter the price between $50,000-$15,000,000):




listedPrice =int(input("Please enter the listed price for your target property, between the range of $50,000 - $15,000,000. Listed Price: $"))
while True:
    try:
        print(str("The target property is listed for $ " + listedPrice))
        if 50000 < listedPrice < 15000000:
            break
    except:  
        print("You entered an unlikely price, please re-enter a price between $50,000 and $15,000,000")


