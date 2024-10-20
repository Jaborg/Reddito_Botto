import google.generativeai as genai
import os


class AI_Response:

    def __init__(self,reddit_input_text,wrapper_guide):
    
        self.reddit_input_text = reddit_input_text
        self.wrapper_guide  = wrapper_guide

    def configure_genai(self):
        genai.configure(api_key=os.environ["API_KEY"])
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def curate_response(self):
        curated_response = self.wrapper_guide + 'for this text :' + self.reddit_input_text
        return curated_response

    def create_response(self):
        self.configure_genai()
        response = self.model.generate_content(self.curate_response())
        return response.text

