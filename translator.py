import requests


def translate_sentence(text,from_lang  = "en" , to_lang = "pl"):
    url = "https://translate-all-languages.p.rapidapi.com/translate"

    querystring = {"toLang":to_lang,"text":text,"from_lang":from_lang}

    headers = {
	    "X-RapidAPI-Key": "33d19b0ba4msh6961e768da698b7p1b9858jsn4951b04ddafc",
	    "X-RapidAPI-Host": "translate-all-languages.p.rapidapi.com"
    }

    try:

        response = requests.get(url, headers=headers, params=querystring).json()
        print(response)



        if response['status'] != 200:
            raise Exception('Status code is not 200!')

        return response['translatedText']
    except Exception as e:
        print('Conncection failed' , "Sorry but we cannot successfully retrieve translated sentence")
#mozna bez 25 linijki

