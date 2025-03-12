import pandas as pd
df = pd.read_csv("output.csv")

# Filter rows where assignee is David and sum the storyPoints
total_story_points = df[df['assignee'] == 'David']['storyPoints'].sum()

# Save the result to output.txt along with the query
with open('output.txt', 'w') as f:
    f.write(f"User Query: Total number of story points assigned to David\n")
    f.write(f"Total Story Points: {total_story_points}")
