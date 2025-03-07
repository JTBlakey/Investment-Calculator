
print("INVESTMENT CALCULATOR")
print("Select an option:")
print("1. ANY")
print("2. LISA")
print(" ")

def calculate_investment(initial, years, rate, contribution, compound, contribute_at_beginning):
    rate /= 100  # Convert percentage to decimal
    total = initial
    c=0

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
        contribution = float(input("Enter additional yearly contribution: "))
        compound = int(input("Enter how many times interest is compounded per year (e.g., 1 for annually, 12 for monthly): "))
        contribute_at_beginning = input("Contribute at the beginning of each year? (yes/no): ").strip().lower() == "yes"

        final_amount = calculate_investment(initial, years, rate, contribution, compound, contribute_at_beginning)
        print(f"Final investment value after {years} years: £{final_amount}")
    except ValueError:
        print("Invalid input. Please enter numbers correctly.")

def LISA():
    try:
        initial = float(input("Enter your initial investment: "))
        years = int(input("Enter number of years investment is for: "))
        rate = float(input("Enter rate of return (% per year): "))
        contribution = float(input("Enter additional yearly contribution (max £4,000 due to LISA limits): "))
        compound = int(input("Enter how many times interest is compounded per year (e.g., 1 for annually, 12 for monthly): "))
        contribute_at_beginning = input("Contribute at the beginning of each year? (yes/no): ").strip().lower() == "yes"

        if contribution > 4000:
            print("LISA contributions cannot exceed £4,000 per year. Adjusting to £4,000.")
            contribution = 4000

        bonus = contribution * 0.25  # LISA 25% government bonus
        contribution += bonus

        final_amount = calculate_investment(initial, years, rate, contribution, compound, contribute_at_beginning)
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
