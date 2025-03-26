import pandas as pd

df = pd.read_csv("generated_files/output.csv")

# Count FTE and FTC utilization
fte_count = (df["employee_type"] == "FTE").sum()
ftc_count = (df["employee_type"] == "FTC").sum()

# Create a summary string
summary = f"Count of FTE utilization: {fte_count}\nCount of FTC utilization: {ftc_count}"

# Save the results to output.txt
with open("generated_files/output.txt", "w") as f:
    f.write(f"User Query: Count of FTE/FTC utilization\n{summary}")

print("Analysis completed. Results saved to generated_files/output.txt")
