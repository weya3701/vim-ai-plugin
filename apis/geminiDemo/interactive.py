from models import translator
from models import interactive
from dotenv import load_dotenv
import os

if __name__ == '__main__':
    # load conf
    load_dotenv(
        "/Users/ccxn/Documents/workspace/repositories/geminiDemo/conf.yaml"
    )
    trans = translator.Trnaslator('en')
    trans_zh = translator.Trnaslator('zh-tw')
    genai = interactive.GenAI(api_key=os.getenv('api_key'))

    while True:
        q = input("Hello, 請問有什麼可以幫忙的: ")

        # q_trans = trans.translate(q)

        rsp = genai.gen_content(q)
        # print(trans_zh.translate(rsp))
        print(rsp)
