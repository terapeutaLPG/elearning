import requests
import os
from dotenv import load_dotenv
load_dotenv()
# nazwa zmiennej(nie moze miec kropek) = wartosc
#
open_translator_key = os.getenv("API_KEY")
print('Test')
print(open_translator_key)

# print(os.getenv('test'))
# #api_key = "PeFxNqHP04GTmKCl5sTumqXFO2CRR3paGnghGO3m"
# url= "https://quizapi.io/api/v1/questions -G"
#
# headers  ={
#     'apiKey':"PeFxNqHP04GTmKCl5sTumqXFO2CRR3paGnghGO3m", #api key
#      "limit": 10 #ilosc pytan 10
# }
#
#
# response=requests.get("https://quizapi.io/api/v1/questions",headers).json()
#
# print(response)

"""ukryc kod moze przez from dotenv"""


# curl https://quizapi.io/api/v1/questions -G \
# -d apiKey=YOUR_API_KEY \
# -d limit=10
# https://quizapi.io/docs/1.0/overview
