def split_bill(total, people, tip_rate=0.10):
    """Return total with tip, tip amount, and per-person share."""
    tip = total * tip_rate
    total_with_tip = total + tip
    per_person = total_with_tip / people
    return total_with_tip, tip, per_person


def get_float(prompt, default=None):
    while True:
        value = input(prompt).strip()
        if not value and default is not None:
            return default
        try:
            return float(value)
        except ValueError:
            print("Please enter a valid number.")


def get_int(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return int(value)
        except ValueError:
            print("Please enter a valid whole number.")


def main():
    print("TeleBirr Tip Calculator")
    print("------------------------")

    bill_total = get_float("Enter bill total in ETB: ")
    people = get_int("Enter number of people: ")
    tip_rate = get_float("Enter tip rate as a decimal (0.10 for 10%): ", default=0.10)

    names = []
    for i in range(people):
        names.append(input(f"Enter name for person {i + 1}: ").strip() or f"Person {i + 1}")

    total_with_tip, tip_amount, each_share = split_bill(bill_total, people, tip_rate)

    print("\nResults")
    print("-------")
    print(f"Bill total: {bill_total:.2f} ETB")
    print(f"Tip rate: {tip_rate * 100:.0f}%")
    print(f"Tip amount: {tip_amount:.2f} ETB")
    print(f"Total with tip: {total_with_tip:.2f} ETB")
    print()

    for name in names:
        print(f"{name} pays: {each_share:.2f} ETB")


if __name__ == "__main__":
    main()
