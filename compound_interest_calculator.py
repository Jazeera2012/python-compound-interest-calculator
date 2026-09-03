# Compound Interest Calculator
# Store all calculations made during the current session.
history = []

def get_currency():
    while True:
        currency = input("Enter the currency: ").strip()

        if not currency:
            print("❌ Currency cannot be empty!")
        else: 
            return currency

def get_positive_number(prompt, number_type=float):
    while True:
        try:
            value = number_type(input(prompt))

            if value < 0:
                print("❌ Value cannot be nagative!")
            else:
                return value
        except ValueError:
            print("❌ Invalid input! Please enter a number!")

def calculate_compound_interest(principal, rate, time):
    return principal * pow((1 + rate / 100), time)

def show_result(currency, principal, rate, time, total):
    interest_earned = total - principal

    print()
    print("=" * 45)
    print("           📊 Your Results")
    print("=" * 45)

    print(f"Initial Principal: {currency}{principal:,.2f}")
    print(f"Final Balance:     {currency}{total:,.2f}")

    print("=" * 45)

    return interest_earned

def show_history():
    if not history:
        print("\n📜 No calculations have been made yet.")
        return

    print()
    print("=" * 45)
    print("           📜 Calculation History")

    for number, calculation in enumerate(history, start=1):
        print(f"\n{number}.")
        print(
            f"   Initial: {calculation['currency']}"
            f"{calculation['principal']:,.2f}"
        )
        print(f"   Rate: {calculation['rate']:.1f}%")
        print(f"   Time: {calculation['time']} year(s)")
        print(f"   Final: {calculation['currency']}"
        f"{calculation['total']:,.2f}"
        )
    print("=" * 45)

def calculate():
    print()
    print("=" * 45)
    print("      💰 Compound Interest Calculator")
    print("=" * 45)

    currency = get_currency()

    principal = get_positive_number(
        "Enter the principle amount: "
    )
    rate = get_positive_number(
        "Enter the interest rate (%): "
    )
    time = get_positive_number(
        "Enter the time in years: ",
        int
    )

    total = calculate_compound_interest(
        principal,
        rate,
        time
    )

    interest_earned = show_result(
        currency,
        principal,
        rate,
        time,
        total
    )

    history.append({
        "currency": currency,
        "principal": principal,
        "rate": rate,
        "time": time,
        "interest": interest_earned,
        "total": total
    })

def main():
    while True:
        calculate()
        while True:
            again = input(
                "\n🔄 Would you like to calculate again? (y/n): "
            ).strip().lower()

            if again == "yes":
                break
            elif again == "no":
                show_history()
                print(
                    "\n👋🏻 Thanks for using the "
                    "Compound Interest Calculator!"
                )
                return
            else:
                print("❌ Please enter 'yes' or 'no'.")



if __name__ == "__main__":
    main()