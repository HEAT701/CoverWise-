
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Warranty
from .forms import WarrantyForm
from django.core.cache import cache
from django.db.models import Count,Avg
# Create your views here.
def Home(request):
   return render(request,"Home.html")


#def dashbord(request):
  #  return render (request,'dashbord.html')
def register_view(request):
    if request.method =="POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request,'register.html',{'form':form})

def login_view(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = authenticate(request,username=username,password= password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid User")
    return render(request,'login.html')



def logout_view(request):
    logout(request)
    return redirect('Home')

@login_required
def dashboard_view(request):
    data = Warranty.objects.filter(user_id=request.user)
    if request.method =="GET":
        if data.exists():
            top_three = data.order_by('-expiry_date')[:3]
            Total = data.aggregate(total=Count("expiry_date"))['total']
            Total_products = data.count()
        else:
            top_three = []
            Total = 0
            Total_products = 0
    return render(request, 'dashboard.html', {'data': data,'products': top_three,'Total_products': Total_products,'Total_ex':Total})

def file_upload(request):
    return render(request,'dashboard.html')


@login_required
def Warranty_form(request):
    if request.method == "POST":
        form = WarrantyForm(request.POST, request.FILES)
        if form.is_valid():
            warranty = form.save(commit=False)
            warranty.user_id = request.user
            warranty.save()
            return redirect('dashboard')
    else:
        form = WarrantyForm()
    return render(request, 'warranty_form.html', {'form': form})


# delete warranty 
@login_required
def delete_warranty(request,id):
    if request.method == "POST":
      warranty = get_object_or_404(Warranty, id=id)
      warranty.delete()
      return redirect('dashboard')
    else:
        return HttpResponse("Method not allowed")

@login_required
def Update_item(request ,id ):
    wareenty = get_object_or_404(Warranty, id=id)
    if request.method == "POST":
        form = WarrantyForm(request.POST, request.FILES, instance=wareenty)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = WarrantyForm(instance=wareenty)
    return render(request, 'update_item.html', {'form': form, 'warranty': wareenty})

# View to handle the update of warranty items
@login_required
def view_item(request, id):

    warranty = get_object_or_404(Warranty, id=id)
    return render(request, 'view_item.html', {'warranty': warranty})



def Get_Document(request, id):
   keys = f'warranty_{id}'
   warranty = cache.get(keys)
   if not warranty:
       warranty = get_object_or_404(Warranty, id=id)
       cache.set(keys, warranty, ex=30)  # Cache for 5 minutes
   else:
         print("Data fetched from cache")
    
   return render(request, 'get_document.html', {'warranty': warranty})


