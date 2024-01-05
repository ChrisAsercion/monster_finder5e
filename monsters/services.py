import requests

def fetch_monsters(request):
    cr = request.GET.get('cr', 1)
    api_url = 'https://api.open5e.com/v1/monsters'
    params = {'cr': cr}
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
      #import pdb; pdb.set_trace()
      return response.json().get('results', [])
    else:
        return None