from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm
from django.views.generic.edit import CreateView
from .models import views
# Create your views here.
def home(request):
    return render(request, 'home.html')
   
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    form = UserCreationForm()
    return render(request, 'signup.html',{'form':form})

#Todo ass error message if credentials are wrong
def login_view(request):
    #Todo - handle post method
    error_message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #extracts the values, brings them to database
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Sorry your username and password are invalid"
    context = {'form':form, 'error_message':error_message}
    form = LoginForm
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect('home')

class CreateView(CreateView):
    model = Skill
    fields = ['skill', 'skill_level']
    template_name = 'skills/skill_form.html'
    def form_valid(self, form):
        form.instance.user= self.request.user
        return super().form_valid(form)