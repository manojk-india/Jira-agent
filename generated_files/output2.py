import pandas as pd

# Read the CSV file
df = pd.read_csv("generated_files/output.csv")

# Filter for CDF board
cdf_issues = df[df['board'] == 'CDF']

# Get unique future sprints for CDF board and sort them to get the next two sprints
future_sprints = cdf_issues[cdf_issues['sprint_state'] == 'Future']['sprint'].unique()
next_two_sprints = future_sprints[:2]

# Initialize results dictionary
results = {}

# Calculate for each sprint
for sprint in next_two_sprints:
    sprint_df = cdf_issues[(cdf_issues['sprint'] == sprint)]
    
    # Calculate total story points
    total_story_points = sprint_df['story_points'].sum()
    
    # Classify issues based on story points
    underutilized = ((sprint_df['story_points'] < 5).sum())
    healthy = ((sprint_df['story_points'] >= 5) & (sprint_df['story_points'] <= 10)).sum()
    overutilized = ((sprint_df['story_points'] > 10)).sum()
    
    # Store results
    results[sprint] = {
        'total_story_points': total_story_points,
        'underutilized': underutilized,
        'healthy': healthy,
        'overutilized': overutilized
    }

# Create output string
output = "Count of all issues in CDF board for next 2 sprints seperately, classify them as healthy, underutilized and overutilized based on story points:\n\n"
for sprint, metrics in results.items():
    output += f"Sprint: {sprint}\n"
    output += f"Total Story Points: {metrics['total_story_points']}\n"
    output += f"Underutilized: {metrics['underutilized']}\n"
    output += f"Healthy: {metrics['healthy']}\n"
    output += f"Overutilized: {metrics['overutilized']}\n\n"

# Save to output.txt
with open("generated_files/output.txt", "w") as f:
    f.write(output)
