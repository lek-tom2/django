from django.http import HttpResponse, Http404
from django.template import loader

tutorials = {
    "tutorials": [
        "django",
    ],
    "chapters": {
        "django": [
            "intro",
            "paths"
        ],
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

    # Split topic string in case multiple topics are passed
    topic_list = topic.split(',')

    for single_topic in topic_list:
        if single_topic not in tutorials["tutorials"]:
            context = {
                "tytul": "No such tutorial",
                "tresc": f"There is no tutorial for: {single_topic}",
            }
            return HttpResponse(template.render(context, request), status=404)

        available_chapters = ",".join(tutorials["chapters"][single_topic])
        context = {
            "tytul": f"{single_topic} tutorial chapters",
            "tresc": f"Available chapters: {available_chapters}",
        }
        return HttpResponse(template.render(context, request), status=200)


def get_chapter(request, topic, chapter):
    template = loader.get_template("quotes/quotes.html")

    # Split topic string in case multiple topics are passed
    topic_list = topic.split(',')

    for single_topic in topic_list:
        if single_topic not in tutorials["chapters"]:
            context = {
                "tytul": "No such topic",
                    "tresc": f"No such chapter",
            }
            return HttpResponse(template.render(context, request), status=404)

        if chapter not in tutorials["chapters"][single_topic]:
            context = {
                "tytul": "No such chapter",
                "tresc": f"No such chapter",
            }
            return HttpResponse(template.render(context, request), status=404)

        context = {
            "tytul": f"{single_topic} - {chapter}",
            "tresc": f"{single_topic} - {chapter}",
        }

        return HttpResponse(template.render(context, request), status=200)
