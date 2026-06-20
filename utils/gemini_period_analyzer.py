from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def analyze_period(
    cycle_length,
    symptoms
):

    symptoms_text = (
        ", ".join(symptoms)
        if symptoms
        else "No symptoms"
    )

    prompt = f"""
You are CycleCare AI.

Analyze the following menstrual cycle information.

Cycle Length:
{cycle_length} days

Symptoms:
{symptoms_text}

Instructions:

1. If symptoms suggest possible PCOS:
   - Mention it gently.
   - Recommend relevant tests.
   - Give food recommendations.
   - Give exercise recommendations.
   - Give stress management advice.

2. If symptoms do not suggest PCOS:
   - Congratulate the user.
   - Encourage healthy habits.

3. Keep the response short.

4. Maximum 100 words.

5. Use emojis.

Example:

🌸 Good Going!

Your symptoms currently do not indicate strong signs of PCOS.

Keep:
• Balanced meals
• Good sleep
• Regular exercise

OR

🌸 Some symptoms may be associated with PCOS.

Recommended Tests:
• AMH
• Testosterone
• Pelvic Ultrasound

Tips:
• High-protein diet
• Daily walking
• Stress management
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"""
⚠️ AI Analysis Currently Unavailable

{str(e)}
"""