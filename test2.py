import google.generativeai as genai



x="AIzaSyCDGF67u4Szetf_pUpAdAlNkXMWAi61uhg"
genai.configure(api_key=x)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)