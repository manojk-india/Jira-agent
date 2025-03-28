import pandas as pd
df = pd.read_csv("generated_files/output.csv")

# Calculate sum of story points assigned to David
story_points_sum = df.loc[df['assignee'] == 'David', 'story_points'].sum()

# Handle potential NaN values
if pd.isna(story_points_sum):
    story_points_sum = 0

# Save results to output.txt
with open("generated_files/output.txt", "w") as f:
    f.write(f"User Query: Sum of all story points assigned to David\n")
    f.write(f"Result: {story_points_sum}")
