from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world.")

    # template = loader.get_template("students/index.html")
    # context = {
    #     "name": "Rupam",
    # }
    # return HttpResponse(template.render(context, request))

    context = {
        "name": "Rupam",
    }
    return render(request, "students/index.html", context)

def add_two_values(request):
    return render(request, "students/add-two-values.html")

def addition_result(request):
    print("request.params: ", request.GET)
    num1 = int(request.GET["num1"])
    num2 = int(request.GET["num2"])
    result = num1 + num2

    context = {
        "num1": num1,
        "num2": num2,
        "sum": result
    }
    return render(request, "students/addition-result.html", context)
