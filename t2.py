import os
from dotenv import load_dotenv

load_dotenv()

pswd = os.getenv('PSWD')
print(pswd)
