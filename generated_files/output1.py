import pandas as pd  
df = pd.read_csv("generated_files/new_custom.csv")  
df_filtered = df[df['assignee'] == 'David']  
df_filtered.to_csv('generated_files/output.csv', index=False)  
