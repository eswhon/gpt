from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID", "16209450"))
API_HASH = getenv("API_HASH", "a4573c55ebf7c23038b927997447b78d")
BOT_TOKEN = getenv("BOT_TOKEN", "5674000763:AAEXDMIe4_ppn91v-zY-6sTU3w7qEgvYvrc")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
