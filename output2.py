import pandas as pd

# Read the CSV file
df = pd.read_csv("output.csv")

# Query the data for issues assigned to David and select storyPoints
david_story_points = df[df['assignee'] == 'David']['storyPoints']

# Save the result to output.txt with the user query
with open('output.txt', 'w') as f:
    f.write(f"User Query: story points of all issues assigned to David\n")
    f.write(f"Result:\n{david_story_points.to_string()}\n")

