import google.generativeai as genai


class GenAI(object):

    def __init__(self, api_key=""):
        genai.configure(api_key=api_key)
        self.genai = genai.GenerativeModel("gemini-1.5-flash")

    def gen_content(self, q=""):
        return self.genai.generate_content(q).text
