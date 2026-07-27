# Quick and discreet gemini assistant

A discreet, background-running Windows assistant powered by the Google Gemini API. This tool allows you to quickly analyze copied text and displays short, concise answers via a customizable notification.

# Features
* **Background operation:** A global hotkey (`Ctrl+Shift+Z`) triggers text analysis from within any application.
* **Clipboard integration:** The script automatically fetches the text from your clipboard and copies the generated response back to it.
* **Rate Limit Handling:** Built-in safeguards against multiple keystrokes.
* **System Instructions:** A pre-configured system prompt that forces short and specific responses from the model.

# Instructions
1) Install Python libraries listed in `requirements.txt` file.
2) Generate an API key at [aistudio.google.com](https://aistudio.google.com/). Paste it into the `apikey` variable in the `QuickAssistant` script.
3) Check which model is available for your key by running the `ModelCheck` script or by visiting [https://aistudio.google.com/rate-limit?timeRange=last-hour](https://aistudio.google.com/rate-limit?timeRange=last-hour).
4) (Optional) Modify the content of the `instruction` variable if you need to adjust the AI's behavior.
5) Change the `model_name` variable to the one available for your account.
6) Run the script and you're ready to go!
7) To use it, simply copy your query to the clipboard (`Ctrl+C`), and then press the hotkey (`Ctrl+Shift+Z`).
8) (Optional) If you want to see full Gemini's response just use `Ctrl+V` in any text space (like notebook).

