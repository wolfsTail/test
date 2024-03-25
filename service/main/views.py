from django.shortcuts import render

from main.forms import FileForm
from utils import parser


def index(request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            data = file.read().decode("utf-8")
            parsed_data = parser.parse_file(data)
            frequency = parser.get_ft_idf(parsed_data)
            return render(
                request, "main/index.html", {"form": form, "frequency": frequency}
            )
        else:
            return render(request, "main/index.html", {"form": form})
    else:
        form = FileForm()
        return render(request, "main/index.html", {"form": form})
