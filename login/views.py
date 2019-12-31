from django.http import HttpResponse
from django.template import loader
import requests 
import yaml

github_url = "https://gist.githubusercontent.com/mmadhavan/dbded03ee898351a7a08afb5a35eadbf/raw/config.py"
server = "prod"

def index(request):
    config_page = requests.get(github_url)
    config = yaml.load(config_page.text.replace(" ", "").replace("\n", ""))
    template = loader.get_template('login/index.html')
    print(config[server])
    context = {
        'show_banner': config[server]['show'],
    }
    return HttpResponse(template.render(context, request))
