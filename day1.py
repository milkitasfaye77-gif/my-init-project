def split_bill(total, people, tip_rate=0.10):
    """Return total with tip, tip amount, and per-person share."""
    tip = total * tip_rate
    total_with_tip = total + tip
    per_person = total_with_tip / people
    return total_with_tip, tip, per_person


def main():
    bill_total = 1450.00
    people = 4
    tip_rate = 0.10
    names = ["Almaz", "Maya", "Biru", "Sami"]

    total_with_tip, tip_amount, each_share = split_bill(bill_total, people, tip_rate)

    print(f"Bill total: {bill_total:.2f} ETB")
    print(f"Tip rate: {tip_rate*100:.0f}%")
    print(f"Tip amount: {tip_amount:.2f} ETB")
    print(f"Total with tip: {total_with_tip:.2f} ETB")
    print()

    for name in names:
        print(f"{name} pays: {each_share:.2f} ETB")


if __name__ == "__main__":
    main()