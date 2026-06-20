from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_food_image(image):
    prompt = """
    You are an expert nutritionist specializing in PCOS and PCOD.

    Analyze the uploaded food image.

    Tasks:

    1. Identify every visible food item.
    2. Estimate portion size.
    3. Estimate calories, protein, carbs, fats and fiber for EACH item.
    4. Calculate total nutrition.
    5. Generate a PCOS suitability score from 0-100.
    6. Mention whether the meal is:
       - Excellent
       - Good
       - Moderate
       - Poor

    7. Warn if there are:
       - Junk foods
       - Sugary foods
       - High calorie foods
       - Refined carbs
       - Low protein
       - Low fiber

    8. Recommend improvements.

    9. Identify nutrients that appear insufficient for a PCOS-friendly meal.

        Examples:
        - Protein
        - Fiber
        - Iron
        - Omega-3
        - Vitamin D

Return them in "missing_nutrients".

    Return ONLY valid JSON.

    Format:

    {
        "food_items":[...],

        "total_nutrition":{...},

        "pcos_score":0,

        "assessment":"",

        "warnings":[],

        "missing_nutrients":[],

        "recommendations":[]
    }
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            prompt,
            image
        ]
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)