import pandas as pd
df = pd.read_csv("generated_files/new_custom.csv")

# Filter for entries where board is CDF and employee_type is either FTE or FTC
cdf_entries = df[(df['board'] == 'CDF') & (df['employee_type'].isin(['FTE', 'FTC']))]

# Save the filtered DataFrame to output.csv
cdf_entries.to_csv('generated_files/output.csv', index=False)
