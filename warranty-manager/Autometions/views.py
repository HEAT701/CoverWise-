from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.shortcuts import render,redirect,get_object_or_404
from warranty_app.models import Warranty
# Create your views here.

@login_required
def Get_Document(request, id):
   keys = f'warranty_{id}'
   warranty = cache.get(keys)
   if not warranty:
       print("Data fetched from database")
       warranty = get_object_or_404(Warranty, id=id)
       cache.set(keys, warranty, nx=300)  # Cache for 5 minutes
   else:
         print("Data fetched from RAM")

   return render(request, 'view_item.html', {'warranty': warranty})