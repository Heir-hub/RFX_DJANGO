from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterBeginnerForm
from .models import BeginnerTutorial
from django.urls import reverse
from django.views.generic import (ListView,
                                  DetailView
)








def Beginnerregister(request):
    if request.method == 'POST':
        form = UserRegisterBeginnerForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'your account is succesfully created {username}!')
            return redirect('https://paystack.com/pay/ctkna14ald')
    else:
        form = UserRegisterBeginnerForm()
    return  render(request, 'Beginner/Beginner_register.html', {'form':form})



def Beginnerjoin(request):
    return render(request,'Beginner/Beginner_join.html')    






class BeginnerTutorialListView( ListView):
        model = BeginnerTutorial
        template_name = 'Beginner/Beginner_tutorial.html'
        context_object_name ='tutorials'
        ordering =['-date']
        paginate_by = 5

 


def VideoCategory(request):
    return render(request, 'tutorials/video_category.html')