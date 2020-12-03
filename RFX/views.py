from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import (ListView,
                                  DetailView
)


def home(request):
    return render(request,'RFX/index.html')

@login_required
def admin(request):
    if request.user.is_superuser:
        return render(request,'RFX/admin.site.urls',args)    
    else:
        return render(request,'RFX/index.html',args)    


def join(request):
    return render(request,'RFX/join.html')    


def aboutfx(request):
    return render(request,'RFX/aboutfx.html')    


