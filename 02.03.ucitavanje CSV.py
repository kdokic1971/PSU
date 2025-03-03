# Load library
import pandas as pd
# Create URL 2
url = 'podaci.csv'
# Load dataset
dataframe = pd.read_csv(url)
# View first two rows
print(dataframe.head(20))