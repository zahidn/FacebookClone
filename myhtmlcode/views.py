from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')


def add(request):
    number1 = int(request.POST["num1"])
    number2 = int(request.POST["num2"])
    result = number1 + number2
    return render(request, 'result.html',{'result': result})