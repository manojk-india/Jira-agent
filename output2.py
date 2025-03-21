import pandas as pd
df = pd.read_csv("output.csv")

# Filter rows where assignee is David and sum storyPoints
david_story_points = df[df['assignee'] == 'David']['storyPoints'].sum()

# Save result to output.txt
with open('output.txt', 'w') as f:
    f.write(f"User Query: sum of all story points assigned to David\n")
    f.write(f"Result: {david_story_points}")
