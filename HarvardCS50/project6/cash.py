quarter = 25
dime = 10
nickel = 5
penny = 1

def calculate_coinTotal(change, coin_value):
    return change // coin_value 

def main():
    while True:
        change = int(input("Change: "))
        if 0 <= change <= 99:
            break
    
    #calculating the coins
    quarters = calculate_coinTotal(change, quarter)
    change %= quarter
    
    dimes = calculate_coinTotal(change, dime)
    change %= dime

    nickels = calculate_coinTotal(change, nickel)
    change %= nickel

    pennies = calculate_coinTotal(change, penny)
    change %= penny

    #calculating + printing total # of oins
    total_coins = int(quarters + dimes + nickels + pennies)
    print(f"Total Coins Owed: {total_coins}")
    print("==================================")
    print(f"Number of Quarters: {quarters}")
    print(f"Number of Dimes: {dimes}")
    print(f"Number of Nickels: {nickels}")
    print(f"Number of Pennies: {pennies}")

main()