import pandas as pd

# Read the CSV file
df = pd.read_csv("output.csv")

# Count the number of issues assigned to each sprint
sprint_issue_counts = df.groupby('sprint').size()

# Prepare the output string
output = f"User Query: the individual number of issues assigned to each sprint\n{str(sprint_issue_counts)}"

# Save the output to a text file
with open('output.txt', 'w') as f:
    f.write(output)
