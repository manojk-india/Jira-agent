import pandas as pd
df = pd.read_csv("new_custom.csv")

# Filter the DataFrame for issues where project is 'E-Commerce' and priority is 'Critical'
filtered_df = df[(df['project'] == 'E-Commerce') & (df['priority'] == 'Critical')]

# Save the filtered DataFrame to output.csv
filtered_df.to_csv('output.csv', index=False)
