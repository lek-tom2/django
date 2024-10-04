from django.http import HttpResponse

open_polls = [
    {
        "topic": "cats",
        "question": "do you like cats",
        "options": [
            "yes",
            "no"
        ]
    }
]

def index(request):
    polls_str = "".join(x["question"] for x in open_polls)
    return HttpResponse(f"polls {polls_str}")
