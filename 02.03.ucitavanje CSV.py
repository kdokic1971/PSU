# Load library
import pandas as pd
# Create URL
url = 'podaci.csv'
# Load dataset
dataframe = pd.read_csv(url)
# View first two rows
print(dataframe.head(20))