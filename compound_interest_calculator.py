# Compound Interest Calculator

# Store all calculations made during the current session.
history = []


def get_currency():
    # Ask the user to enter a currency symbol or code.
    while True:
        currency = input("Enter the currency: ").strip()

        # Make sure the user does not leave the currency empty.
        if not currency:
            print("❌ Currency cannot be empty!")
        else:
            return currency


def get_positive_number(prompt, number_type=float):
    # Keep asking until the user enters a valid number.
    while True:
        try:
            # Convert the user's input into the required number type.
            value = number_type(input(prompt))

            # Do not allow negative values.
            if value < 0:
                print("❌ Value cannot be negative!")
            else:
                return value

        # Handle inputs that cannot be converted into a number.
        except ValueError:
            print("❌ Invalid input! Please enter a number!")


def calculate_compound_interest(principal, rate, time):
    # Calculate the final balance using the compound interest formula.
    return principal * pow((1 + rate / 100), time)


def show_result(currency, principal, rate, time, total):
    # Calculate how much interest was earned.
    interest_earned = total - principal

    # Display the calculation results.
    print()
    print("=" * 45)
    print("           📊 Your Results")
    print("=" * 45)

    print(f"Initial Principal: {currency}{principal:,.2f}")
    print(f"Final Balance:     {currency}{total:,.2f}")

    print("=" * 45)

    # Return the earned interest so it can be stored in history.
    return interest_earned


def show_history():
    # Check whether any calculations have been stored.
    if not history:
        print("\n📜 No calculations have been made yet.")
        return

    print()
    print("=" * 45)
    print("           📜 Calculation History")
    print("=" * 45)

    # Display every calculation stored in the session.
    for number, calculation in enumerate(history, start=1):
        print(f"\n{number}.")
        print(
            f"   Initial: {calculation['currency']}"
            f"{calculation['principal']:,.2f}"
        )
        print(f"   Rate: {calculation['rate']:.1f}%")
        print(f"   Time: {calculation['time']} year(s)")
        print(
            f"   Final: {calculation['currency']}"
            f"{calculation['total']:,.2f}"
        )

    print("=" * 45)


def calculate():
    # Display the calculator title.
    print()
    print("=" * 45)
    print("      💰 Compound Interest Calculator")
    print("=" * 45)

    # Get the currency symbol or code from the user.
    currency = get_currency()

    # Get the principal amount, interest rate, and time.
    principal = get_positive_number(
        "Enter the principal amount: "
    )

    rate = get_positive_number(
        "Enter the interest rate (%): "
    )

    time = get_positive_number(
        "Enter the time in years: ",
        int
    )

    # Calculate the final balance.
    total = calculate_compound_interest(
        principal,
        rate,
        time
    )

    # Display the result and get the interest earned.
    interest_earned = show_result(
        currency,
        principal,
        rate,
        time,
        total
    )

    # Store the calculation in the session history.
    history.append({
        "currency": currency,
        "principal": principal,
        "rate": rate,
        "time": time,
        "interest": interest_earned,
        "total": total
    })


def main():
    # Keep the calculator running until the user chooses "no".
    while True:
        # Run a new compound interest calculation.
        calculate()

        # Ask whether the user wants to calculate again.
        while True:
            again = input(
                "\n🔄 Would you like to calculate again? (yes/no): "
            ).strip().lower()

            if again == "yes":
                # Start another calculation.
                break

            elif again == "no":
                # Show all calculations before exiting.
                show_history()

                print(
                    "\n👋🏻 Thanks for using the "
                    "Compound Interest Calculator!"
                )
                return

            else:
                # Handle invalid yes/no responses.
                print("❌ Please enter 'yes' or 'no'.")


# Run the program only when this file is executed directly.
if __name__ == "__main__":
    main()
