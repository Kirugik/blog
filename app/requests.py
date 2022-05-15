import requests,json 
# from .models import Quote

# url = "http://quotes.stormconsultancy.co.uk/random.json"

# def get_quote():
#     """
#     Function to consume http request and return a Quote class instance
#     """
    
#     response = requests.get(url).json() 
    
#     random_quote = Quote(response.get("author"), response.get("quote"))
    
#     return random_quote

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    if response.status_code == 200:
        quote = response.json()
        return quote