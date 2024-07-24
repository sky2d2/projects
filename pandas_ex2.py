import pandas as pd

df = pd.read_csv("D:\python_work\projects\kaggle_datasets\chipotle.tsv", sep = '\t')
#print(df)
print(df.head())

# First 10 entries
print(df.head(10))

# Total number of observations in the dataset
num_observations = df.shape[0]
print('Total number of observations:', num_observations)
print(len(df))
#print(df.shape)

# Total number of columns in the dataset
print(f"Total number of columns: {df.shape[1]}")

# Print the name of all the columns
print("Column names:")
col_names = df.columns
for i in col_names:
    print(i)

# How is dataset indexed?
index_type = type(df.index).__name__
print(f"Index : {index_type}")

# Which was the most-ordered item?
item_quantities = df.groupby('item_name')['quantity'].sum()
most_ordered_item = item_quantities.idxmax()
print("The most-ordered item is:", most_ordered_item)

#  For the most-ordered item, how many items were ordered?
item_quantities1 = df.groupby('item_name')['quantity'].sum()
num_items_ordered = item_quantities1.max()
print(f"For {most_ordered_item}, {num_items_ordered} units were ordered.")

# What was the most ordered item in the choice_description column?
item_quantities3 = df.groupby('choice_description')['quantity'].sum()
most_choice = item_quantities3.idxmax()
num_of_choice = item_quantities3.max()
print("Choice Description for most ordered item: ",most_choice)
print(num_of_choice, "units sold")

#  How many items were orderd in total?
total_orders = df['quantity'].sum()
print(f"Total number of items ordered: {total_orders}")

# Turn item_price to float
df['item_price'] = df['item_price'].apply(lambda x: float(x.replace('$','')))
type = df['item_price'].dtype
print(type)

# How much was the revenue for the period in the dataset?

revenue = (df['quantity'] * df['item_price']).sum()
print(f"The revenue is ${revenue}.")

# Total number of orders
total_orders = df['order_id'].nunique()
print("Total num of orders:",total_orders)

# Average revenue amount per order
avg_revenue = round((revenue / total_orders),2)
print(f"The average revenue amount per order is ${avg_revenue}")

# Total different items sold
item_sold = df['item_name'].nunique()
print("Total number of different items sold:",item_sold)




