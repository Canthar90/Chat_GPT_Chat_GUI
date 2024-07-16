import openai
from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()

special_key = os.getenv("SECRET_KEY")

# openai.base_url = "http://localhost:3040"
# OpenAI.base_url = "http://localhost:3040"

openai.api_key = 'anything'
openai.base_url = "http://localhost:3040/v1"

class Chatbot:
    def __init__(self):
        self.client = OpenAI(
            base_url="http://localhost:3040/v1",
            api_key=special_key,
            organization=os.getenv('ORG_SETTING'),
            project=os.getenv('PROJ_SETTING'),

            )
        pass
        

    def get_response(self, user_input):
        
        completion = self.client.chat.completions.create(
             model="gpt-3.5-turbo-0125",
             messages=[
            {"role": "user", "content": "How do I list all files in a directory using Python?"},
             ],
        )

        return(completion)
    

if __name__ == '__main__':
    chatbot = Chatbot()
    response = chatbot.get_response("Write joke about birds")
    print(response)