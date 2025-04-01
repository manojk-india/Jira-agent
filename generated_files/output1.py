import pandas as pd  
df = pd.read_csv("generated_files/new_custom.csv")  

# Filter the DataFrame for issues assigned to David in Sprint 8  
df_filtered = df[(df['assignee'] == 'David') & (df['sprint'] == 'Sprint 8')]  

# Save the filtered DataFrame to output.csv  
df_filtered.to_csv('generated_files/output.csv', index=False)  
