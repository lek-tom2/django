
from django.http import HttpResponse, Http404
from django.template import loader

quotes = {
    "shakespeare": {"content": "I am William the PearShaker"},
    "einstein": {"content": "I love relativity. I love my Relatives i meant"},
    "coehlo": {"content": "Machine steht"}
}

def main(request):
    template = loader.get_template("quotes/index.html")
    context = {
        "nate": "higgers"
    }
    return HttpResponse(template.render(context, request))

def get_author(request, author):
    if author not in quotes:
        HttpResponse("brak autora cie dobija?", status=404)
    print(quotes[author], author)
    context = quotes[author]

    template = loader.get_template("quotes/quotes.html")
    return HttpResponse(template.render(context, request))