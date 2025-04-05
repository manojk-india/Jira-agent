import pandas as pd
df = pd.read_csv("generated_files/output.csv")

# Calculate sum of story points assigned to David
david_story_points = df[df['assignee'] == 'David']['story_points'].sum()

# Save the result to output.txt
with open('generated_files/output.txt', 'w') as f:
    f.write(f"Sum of all story points assigned to David: {david_story_points}")
