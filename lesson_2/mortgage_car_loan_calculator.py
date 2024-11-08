# loan amount

# APR

# loan duration 

# monthly interest rate APR/12
# loan duration in months 

# Add validation for loan duration, make sure it is in an int (years, months) & APR is int

# m = monthly pmt, p = loan amount, j = monthly interest rate, n = loan dur (mo)
# m = p * (j / (1 - (1 + j)**-n))

def get_inputs():
    loan_amount = input("Enter loan amount: ")
    apr = input("Enter the APR: ")
    loan_duration = input("What is the loan term:\n"
                          "Enter with space between year and month"
                          "(E.g. Ten years, 5 months = 10 5): ")
    return loan_amount, apr, loan_duration


def calculate_loan(loan_amount, apr, loan_duration):
    final_loan_amount = float(loan_amount)
    final_monthly_apr = round(int(apr) / 12, 2)
    final_loan_duration = loan_duration.split()
    # Issue with converting year month into months...
    if len(final_loan_duration) == 1: 
        final_loan_duration = int(final_loan_duration[0]) * 12
    else:
        final_loan_duration = (int(final_loan_duration[0]) * 12) + round(int(final_loan_duration[1])/12, 2)
    print(final_loan_duration)
    test = final_monthly_apr / (1 - (1 + final_monthly_apr) ** (-final_loan_duration))
    print(test)
    mortgage = final_loan_amount * test
    return mortgage


# loan_amount, apr, loan_duration = get_inputs()
# answer = calculate_loan(loan_amount, apr, loan_duration)
# print(f'${answer:.2f}')

p = 100000
j = (6/100)/12
n = 120
m = p * (j / (1 - (1 + j) ** (-n)))
print(f'formula: ${m}')
