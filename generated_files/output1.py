import pandas as pd
df = pd.read_csv("generated_files/new_custom.csv")

# Filter the DataFrame where assignee is Alok and sprint is Sprint 6
filtered_df = df[(df['assignee'] == 'Alok') & (df['sprint'] == 'Sprint 6')]

# Save the filtered DataFrame to output.csv
filtered_df.to_csv('generated_files/output.csv', index=False)
