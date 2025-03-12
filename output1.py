import pandas as pd
df = pd.read_csv("new_custom.csv")

# Filter the DataFrame for issues assigned to David
filtered_df = df[df['assignee'] == 'David']

# Save the filtered DataFrame to output.csv
filtered_df.to_csv('output.csv', index=False)
