import pandas as pd

# Read the CSV file
df = pd.read_csv("generated_files/output.csv")

# Filter data for Sprint 8
sprint_8_df = df[df['sprint'] == 'Sprint 8']

# Calculate total story points for Apoorva and Rishika
apoorva_points = sprint_8_df[sprint_8_df['assignee'] == 'Apoorva']['story_points'].sum()
rishika_points = sprint_8_df[sprint_8_df['assignee'] == 'Rishika']['story_points'].sum()

# Create a formatted string with the results
result = f"User Query: Total story points assigned to Apoorva and Rishika separately in Sprint 8\n"
result += f"Apoorva: {apoorva_points} story points\n"
result += f"Rishika: {rishika_points} story points"

# Save the result to output.txt
with open("generated_files/output.txt", "w") as f:
    f.write(result)
