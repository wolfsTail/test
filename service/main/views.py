from django.shortcuts import render

from main.forms import FileForm
from utils import parser


def index(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            data = file.read().decode("utf-8").split()
            frequency = parser.parse_text(data)
            return render(
                request, "main/index.html", {"form": form, "frequency": frequency}
            )
        else:
            return render(request, "main/index.html", {"form": form})
    else:
        form = FileForm()
        return render(request, "main/index.html", {"form": form})


def results(request):
    return render(request, "main/results.html")


def get_result(request, file_id):
    return render(request, "main/detail.html", {"file_id": file_id})
