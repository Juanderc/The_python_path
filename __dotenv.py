

#pip install python-dotenv

import os
from dotenv import dotenv_values, load_dotenv

load_dotenv() #It loads the env variables.
v = os.getenv("secretkey") #It get the variable from the .env file

print(v)