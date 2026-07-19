import os
import json
import google.generativeai as genai
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-flash-latest")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Waste2Wealth AI backend is running!"}


@app.post("/analyze-waste")
async def analyze_waste(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    prompt = """
    You are an AI system for an industrial waste reuse platform called Waste2Wealth AI.
    Look at this image of waste material and respond ONLY with valid JSON (no markdown, no extra text) in this exact format:

    {
      "waste_type": "short name of the material, e.g. Metal Scrap, Plastic Waste, E-waste, Textile Waste, Paper/Cardboard, Organic Waste",
      "condition": "short description of condition/quality, e.g. Clean and reusable, Mixed/contaminated, Good quality",
      "estimated_quantity_note": "a short guess like 'appears to be a small batch' since exact weight isn't provided",
      "reuse_suggestions": [
        "specific industry or product this waste could be reused for/as, e.g. Can be reused by metal fabrication units as raw input",
        "another specific reuse idea",
        "a third reuse or value-added product idea"
      ],
      "recommended_recycling_method": "short recommendation, e.g. Mechanical recycling, Shredding and pelletizing, etc.",
      "estimated_price_per_kg_inr": a number (just the number, your best estimate in Indian Rupees per kg based on material type),
      "carbon_saved_kg_per_kg_waste": a number (your best estimate of CO2 emissions saved in kg, per kg of this waste type, if reused instead of landfilled)
    }

    Only output the JSON object, nothing else.
    """

    response = model.generate_content([prompt, image])

    text = response.text.strip()
    text = text.replace("```json", "").replace("```", "").strip()

    try:
        result = json.loads(text)
    except:
        result = {"error": "Could not parse AI response", "raw_response": text}

    return result