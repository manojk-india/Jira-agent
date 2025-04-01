import pandas as pd
df = pd.read_csv("generated_files/output.csv")

# Calculate sum of story points for David in Sprint 8
sum_story_points = df[(df['assignee'] == 'David') & (df['sprint'] == 'Sprint 8')]['story_points'].sum()

# Save result to output.txt
with open("generated_files/output.txt", "w") as f:
    f.write(f"User Query: Sum of all story points assigned to David in Sprint 8\n")
    f.write(f"Result: {sum_story_points}")
