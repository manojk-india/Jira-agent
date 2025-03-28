import pandas as pd
df = pd.read_csv("generated_files/new_custom.csv")
rishika_issues = df[df['assignee'] == 'Rishika']
rishika_issues.to_csv('generated_files/output.csv', index=False)
