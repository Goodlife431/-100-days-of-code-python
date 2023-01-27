if __name__ == '__main__':
    debt_capital = 1000
    interest_rate = 0.05
    for year in range(11):
        loan_calculator = debt_capital * (1.00 + interest_rate) ** year
        year += 1
        float(loan_calculator)
        result = round(loan_calculator, 2)
        print(f'Year {year - 1} is {result}')