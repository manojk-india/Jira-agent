import pandas as pd
df = pd.read_csv("new_custom.csv")

# Filter the DataFrame where 'issuetype' is 'Bug'
bug_issues = df[df['issuetype'] == 'Bug']

# Save the filtered DataFrame to output.csv
bug_issues.to_csv('output.csv', index=False)
