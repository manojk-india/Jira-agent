import pandas as pd
df = pd.read_csv("generated_files/output.csv")

# Calculate sum of story points for David in Sprint 8
david_sprint8_sum = df[(df['assignee'] == 'David') & (df['sprint'] == 'Sprint 8')]['story_points'].sum()

# Save the result to output.txt
with open('generated_files/output.txt', 'w') as f:
    f.write(f"User Query: Sum of all story points assigned to David in Sprint 8\n")
    f.write(f"Result: {david_sprint8_sum}")
