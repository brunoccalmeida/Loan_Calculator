loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'

# write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

loan = int(input("Enter the loan principal: "))
what_to_calculate = input('What do you want to calculate?\n'
                          'type "m" - for number of monthly payments,\n'
                          'type "p" - for the monthly payment: ')

if what_to_calculate == "m":
    monthly_payment = int(input('Enter the monthly payment:'))

elif what_to_calculate == "p":
    number_of_months = int(input('Enter the number of months: '))

