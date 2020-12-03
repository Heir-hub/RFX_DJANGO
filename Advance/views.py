from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterAdvanceForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import AdvanceTutorial
from django.urls import reverse
from django.views.generic import (ListView,
                                  DetailView
)







def advanceregister(request):
    if request.method == 'POST':
        form = UserRegisterAdvanceForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'your account is succesfully created {username}!')
            return redirect('https://paystack.com/pay/1xgi1quvcg')
    else:
        form = UserRegisterAdvanceForm()
    return  render(request, 'Advance/Advance_register.html', {'form':form})




def Advancejoin(request):
    return render(request,'Advance/Advance_join.html')    







class AdvanceTutorialListView(ListView):
        model = AdvanceTutorial
        template_name = 'Advance/Advance_tutorial.html'
        context_object_name ='tutorials'
        ordering =['-date']
        paginate_by = 5

        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)

            

 


def VideoCategory(request):
    return render(request, 'tutorials/video_category.html')