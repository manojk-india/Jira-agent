import pandas as pd
df = pd.read_csv("generated_files/output.csv")

# Calculate the number of story points assigned to Rishika
rishika_story_points = df[df['assignee'] == 'Rishika']['story_points'].sum()

# Save the result to output.txt
with open('generated_files/output.txt', 'w') as f:
    f.write(f"User Query: Number of story points assigned to Rishika\n")
    f.write(f"Result: {rishika_story_points}")
