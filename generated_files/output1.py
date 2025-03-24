import pandas as pd
df = pd.read_csv("generated_files/new_custom.csv")

# Filter the DataFrame for issues assigned to Sanjay
sanjay_issues = df[df['assignee'] == 'Sanjay']

# Save the result to output.csv
sanjay_issues.to_csv('generated_files/output.csv', index=False)
