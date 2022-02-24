import math


def number_of_monthly_payments(loan_principal, monthly_payment_value, loan_interest):
    nominal_interest_rate = (loan_interest / 100) / 12
    number_of_payments = math.log(monthly_payment_value /
                                  (monthly_payment_value - (nominal_interest_rate * loan_principal)),
                                  (1 + nominal_interest_rate))
    number_of_payments_rounded_up = math.ceil(number_of_payments)
    years = number_of_payments_rounded_up // 12
    months = number_of_payments_rounded_up - (years * 12)
    if number_of_payments_rounded_up < 12:
        if months == 1:
            print('It will take 1 month to repay this loan!')
        else:
            print(f'It will take {months} months to repay this loan!')
    elif number_of_payments_rounded_up == 12:
        print(f'It will take 1 year to repay this loan!')
    elif number_of_payments_rounded_up % 12 == 0:
        print(f'It will take {years} years to repay this loan!')
    elif number_of_payments_rounded_up > 12:
        if years == 1 and months == 1:
            print('It will take 1 year and 1 month to pay this loan!')
        elif years > 1 and months == 1:
            print(f'It will take {years} years and 1 month to pay this loan!')
        elif years > 1 and months > 1:
            print(f'It will take {years} years and {months} months to repay this loan!')


def annuity_monthly_payment_amount(loan_principal, number_of_periods, loan_interest):
    nominal_interest_rate = (loan_interest / 100) / 12
    annuity_monthly = loan_principal * (nominal_interest_rate * (1 + nominal_interest_rate) ** number_of_periods) / \
                      ((1 + nominal_interest_rate) ** number_of_periods - 1)
    print(f'Your monthly payment = {math.ceil(annuity_monthly)}')


def calculate_loan_principal(annuity_payment, number_of_periods, loan_interest):
    nominal_interest_rate = (loan_interest / 100) / 12
    loan_principal = annuity_payment / ((nominal_interest_rate * (1 + nominal_interest_rate) ** number_of_periods) / \
                     ((1 + nominal_interest_rate) ** number_of_periods - 1))
    print(f'Your loan principal = {round(loan_principal)}')


def main():
    what_to_calculate = input('What do you want to calculate?\n'
                              'type "n" for number of monthly payments,\n'
                              'type "a" for annuity monthly payment amount,\n'
                              'type "p" for loan principal: ')

    if what_to_calculate == "n":
        loan_principal = int(input('Enter the loan principal: '))
        monthly_payment_value = int(input('Enter the monthly payment: '))
        loan_interest = float(input('Enter the loan interest: '))
        number_of_monthly_payments(loan_principal, monthly_payment_value, loan_interest)

    elif what_to_calculate == "a":
        loan_principal = int(input('Enter the loan principal: '))
        number_of_periods = int(input('Enter the number of periods: '))
        loan_interest = float(input('Enter the loan interest: '))
        annuity_monthly_payment_amount(loan_principal, number_of_periods, loan_interest)

    elif what_to_calculate == "p":
        annuity_payment = float(input('Enter the annuity payment: '))
        number_of_periods = int(input('Enter the number of periods: '))
        loan_interest = float(input('Enter the loan interest: '))
        calculate_loan_principal(annuity_payment, number_of_periods, loan_interest)


if __name__ == '__main__':
    main()
