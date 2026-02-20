import pandas as pd
from helpers import calculate_total, format_currency

df=pd.read_csv('../sales.csv')

#Calculate total for each row
totals=[]
for index, row in df.iterrows():
    total=calculate_total(row['price'],row['quantity'])
    totals.append(total)

#add totals to dataframe(sales-table)
df['total']=totals


#Display with formatted totals 
print("Sales Analysis:")
for index, row in df.iterrows():
    formatted_total=format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

#show grand total
grandtotal=df['total'].sum()
currency_converter=format_currency(grandtotal)
print(f"Grand total is:{currency_converter}")
