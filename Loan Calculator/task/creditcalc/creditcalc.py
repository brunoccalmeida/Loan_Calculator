import math
import argparse
import sys


def differentiated_payment(loan_principal, interest, periods):
    nominal_interest_rate = (interest / 100) / 12
    m = 1
    total_payment = 0
    for _ in range(periods):
        diff_payment = math.ceil((loan_principal / periods) + nominal_interest_rate * \
                       (loan_principal - (loan_principal * (m - 1)) / periods))
        print(f"Month {m}: payment is {diff_payment}")
        total_payment += diff_payment
        m += 1
    overpayment = total_payment - loan_principal
    print(f"\nOverpayment = {overpayment}")


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
    over_payment = (((years * 12) + months) * monthly_payment_value) - loan_principal
    print(f'Overpayment = {math.ceil(over_payment)}')


def annuity_monthly_payment_amount(loan_principal, number_of_periods, loan_interest):
    nominal_interest_rate = (loan_interest / 100) / 12
    annuity_monthly = loan_principal * (nominal_interest_rate * (1 + nominal_interest_rate) ** number_of_periods) / \
                      ((1 + nominal_interest_rate) ** number_of_periods - 1)
    # over_payment = (annuity_monthly * number_of_periods) - loan_principal
    print(f'Your monthly payment = {math.ceil(annuity_monthly)}')
    # print(f'Overpayment = {math.ceil(over_payment)}')


def calculate_loan_principal(annuity_payment, number_of_periods, loan_interest):
    nominal_interest_rate = (loan_interest / 100) / 12
    loan_principal = annuity_payment / ((nominal_interest_rate * (1 + nominal_interest_rate) ** number_of_periods) /
                                        ((1 + nominal_interest_rate) ** number_of_periods - 1))
    print(f'Your loan principal = {round(loan_principal)}')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", type=str)
    parser.add_argument("--payment", type=float)
    parser.add_argument("--principal", type=int)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    parser.add_argument("-m", type=int, default=1)
    args = parser.parse_args()
    list_of_arguments = [args.interest, args.m]
    if args.payment:
        list_of_arguments.append(args.payment)
    if args.principal:
        list_of_arguments.append(args.principal)
    if args.periods:
        list_of_arguments.append(args.periods)
    if not args.type or args.type not in ["diff", "annuity"]:
        print("Incorrect parameters")
        sys.exit()
    elif args.type == "diff" and args.payment:
        print("Incorrect parameters")
        sys.exit()
    elif not args.interest:
        print("Incorrect parameters")
        sys.exit()
    elif len(list_of_arguments) < 4:
        print("Incorrect parameters")
        sys.exit()
    for e in list_of_arguments:
        if e is None:
            continue
        if e < 0:
            print("Incorrect parameters")
    if args.type == "annuity":
        if not args.periods:
            number_of_monthly_payments(args.principal,
                                       args.payment,
                                       args.interest)
        elif not args.principal:
            calculate_loan_principal(args.payment,
                                     args.periods,
                                     args.interest)
        elif not args.payment:
            annuity_monthly_payment_amount(args.principal,
                                           args.periods,
                                           args.interest)

    elif args.type == "diff":
        differentiated_payment(args.principal, args.interest, args.periods)


if __name__ == '__main__':
    main()
