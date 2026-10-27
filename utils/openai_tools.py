from config.settings import OPENAI_API_KEY
import openai
openai.api_key = OPENAI_API_KEY

def call_chat_model(messages, model='gpt-4o'):
    resp = openai.ChatCompletion.create(model=model, messages=messages, max_tokens=512)
    return resp
