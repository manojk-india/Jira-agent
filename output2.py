import pandas as pd  
df = pd.read_csv("output.csv")  

# Filter rows where assignee is David and sum the storyPoints  
total_points = df[df['assignee'] == 'David']['storyPoints'].sum()  

# Save the result to output.txt with the user query  
with open('output.txt', 'w') as f:  
    f.write(f"User Query: sum of all story points of David\n")  
    f.write(f"Result: {total_points}")  
