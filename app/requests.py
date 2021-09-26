import urllib.request, json
from app.models import Quote_Body
import random



def get_quotes():

    quotes_api_endpoint = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(quotes_api_endpoint) as url:
        get_quotes_data = url.read()
        randomquotes = json.loads(get_quotes_data)

        

        
        while randomquotes['id'] >=1 and randomquotes['id'] <=44:
            quote_id = random.randint(1,45)
            randomquotes['id'] = quote_id
            return randomquotes