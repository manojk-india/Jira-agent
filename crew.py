from crewai import Agent, Task, Crew,LLM
from dotenv import load_dotenv
import os

load_dotenv()

llm = LLM(
    model="sambanova/DeepSeek-R1-Distill-Llama-70B",
    temperature=0.7
)

# user_query = input("Please give us your promt for us to process:")
user_query1 = "Filter the DataFrame to show only the tasks with priority 'High'"
user_query2="All the issues that are assigned to David and have a status of 'In Progress'"
user_query3="All the issues under E-Commerce project those priority is 'Critical'"
dynamic_user=input("enter the query")




df_structure = """
The dataset has the following columns:
- "id": unique identifier
- "key": issue key
- "project": project name
- "summary": summary of project
- "description": description of task
- "status": ["Backlog", "To Do", "In Progress", "Review", "Done"]
- "assignee": assigned person's name
- "reporter": reporter's name
- "priority": ["High", "Medium", "Low", "Critical"]
- "issuetype": ["Story", "Bug", "Task", "Epic"]
- "created": date of creation (YYYY-MM-DD)
- "updated": last update date (YYYY-MM-DD)
- "resolution": ["Fixed", "Won't Fix", "Duplicate", None]
- "labels": labels (list)
- "components": components involved
- "sprint": sprint name
- "sprintId": sprint ID
- "sprintState": ["To Do", "In Progress", "Review", "Done"]
- "sprintStartDate": sprint start date (YYYY-MM-DD)
- "sprintEndDate": sprint end date (YYYY-MM-DD)
- "storyPoints": story points (numeric)
- "epicLink": linked epic
- "rank": rank
"""
prompt = f"""
    You are an expert in Pandas and data analysis. Convert the following natural language request into a valid Pandas DataFrame query.

    DataFrame Structure:
    {df_structure}

    Request: "{dynamic_user}"

    Ensure the output is a valid Pandas query.
    Just give the valid python code ..no extra commenst or print statements needed
    Encapsulate your output with //code start and //code end
    output should be in this format 
    '''
    //code start
    import pandas as pd
    df = pd.read_csv("new_custom.csv")

    // your pandas generated code 
    // code saving it into output.csv
    '''

    """


# Define the CrewAI Agent
agent = Agent(
    role="Pandas Query Agent",
    goal="Generate and execute Pandas queries from user requests.",
    backstory="You are a data expert specializing in analyzing and extracting information from Pandas DataFrames.",
    llm=llm,
    verbose=True,
)

# Define the Task
task = Task(
    description="Convert user queries given in {prompt} into Pandas queries by understanding the dataframe structure given in {prompt} and return the perfectly working queries",
    agent=agent,
    expected_output="A pandas query that filters the DataFrame based on the given prompt.",
)

# Create the Crew
crew = Crew(agents=[agent], tasks=[task])

# Run the agent
result = crew.kickoff(inputs={"prompt": prompt})

with open("panda.py", "w") as f:
    f.write("\n")
    f.write(str(result))
    f.write("\n")

def extract_code_section(input_file, output_file):
    """
    Extracts the lines between '//code start' and '//code end' from a given Python file.
    
    :param input_file: Path to the input Python file.
    :param output_file: Path to save the extracted code.
    """
    inside_code = False
    extracted_lines = []

    with open(input_file, "r", encoding="utf-8") as file:
        for line in file:
            if "//code start" in line:
                inside_code = True
                continue  # Skip the marker line
            elif "//code end" in line:
                inside_code = False
                break  # Stop reading after //code end
            
            if inside_code:
                extracted_lines.append(line)

    with open(output_file, "w", encoding="utf-8") as file:
        file.writelines(extracted_lines)

    print(f"Extracted code saved to: {output_file}")
    os.remove(input_file)
    print(f"Deleted original file: {input_file}")



# Example usage:
extract_code_section("panda.py", "output.py")

os.system("python output.py")
