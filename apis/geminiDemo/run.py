import sys
import os
import logging
import absl.logging
from dotenv import load_dotenv
from models import translator
from models import interactive

absl.logging.set_verbosity(absl.logging.INFO)

# Initialize logging
logging.basicConfig(level=logging.INFO)
absl.logging.set_verbosity(absl.logging.INFO)

load_dotenv(
    "/Users/ccxn/Documents/workspace/repositories/geminiDemo/conf.yaml"
)
trans = translator.Trnaslator('en')
trans_zh = translator.Trnaslator('zh-tw')


if __name__ == '__main__':
    trans = translator.Trnaslator('en')
    trans_zh = translator.Trnaslator('zh-tw')
    genai = interactive.GenAI(api_key=os.getenv("api_key"))
    q_trans = sys.argv[1]
    rsp = genai.gen_content(q_trans)
    print(rsp)
