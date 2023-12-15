from django.shortcuts import render
from .forms import InputEmail, InputPassword, InputName
from django.http import HttpResponseRedirect

def join(request):
    if request.method == "POST":
        email = request.POST.get("email", "Undefined")
        password = request.POST.get("password", "Undefined")

        input_email = InputEmail(request.POST)
        input_password = InputPassword(request.POST)

        if input_email.is_valid() and input_password.is_valid():
            if email == 'User@mail.ru' and password == "12345678":
                return render(request, 'result.html', context={'text': 'Вы успешно вошли'})

            else:
                return HttpResponseRedirect('registration/')


    else:
        input_email = InputEmail()
        input_password = InputPassword()
        return render(request, 'join.html', {'input_email': input_email, 'input_password': input_password})


def registration(request):
    if request.method == "POST":
        name = request.POST.get("name", "Undefined")
        email = request.POST.get("email", "Undefined")
        password = request.POST.get("password", "Undefined")

        input_name = InputName(request.POST)
        input_email = InputEmail(request.POST)
        input_password = InputPassword(request.POST)

        if input_name.is_valid() and input_email.is_valid() and input_password.is_valid():
            return render(request, 'successfully.html', context={'name': name,'text': ', поздравляю с регистрацией!'})


    else:
        input_name = InputName()
        input_email = InputEmail()
        input_password = InputPassword()
        return render(request, 'registration.html', {'input_name': input_name, 'input_email': input_email, 'input_password': input_password})


def user_return(request):
    return render(request, 'result.html')
