#!/user/bin/env python3

#Display greeting

print("Congratulations on making your first step towards buying your dream home")


#prompt user input for the property asking price (enter the price between $50,000-$15,000,000):



#def listedPrice():

listedPrice = int(input("Please enter the listed price for your target property, between the range of $50,000 - $15,000,000. Listed Price: $"))
if 50000 < listedPrice < 15000000:
    print("The target property is listed for $ " + str(listedPrice)) 
else:
    print("You entered an unlikely price, please re-enter a price between $50,000 and $15,000,000")

#if __name__ == "__main__":
 #   listedPrice()

