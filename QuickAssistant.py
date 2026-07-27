import keyboard
import pyperclip
import google.generativeai as genai
from plyer import notification

apikey = "YOUR API KEY HERE"
genai.configure(api_key=apikey)

#instructions based on which the algorithm will respond. 
#Change it to suit your needs.
instruction = (
    "Answers: "
    "short, concise and straight to the point. Skip greetings, "
    "farewells and fluff. "
    "Write a few sentences including the answer first and then the explanation. Write answers in language which the question was asked."
)

model = genai.GenerativeModel(
    model_name='gemini-3.5-flash-lite', # <--- change the model here
    system_instruction=instruction
)

isBusy = False

def showNotification(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Stealth Assistant',
        timeout=5
    )

def askGemini():
    global isBusy
    if isBusy:
        return
    try:
        isBusy = True
        text = pyperclip.paste()
        
        if not text or text.isspace():
            print("\n[Error] Clipboard is empty.")
            return

        print("\n[Request sent to Gemini]")
        showNotification("Gemini", "Processing")

        response = model.generate_content(text)
        result = response.text

        pyperclip.copy(result)


        print("GEMINI RESPONSE:")
        print(result)

        shortAnswer = result[:100] + "..." if len(result) > 100 else result
        showNotification("Answer ready", shortAnswer)

    except Exception as e:
        print(f"\n[Execution error]: {e}")
    finally:
        isBusy = False
print("The alogirthm has started")
print("Press ESC in the console to exit.")

keyboard.add_hotkey('ctrl+shift+z', askGemini) 
keyboard.wait('esc')

