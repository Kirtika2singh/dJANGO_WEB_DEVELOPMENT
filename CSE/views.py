
from django.shortcuts import render, redirect
from .forms import CreateUserForm 

from django.contrib.auth import login
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
#from django.contrib import authenticate, login, logout
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required 



@login_required(login_url = 'login')
def home(request):
	return render (request,"home.html", context = {})





def register(request):
	
	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Your Account has been created for '+ user)
			return redirect('login')


	context = { 'form': form }
	return render (request, 'register.html', context)


def login_reg(request):

	if request.method =='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, "Username Or password is incorrect.")


	context = {}
	return render (request, 'login.html', context)

def logoutuser(request):
	logout(request)
	return redirect('login')

from django.shortcuts import render

from CSE.models import Student

# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required(login_url = 'login')
def students(request):
    student = Student.objects.all()
    context = {'student': student}
    return render(request, 'student.html', context)




from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

class Forms(CreateView):
    model = Student
    fields = "__all__"
    template_name = 'forms.html'
    success_url = '/'

class StudentList(ListView):
    model = Student
    template_name = 'stulist.html'

class StudentDetail(DetailView):
    model = Student
    template_name = 'studetail.html'

class StudentUpdate(UpdateView):
    model = Student
    fields = '__all__'
    template_name = 'stuupdate.html'
    success_url = '/'

class StudentDelete(DeleteView):
    model = Student
    template_name = 'studelete.html'
    success_url = '/'

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def portfolio(request):
    return render(request,'portfolio.html')