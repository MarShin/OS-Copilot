import tkinter as tk
from tkinter import scrolledtext, END, font as tkFont

from oscopilot import FridayWebAgent
from oscopilot import ToolManager
from oscopilot import FridayWebExecutor, FridayPlanner, FridayRetriever
from oscopilot.utils import setup_config, setup_pre_run
from selenium_utils.create_driver import create_driver
from selenium_utils.reconnect_driver import reconnect_driver

# messages = [
#     {"role": "system", "content": "You are a helpful assistant."},
# ]

# def add_messages(text: str, role: str):
#     if role == 'user':
#         messages.append({"role": "user", "content": text})
#     else:
#         messages.append({"role": "assistant", "content": text})

# # Function to interact with the OpenAI language model and get the chatbot response
# def get_chatbot_response(input_text):
#     add_messages(input_text, 'user')
#     client = openai.OpenAI(base_url=OPENAI_BASE_URL, api_key=OPENAI_API_KEY)
#     response = client.chat.completions.create(
#         model=MODEL_NAME,
#         messages=messages,
#         temperature=0.5
#     )
#     response_text = response.choices[0].message.content.strip()
#     add_messages(response_text, 'assistant')
#     return response_text

args, llm_model, embbed_model = setup_config()

def connect_drvier():
    driver = reconnect_driver()
    if  not driver:
        create_driver()
    return driver

def web_copilot_agent(input_text):
    try:
        # if not args.query:
        args.query = input_text

        task = setup_pre_run(args)
        
        agent = FridayWebAgent(FridayPlanner, FridayRetriever, FridayWebExecutor, ToolManager, config=args)
        connect_drvier()
        agent.run(task=task)
        response_text = "Your task is completed."
        return response_text
    except Exception as e:
        print(f"Error in web_copilot_agent: {e}")
        return "An error occurred while processing your request."

# Function to display the copilot response in the GUI
def show_copilot_response():
    user_input = user_input_box.get("1.0", END).strip()
    user_input_box.delete("1.0", END)

    if user_input.lower() in ["exit", "quit", "bye", "Goodbye"]:
        insert_chat_log("Web Copilot: Goodbye!\n")
        windows.destroy()
        return

    insert_chat_log(f"You: {user_input}\n")
    send_button.config(state=tk.DISABLED)

    response_text = web_copilot_agent(user_input)
    insert_chat_log(f"Web Copilot: {response_text}\n")
    send_button.config(state=tk.NORMAL)

def insert_chat_log(message):
    chat_log.config(state=tk.NORMAL)  # Enable editing to insert text
    chat_log.insert(tk.END, message)   # Insert the message
    chat_log.config(state=tk.DISABLED)  # Disable editing again

# Function to handle key press events
def handle_keypress(event):
    # 12 is the state for Ctrl key pressed
    if (event.state & 0x0004) and event.keysym == 'Return':
        show_copilot_response()

# Main GUI window
windows = tk.Tk()
windows.title("Web Copilot")

# Create a font object
custom_font = tkFont.Font(family="Arial", size=12)  # Change "Helvetica" and size as needed

# Chat log
chat_log = scrolledtext.ScrolledText(windows, width=60, height=20, wrap=tk.WORD, font=custom_font)
chat_log.insert(tk.END, f"Current args: {args}\n{llm_model}\n{embbed_model}\n")
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
chat_log.config(state=tk.DISABLED)  # Make chat_log non-editable

# User input box
user_input_box = scrolledtext.ScrolledText(windows, width=50, height=4, wrap=tk.WORD, font=custom_font)
user_input_box.grid(row=1, column=0, padx=10, pady=10)

# Send button
send_button = tk.Button(windows, width=10, height=4, text="Send", command=show_copilot_response)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Bind the Ctrl + Enter key event
windows.bind('<KeyRelease>', handle_keypress)

# Start the GUI event loop
windows.mainloop()