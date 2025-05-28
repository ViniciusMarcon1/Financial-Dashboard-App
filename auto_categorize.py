from google import genai
import os 
import json 
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
google_client = genai.Client(api_key=api_key)

prompt = '''
Task:
You are an AI specialized in semantic understanding and consumer behavior categorization. You will receive a Python list containing unique establishment names. Your task is to analyze each establishment and assign it to the single most appropriate consumer category, returning the result as a JSON object.

Instructions:
For each establishment in the list, determine the single most appropriate consumer category based on common sense, general knowledge, and typical consumer behavior.

Example of potential categories (you may create new ones if justified by the nature of the establishment):
- Housing
- Transportation
- Food
- Utilities
- Health
- Groceries
- Shopping
- Personal Care 
- Education
- Travel
- Income 
Uncategorized (if no suitable category can be determined)

Each establishment must be assigned to only one category—choose the most representative category if an establishment could belong to multiple.
Only include categories in the output JSON that are actually used based on the input list.
Do not create empty categories.

The final output must be a JSON object where:
Keys are the category names.
Values are lists containing the establishments that belong to each category.
If an establishment does not fit into any known or reasonable consumer category, place it under the “Uncategorized” category.

python List:
'''

def auto_categorize_func(some_data, prompt):
    response = google_client.models.generate_content(
        model="gemini-2.0-flash", 
        contents=[
            {
                "role": "user",
                "parts": [{"text": f"{prompt}\n{some_data}"}]
            }
        ]
    )
    return str(response.text)