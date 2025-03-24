import pandas as pd
df = pd.read_csv("generated_files/output.csv")

# Filter the dataframe where assignee is Sanjay and calculate sum of storyPoints
sum_sanjay_story_points = df[df['assignee'] == 'Sanjay']['storyPoints'].sum()

# Save the result to output.txt along with the user query
with open('generated_files/output.txt', 'w') as f:
    f.write(f"User Query: sum of all story points of Sanjay\n")
    f.write(f"Result: {round(sum_sanjay_story_points, 2)}")
