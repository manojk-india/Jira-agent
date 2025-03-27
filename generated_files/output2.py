import pandas as pd
df = pd.read_csv("generated_files/output.csv")

# Filter rows where assignee is Alok and sprint is Sprint 6
alok_sprint6 = df[(df['assignee'] == 'Alok') & (df['sprint'] == 'Sprint 6')]

# Calculate sum of story points
story_points_sum = alok_sprint6['story_points'].sum()

# Save results to output.txt
with open('generated_files/output.txt', 'w') as f:
    f.write(f"User Query: sum of all story points assigned to Alok in Sprint 6\n")
    f.write(f"Result: {story_points_sum}")
