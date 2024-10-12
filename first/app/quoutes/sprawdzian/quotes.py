from lib2to3.fixes.fix_input import context

from django.http import HttpResponse, Http404
from django.template import loader

tutorials = {
    "tutorials": [
        "django",
        "gregtechnewhorizonts"
    ],
    "chapters": {
        "django": [
            "intro",
            "paths"
        ],
        "gregtechnewhorizonts": [
            "beginning",
            "steamage",
            "lv",
            "mv",
        ]
    }
}

def main(request):
    template = loader.get_template("quotes/index.html")
    topics_list = ",".join(tutorials["tutorials"])
    context = {
        "tresc": f"Available topics: {topics_list}",
        "tytul": "Available tutorial topics"
    }
    return HttpResponse(template.render(context, request), status=200)


def get_tutorial(request, topic):
    template = loader.get_template("quotes/quotes.html")
    if topic not in tutorials["tutorials"]:
        context = {
            "tytul": "No such tutorial",
            "tresc": f"There is no tutorial for: {topic}",
        }
        return HttpResponse(template.render(context, request), status=404)

    aviable_chapters = ",".join(tutorials["chapters"][topic])
    context = {
        "tytul": f"{topic} tutorial chapters",
        "tresc": f"Available chapters: {aviable_chapters}",
    }

    return HttpResponse(template.render(context, request), status=200)


def get_chapter(request, topic, chapter):
    template = loader.get_template("quotes/quotes.html")

    if chapter not in tutorials["chapters"][topic]:
        context = {
            "tytul": "No such chapter",
            "tresc": f"No chapter {chapter} for {topic}",
        }
        return HttpResponse(template.render(context, request), status=404)

    context = {
        "tytul": f"{topic} - {chapter}",
        "tresc": f"{topic} - {chapter}",
    }

    return HttpResponse(template.render(context, request), status=200)

