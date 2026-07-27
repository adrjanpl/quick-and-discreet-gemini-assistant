import google.generativeai as genai

apikey = "YOUR API KEY HERE"
genai.configure(api_key=apikey)

#first check which model is available for you
#then go to https://aistudio.google.com/rate-limit?timeRange=last-hour
#and check if RPD (requests per day) is satisfactional for a specific model.
availableModels = []
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        availableModels.append(m.name)
        print(f"- {m.name}")

if not availableModels:
    print("\nYour API key does not have access to any text models.")
else:
    print("\nCopy one of the names above without the 'models/' prefix.")