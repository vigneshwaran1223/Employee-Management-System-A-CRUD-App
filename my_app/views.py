from django.shortcuts import redirect,render
from .forms import MyRegisterForm
from django.contrib import messages
from .models import RegisterForm

# Create your views here.
def home(request):
    data = RegisterForm.objects.all()
    if(data):
        return render(request,'home.html',{'data':data})
    else:
        return render(request,'home.html')

def insert(request):
    if request.method=="POST":
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,'"Successfully Registered"')
                return redirect("Home")
            except:
                pass
    else:       
        form = MyRegisterForm()
    return render(request,'register.html',{'form':form}) 
def update(request,id):
    data = RegisterForm.objects.get(id=id)
    form = MyRegisterForm(request.POST,instance=data)
    if form.is_valid():  
        form.save()
        messages.success(request,'"Updated Successfully"')
        return redirect("Home")

    return render(request,'update.html',{'data':data})

def delete(request,id):
    data = RegisterForm.objects.get(id=id)
    data.delete()
    messages.error(request,'"Deleted Successfully"')
    return redirect('Home')






