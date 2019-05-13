"""
Definition of urls for DjangoWeb.
"""

from datetime import datetime
from django.urls import re_path, include, path
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
#from app import forms, views
from dataCRUD.views import PRG_STUDENT_SITE_View
from Interface import views

from UploadingFile.views import uploadCSV


from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    # url(r'^admin/', include(admin.site.urls)),

    path('Interface/', views.home, name='home'),
    path('Interface/descriptiveStats', views.descriptiveStats, name='descriptiveStats'),
    path('Interface/maps', views.maps, name='maps'),
    path('Interface/etl', views.etl, name='etl'),
    path('', views.home, name='home'),
    #path('contact/', views.contact, name='contact'),
    #path('about/', views.about, name='about'),
    #path('login/',
    #    LoginView.as_view
    #    (
    #        template_name='app/login.html',
    #        authentication_form=forms.BootstrapAuthenticationForm,
    #        extra_context=
    #        {
    #            'title': 'Log in',
    #            'year' : datetime.now().year,
    #        }
    #    ),
    #    name='login'),
    #path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    #path('admin/', admin.site.urls),
    path('Interface/dataCRUD/',PRG_STUDENT_SITE_View, name='dataCRUD'), # Url to programstudentsite module
    #url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
    path('Interface/uploadcsv/',uploadCSV,name='uploadCSV')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)