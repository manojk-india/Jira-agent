import pandas as pd
df = pd.read_csv("new_custom.csv")
df_filtered = df[(df['project'] == 'E-Commerce') & (df['assignee'] == 'David')]
df_filtered.to_csv('output.csv', index=False)
