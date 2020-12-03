"""RFX_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from Advance import views as Advance_view
from Beginner import views as Beginner_view
from Intermediate import views as Intermediate_view
from django.contrib.auth import views as auth_view

                          
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('RFX.urls')),
    path('blog/', include('blog.urls')),
    path('Beginner/', include('Beginner.urls',)),
    path('Advance/', include('Advance.urls',)),
    path('Intermediate/', include('Intermediate.urls',)),
    path('Beginner/',Beginner_view.Beginnerregister, name = 'Beginner-register'),
    path('advanceregister/',Advance_view.advanceregister, name = 'advance-register'),
    path('intermediateregister/',Intermediate_view.intermediateregister, name = 'intermediate-register'),
    path('Advance/',auth_view.LoginView.as_view(template_name ='Advance/login.html'), name= 'login'),
    path('logout/', auth_view.LogoutView.as_view(template_name ='users/logout.html'), name ='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
