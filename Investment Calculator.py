
print("INVESTMENT CALCULATOR")
print("Select an option:")
print("1. ANY")
print("2. LISA")
print(" ")

def calculate_investment(initial, years, rate, depositType, contribution, compound, contribute_at_beginning):
    rate /= 100  # Convert percentage to decimal
    total = initial
    c=0
    
    if depositType:
        for year in range(1, years + 1):
            c=c+1
    
            if contribute_at_beginning:
                total += contribution  # Contribution at the start of the year
    
            total *= (1 + rate / compound) ** compound  # Apply compound interest
            print("year",c,"- £", round(total, 2))
    
            if not contribute_at_beginning:
                total += contribution  # Contribution at the end of the year
                print("year",c,"- £",round(total, 2))
    
        return round(total, 2)
    
    elif not depositType:
        for year in range(1, years + 1):
            c=c+1

            if contribute_at_beginning:
                total += contribution  # Contribution at the start of the year

            total *= (1 + rate / compound) ** compound  # Apply compound interest
            print("year",c,"- £", round(total, 2))

            if not contribute_at_beginning:
                total += contribution  # Contribution at the end of the year
                print("year",c,"- £",round(total, 2))

        return round(total, 2)
        

def ANY():
    try:
        initial = float(input("Enter your initial investment: "))
        years = int(input("Enter number of years investment is for: "))
        rate = float(input("Enter rate of return (% per year): "))
        
        depositType = input("deposit monthly or yearly (m or y)").strip().lower() == "y"
        if depositType:
            contribution = float(input("Enter additional yearly contribution: "))
        if not depositType:
            contribution = 12 * float(input("Enter monthly contribution: "))
            
        compoundType = input("Enter whether interest is compounded monthly or yearly (m or y): ").strip().lower() == "y"
        if compoundType:
            compound = 1
        if not compoundType:
            compound = 12
            
        contribute_at_beginning = input("Contribute at the beginning of each year? (yes/no): ").strip().lower() == "yes"

        final_amount = calculate_investment(initial, years, rate, depositType, contribution, compound, contribute_at_beginning)
        print(f"Final investment value after {years} years: £{final_amount}")
    except ValueError:
        print("Invalid input. Please enter numbers correctly.")

def LISA():
    try:
        initial = float(input("Enter your initial investment: "))
        years = int(input("Enter number of years investment is for: "))
        rate = float(input("Enter rate of return (% per year): "))
        
        depositType = input("deposit monthly or yearly (m or y)").strip().lower() == "y"
        if depositType:
            contribution = float(input("Enter additional yearly contribution (max £4,000 due to LISA limits): "))
        if not depositType:
            contribution = 12 * float(input("Enter monthly contribution (max £333 due to LISA limits): "))
            
        compoundType = input("Enter whether interest is compounded monthly or yearly (m or y): ").strip().lower() == "y"
        if compoundType:
            compound = 1
        if not compoundType:
            compound = 12
        
        contribute_at_beginning = input("Contribute at the beginning of each year? (y/n): ").strip().lower() == "y"

        if contribution > 4000:
            print("LISA contributions cannot exceed £4,000 per year. Adjusting to £4,000.")
            contribution = 4000

        bonus = contribution * 0.25  # LISA 25% government bonus
        contribution += bonus

        final_amount = calculate_investment(initial, years, rate, depositType, contribution, compound, contribute_at_beginning)
        print(f"Final investment value after {years} years: £{final_amount}")
    except ValueError:
        print("Invalid input. Please enter numbers correctly.")

choice = input("Enter option: ").strip()

if choice == "1":
    print(" ")
    ANY()
elif choice == "2":
    print("")
    LISA()
else:
    print("Invalid selection.")
