from django.http import HttpResponse
from .models import ALBUMS


def index(request):
    message = "Salut tout le monde !"
    return HttpResponse(message)


def listing(request):
    i = 0
    albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    artists = ["<li>{}</li>".format(album['artists'][0]) for album in ALBUMS]
    message = """<ul>{}{}</ul>""".format("\n".join(albums), "\n".join(artists))
    return HttpResponse(message)
