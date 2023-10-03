import os
import openai
import json
import gradio as gr

from dotenv import load_dotenv
from hotel import search_hotels  
from hotel import format_hotel_info

load_dotenv(dotenv_path="openai.env")

# Model
text_model = "gpt-4-32k"

# Setup parameters
openai.api_type = os.environ["OPENAI_API_TYPE"]
openai.api_key = os.environ["OPENAI_API_KEY_ALL"]
openai.api_base = os.environ["OPENAI_API_BASE_ALL"]
openai.api_version = os.environ["OPENAI_API_VERSION_ALL"]


"""messages= [
    {"role": "user", "content": "Hi"}
]

messages= [
    {"role": "user", "content": "Find beachfront hotels in San Diego for less than $300 a month with free wifi."}
]
"""

functions= [  
    {
        "name": "search_hotels",
        "description": "Retrieves hotels from the search index based on the parameters provided",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location of the hotel (i.e. Seattle)"
                },
                "max_price": {
                    "type": "number",
                    "description": "The maximum price for the hotel"
                },
                "features": {
                    "type": "string",
                    "description": "A comma separated list of features (i.e. beachfront, free wifi, etc.)"
                }
            },
            "required": ["location"]
        }
    }
]  

def get_gptanswer(user_question):
    messages= [
    {"role": "user", "content": user_question}
    ]
    response = openai.ChatCompletion.create(
        engine=text_model,
        messages=messages,
        functions=functions,
        function_call="auto", 
    )
    print(user_question)
    response_message = response["choices"][0]["message"]
    print(response["choices"][0]["message"])

    if not response_message.get("function_call"):  
        return (response_message["content"]) # print the model response
    else: # the model wants to call a function
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = search_hotels(**function_args)
        
        # Add the assistant response and function response to the messages
        messages.append( 
            response_message
        )
        print(response_message)
        messages.append( 
            {
                "role": "function",
                "name": "search_hotels",
                "content": function_response,
            }
        ) 
        #print(messages.pop()["content"]) # print the function response
        formatted_info = format_hotel_info(messages.pop()["content"])  
        print(formatted_info)
        return (formatted_info)  



with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message=get_gptanswer(message)
        chat_history.append((message, bot_message))
        
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()
 



    