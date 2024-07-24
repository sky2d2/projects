import pandas as pd

food = pd.read_csv("D:\python_work\projects\kaggle_datasets\en.openfoodfacts.org.products.tsv", sep="\t",dtype=str, low_memory=False)

print(food.head())
print(food.shape)

# Number of Observations in Dataset
num_observations = food.shape[0]
print("Number of observations:", num_observations)

# Number of Columns in Dataset
num_columns = food.shape[1]
print("Number of columns:", num_columns)

# Print the name of all the columns

print("Column Names:")
for i in food.columns:
    print(i)

# Name of 100th column
col_100_name = food.columns[99]
print("\nThe 100th column name:",col_100_name)

# Type of the observations of the 100th column
import warnings
warnings.filterwarnings("ignore")

col_100_type = food.dtypes[99]
print("\nType of observations in the 100th column:", col_100_type)

# How is the dataset indexed?
index_type = type(food.index)
print("Type of index:", index_type)

# Product name of the 5th observation
product_name_5th = food.iloc[4, 0]  
print("Product name of the 5th observation:", product_name_5th)