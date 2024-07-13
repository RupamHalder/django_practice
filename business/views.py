from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
# def index(request):
#     # context = {
#     #     "name": "Rupam",
#     # }
#     return render(request, "index.html")

# class HomeView(View):
#     template_name = "index.html"
#     data = {"name": "Rupam"}
#
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name,
#                       {"data": self.data})


# class LoginView(TemplateView):
#     template_name = "login.html"
#     extra_context = {"page_details": {
#         "page_title": "Login"
#     }}


class LoginView(View):
    template_name = "login.html"
    data = {"page_details": {
        "page_title": "Login"
    }}

    def is_valid_form(self, request_obj):
        pass

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      self.data)

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      self.data)


# class RegisterView(TemplateView):
#     template_name = "register.html"
#     extra_context = {"page_details": {
#         "page_title": "Register"
#     }}


class RegisterView(View):
    template_name = "register.html"
    data = {"page_details": {
        "page_title": "Register"
    }}

    @staticmethod
    def is_valid_form(request_obj):
        password = request_obj.get('password').strip()
        conf_password = request_obj.get('confirmPassword').strip()
        username = request_obj.get('username').strip()
        email = request_obj.get('email').strip()
        username_exist = len(User.objects.filter(username=username)) > 0
        email_exist = len(User.objects.filter(email=email)) > 0
        if password != conf_password:
            return False, "Password and Confirm Password didn't match!"
        elif username_exist:
            return False, "Username taken!"
        elif email_exist:
            return False, "Email taken!"
        else:
            return True, "Success"

    @staticmethod
    def process_request(request_obj):
        username = request_obj.get('username').strip()
        first_name = request_obj.get('firstName').strip()
        last_name = request_obj.get('lastName').strip()
        email = request_obj.get('email').strip()
        password = request_obj.get('password').strip()

        user = User(username=username, first_name=first_name,
                    last_name=last_name, email=email, password=password)
        print("user: ", user)
        user.save()

        if len(User.objects.filter(username=username)) > 0:
            return True, "You account has been created now please login."
        else:
            return False, "Registration failed!"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      self.data)

    def post(self, request, *args, **kwargs):
        request_obj = request.POST
        validation_status, validation_msg = self.is_valid_form(request_obj)
        if validation_status:
            response_status, response_msg = self.process_request(request_obj)
            if response_status:
                messages.success(request, response_msg)
                return redirect('/login')
            else:
                messages.error(request, response_msg)
                return redirect('/register')
        else:
            messages.error(request, validation_msg)
            return redirect('/register')


class HomeView(TemplateView):
    template_name = "index.html"
    extra_context = {"page_details": {
        "page_title": "Home"
    }}


class AboutView(TemplateView):
    template_name = "about.html"


class ServicesView(TemplateView):
    template_name = "services.html"


class PortfolioView(TemplateView):
    template_name = "portfolio.html"


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            print(name, email, message)
            # Do something with the data
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
