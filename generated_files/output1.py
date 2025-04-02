import pandas as pd
df = pd.read_csv("generated_files/new_custom.csv")

# Filter for issues in CDF board and Future sprint state
cdf_future_sprints = df[(df['board'] == 'CDF') & (df['sprint_state'] == 'Future')]

# Sort by sprint start date to get the next two sprints
cdf_future_sprints_sorted = cdf_future_sprints.sort_values(by='sprint_start_date')

# Select the top two sprints (next two sprints)
next_two_sprints = cdf_future_sprints_sorted.head(2)

# Save the result to output.csv
next_two_sprints.to_csv('generated_files/output.csv', index=False)
