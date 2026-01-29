#data composition module

# in data composition module we check:
# 1. the structure of the data set (row and columns)
# 2. the presence of missing values
# 3. basic statistics (mean, median, mode, std, etc.)
# 4. the data type of each feature/column
import pandas as pd
import seaborn as sns
# Load a sample dataset


df = sns.load_dataset('tips')
print(df)




