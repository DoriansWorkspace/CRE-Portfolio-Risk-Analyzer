import pandas as pd

portfolio_data = {
    'Asset_Name': ['Luxury Apartments', 'Office Tower', 'Shopping Mall', 'Warehouse Facility'],
    'Loan_Balance': [50000000, 80000000, 120000000, 30000000],
    'Market_Value': [65000000, 75000000, 150000000, 45000000],
    'Net_Operating_Income': [400000, 150000, 800000, 300000],
    'Debt_Service_Payment': [300000, 250000, 600000, 150000]
}

df = pd.DataFrame(portfolio_data)

df['LTV'] = df['Loan_Balance'] / df['Market_Value']
df['DSCR'] = df['Net_Operating_Income'] / df['Debt_Service_Payment']

df['LTV_%'] = (df['LTV'] * 100).round(1).astype(str) + '%'
df['DSCR_Fixed'] = df['DSCR'].round(2)

df['Risk_Watchlist'] = (df['LTV'] > 0.8) | (df['DSCR'] < 1.2)
df['Risk_Watchlist'] = df['Risk_Watchlist'].map({True: 'YES', False: 'No'})

report_cols = ['Asset_Name', 'LTV_%', 'DSCR_Fixed', 'Risk_Watchlist']
print(df[report_cols])

print("\n--- HIGH RISK ALERT ---")
high_risk = df[df['Risk_Watchlist'] == 'YES']
print(high_risk[['Asset_Name', 'Risk_Watchlist']])