import pandas as pd

sheet_path = r"C:\Users\Divya\Downloads\China expansion - KeyValues(1-500).csv"
dest_path =r'.\data\China 501-end titlecased.csv'

df = pd.read_csv(sheet_path)

print(df['Metric Heading'].unique())

for i in range(len(df)):
    if isinstance(df.at[i,'Metric Heading'], str):
        df.at[i, 'Metric Heading'] = ' '.join(x if x.lower() != 'by' else x.lower() for x in df.at[i, 'Metric Heading'].title().split())

df.to_csv(dest_path, index=False)
