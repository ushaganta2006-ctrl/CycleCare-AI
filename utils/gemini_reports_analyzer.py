from google import genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)



def analyze_report(image):

    prompt = """
    You are an expert medical report interpreter specializing in:

    - Women's Health
    - PCOS
    - PCOD
    - CBC Reports
    - Iron Profiles
    - Thyroid Reports
    - Vitamin Reports
    - Ultrasound Reports

    Analyze the uploaded report.

    Return ONLY valid JSON.

    JSON Format:

    {
      "patient_information":{
        "name":"",
        "age":"",
        "gender":""
      },

      "reports_analysis":[
        {
          "report_type":"",
          "findings":[],
          "abnormalities":[]
        }
      ],

      "summary":"",

      "pcos_relevance":"",

      "health_score":0,

      "recommendations":[]
    }
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                prompt,
                image
            ]
        )

        result = response.text.strip()

        if result.startswith("```json"):
            result = result.replace("```json", "")
            result = result.replace("```", "")

        return json.loads(result)

    except Exception as e:

        return {
            "error": str(e)
        }