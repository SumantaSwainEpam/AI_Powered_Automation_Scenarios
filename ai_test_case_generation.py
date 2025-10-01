
import google.generativeai as genai
import os
from dotenv import load_dotenv
from rich.markdown import Markdown
from rich.console import Console

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

req = "As a user, I want to log into the SauceDemo application using my email and password."

model = genai.GenerativeModel('gemini-2.0-flash')
prompt = "Generate automation test cases based on plain text requirements for the SauceDemo application.\n" + req
response = model.generate_content(prompt)

# Format and print output as Markdown for better readability
console = Console()
console.print(Markdown(response.text))