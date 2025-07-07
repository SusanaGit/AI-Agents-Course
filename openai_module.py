from dotenv import load_dotenv
import os
from openai import OpenAI

# load environment variables
load_dotenv()

# create an instance of the OpenAI class
openai = OpenAI(os.getenv("OPENAI_API_KEY"))

