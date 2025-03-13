import pandas as pd
df = pd.read_csv("new_custom.csv")

# Filter the DataFrame where issuetype is 'Bug' and assignee is either David or Alice
filtered_df = df[(df['issuetype'] == 'Bug') & (df['assignee'].isin(['David', 'Alice']))]

# Save the filtered DataFrame to output.csv
filtered_df.to_csv('output.csv', index=False)
