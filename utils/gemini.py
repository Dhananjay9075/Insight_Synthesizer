import google.generativeai as genai
import json
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_insights(feedback_list):
    prompt = f"""
You are an Insight Synthesizer AI. Your job is to read raw user feedback and extract insight cards.

Each insight card must include:
- A short theme title
- 2–5 supporting quotes from the feedback
- An optional sentiment (positive, negative, neutral)

Input (a list of feedback):
{json.dumps(feedback_list, indent=2)}

Output a JSON array in this format ONLY (no explanation):

[
  {{
    "theme": "Theme title",
    "quotes": ["quote1", "quote2", ...],
    "sentiment": "positive | negative | neutral"
  }},
  ...
]
"""
    response = model.generate_content(prompt)
    try:
        response_json = response.text.strip().split("```json")[-1].split("```")[0] if "```json" in response.text else response.text
        result = json.loads(response_json)
    except Exception as e:
        print(f"Parsing error: {e}")
        result = [{"theme": "Error parsing response", "quotes": [], "sentiment": "N/A"}]
    return result
