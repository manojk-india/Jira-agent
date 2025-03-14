import pandas as pd
df = pd.read_csv("new_custom.csv")

# Filter issues assigned to Sprint 1, Sprint 2, and Sprint 3
df_filtered = df[df['sprint'].isin(['Sprint 1', 'Sprint 2', 'Sprint 3'])]

# Save the filtered DataFrame to output.csv
df_filtered.to_csv('output.csv', index=False)
