def user_input():
    while True:
        try:
            salary = float(input("Enter the salary: "))
            expense = float(input("Enter expense: "))
            note = input("If any note, enter here... ")

            if salary <= 0 or expense <= 0:
                print("Salary and expense must be positive.")
                continue

            return salary, expense, note

        except ValueError:
            print("That is not valid. Please try again.")


def calculation(salary,expense,note):
    remaining = salary - expense
    percentage = (remaining / salary) * 100

    if percentage >= 80:
        state = "Good"
    elif percentage >= 50:
        state = "Tight"
    else:
        state = "Not Recommended"

    if not note.strip():
        note = "No additional notes for this calculation."

    return {
        "salary": salary,
        "expense": expense,
        "remaining": remaining,
        "percentage": percentage,
        "state": state,
        "note": note
    }


def print_report(report):
    print("\n----- Personal Finance Report -----")
    print(f"Salary: ₹{report['salary']:,.2f}")
    print(f"Expense: ₹{report['expense']:,.2f}")
    print(f"Remaining: ₹{report['remaining']:,.2f}")
    print(f"Savings: {report['percentage']:.2f}%")
    print(f"Status: {report['state']}")
    print(f"Note: {report['note']}")


def main():
    salary, expense, note = user_input()

    report = calculation(salary, expense, note)

    print_report(report)


if __name__ == "__main__":
    main()