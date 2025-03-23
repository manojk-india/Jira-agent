import pandas as pd
df = pd.read_csv("generated_files/output.csv")

# Filter the dataframe where assignee is David and sum the storyPoints
total_points = df[df['assignee'] == 'David']['storyPoints'].sum()

# Save the result to output.txt
with open('generated_files/output.txt', 'w') as f:
    f.write(f"User Query: sum of all story points of David\n")
    f.write(f"Total Story Points: {total_points}")
