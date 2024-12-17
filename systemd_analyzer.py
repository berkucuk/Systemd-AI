import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langserve import add_routes
from langchain_core.output_parsers import StrOutputParser
import subprocess
import uvicorn
import distro
import pprint
from fastapi.responses import HTMLResponse
import datetime

MAX_LOG_LINES = 100  # Son 100 satır

def check_root():
    if os.getuid() != 0:
        print("You need to have root privileges to run this script!")
        exit(1)

def read_systemd_errors():
    check_root()  # Ensure the script is run as root
    try:
        result = subprocess.run(['journalctl', '-p', '3', '-xb'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            logs = result.stdout.strip()  # Strip to avoid unnecessary blank spaces
            logs_lines = logs.splitlines()  # Satırlara ayır
            # Son 100 satırı al
            return "\n".join(logs_lines[-MAX_LOG_LINES:])
        else:
            print(f"Error reading logs: {result.stderr}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def detect_linux_distro():
    try:
        name = distro.name()  # Gets the name of the distribution
        version = distro.version()  # Gets the version of the distribution
        return f"{name} {version}"
    except Exception as e:
        print(f"An error occurred while detecting Linux distribution: {e}")
        return "Unknown Linux Distribution"

# Load environment variables
load_dotenv()
key = os.getenv("key")

# Ensure API key is available
if not key:
    print("Error: API key not found in .env file")
    exit(1)

# Initialize model
model = ChatGroq(api_key=key, model="llama-3.3-70b-versatile", temperature=0)

# Read system logs
logs = read_systemd_errors()
if not logs:
    print("No logs available or an error occurred while reading logs.")
    logs = "No systemd errors found."

# Detect Linux distribution
distro_name = detect_linux_distro()

# Define system prompt template
system_template = f"""
You are a system administrator who provides solutions to common systemd errors on Linux.
Specifically, provide a clear and actionable solution for systemd errors on {distro_name}.
Do not provide unnecessary details or explanations. Just give the solution in a concise manner.
"""
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", logs)  # Logs will be passed as the input to the AI
])

# Initialize output parser
parser = StrOutputParser()

# Create the chain
chain = prompt_template | model | parser

# Initialize FastAPI app
app = FastAPI(title="System Analysis AI")

result = chain.invoke({"text": logs}) 
pretty_result = pprint.pformat(result)  
print(pretty_result)

current_time = datetime.datetime.now()
file_name = current_time.strftime("%Y-%m-%d_%H-%M-%S.txt")

with open(f"/var/log/Systemd_AI/{file_name}", "w") as file:
    file.write(pretty_result)

print(f"File '{file_name}' has been created.")


@app.get("/analyze_system")
async def analyze_system():
    result = chain.invoke({"text": logs}) 
    pretty_result = pprint.pformat(result)  
    return HTMLResponse(content=f"<pre>{pretty_result}</pre>")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=3131)
