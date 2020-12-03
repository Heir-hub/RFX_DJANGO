from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import UserRegisterIntermediateForm
from .models import IntermediateTutorial
from django.urls import reverse
from django.views.generic import (ListView,
                                  DetailView
)







def intermediateregister(request):
    if request.method == 'POST':
        form = UserRegisterIntermediateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'your account is succesfully created {username}!')
            return redirect('https://paystack.com/pay/v7kd2n9h0o')
    else:
        form = UserRegisterIntermediateForm()
    return  render(request, 'Intermediate/intermediate_register.html', {'form':form})




def Intermediatejoin(request):
    return render(request,'Intermediate/Intermediate_join.html')    



class IntermediateTutorialListView( ListView):
        model = IntermediateTutorial
        template_name = 'Intermediate/Intermediate_tutorial.html'
        context_object_name ='tutorials'
        ordering =['-date']
        paginate_by = 5

 
def VideoCategory(request):
    return render(request, 'tutorials/video_category.html')

