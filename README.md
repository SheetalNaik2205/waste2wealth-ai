Waste2Wealth AI ♻️
AI-powered platform that identifies industrial/manufacturing waste from a photo and suggests reuse opportunities, value-added products, pricing, and environmental impact — instead of routing waste straight to a scrap dealer.
Problem
MSMEs generate industrial waste that's typically sold to scrap dealers at low prices, even though the same material could often be reused as input by another industry. There's no discovery layer connecting waste generators to waste reusers.
What It Does

User uploads a photo of waste material
AI (Google Gemini vision model) identifies the waste type and condition
AI suggests specific reuse ideas / value-added products
AI recommends a recycling method
System estimates resale price (₹/kg) and carbon emissions saved

Tech Stack

Backend: Python, FastAPI, Google Gemini API (gemini-flash-latest)
Frontend: HTML, CSS, JavaScript (vanilla)
Deployment: Render (backend), Netlify (frontend)

Live Links

Frontend: https://venerable-arithmetic-b7b0e4.netlify.app
Backend API: https://waste2wealth-backend-y4ix.onrender.com

Run Locally
Backend:
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Create a .env file with:
GEMINI_API_KEY=your_key_here
Then run:
uvicorn main:app --reload
Frontend:
Open frontend/index.html in your browser.
Future Roadmap

Buyer/reuser matching database with location-based search
Automated ESG report generation for MSMEs
Demand prediction and logistics/pickup scheduling
Payment integration