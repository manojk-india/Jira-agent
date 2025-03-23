import pandas as pd
df = pd.read_csv("new_custom.csv")

# Filter the DataFrame where assignee is David
david_issues = df[df['assignee'] == 'David']

# Save the filtered DataFrame to output.csv
david_issues.to_csv('datasets/output.csv', index=False)
