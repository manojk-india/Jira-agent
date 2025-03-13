import pandas as pd
df = pd.read_csv("output.csv")

# Filter the dataframe to only include bugs
bugs_df = df[df['issuetype'] == 'Bug']

# Count the number of bugs issued to each individual
bug_counts = bugs_df['assignee'].value_counts()

# Save the results to output.txt with the user query
with open('output.txt', 'w') as f:
    f.write("User Query: count of bugs issued to each individual\n")
    f.write(f"{bug_counts}")
