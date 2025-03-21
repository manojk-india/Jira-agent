import pandas as pd
df = pd.read_csv("new_custom.csv")
df_filtered = df[df['assignee'] == 'David']
df_filtered.to_csv('output.csv', index=False)
