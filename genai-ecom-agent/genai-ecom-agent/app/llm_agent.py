import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env for API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the Gemini 2.5 model
model = genai.GenerativeModel("gemini-2.5-flash")

def clean_sql_response(response_text):
    """
    Removes ```sql ... ``` blocks or any triple backtick markdown formatting.
    """
    cleaned = response_text.strip()

    # Remove markdown code blocks
    if cleaned.startswith("```sql"):
        cleaned = cleaned.replace("```sql", "")
    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```", "")
    if cleaned.endswith("```"):
        cleaned = cleaned.replace("```", "")
    
    return cleaned.strip()

def generate_sql(question, schema_hint=""):
    prompt = f"""
You are a SQL data assistant working with SQLite.

Rules:
- Only use columns provided in the schema.
- Do not make up columns like 'product_id' or 'cpc'.
- Use only the exact column names.
- Do NOT return markdown or triple backtick code blocks.
- Return clean, runnable SQL only.

Schema:
{schema_hint}

Question: {question}
"""
    try:
        response = model.generate_content(prompt)
        raw_sql = response.text.strip()
        return clean_sql_response(raw_sql)
    except Exception as e:
        return f"-- Gemini error: {e}"
