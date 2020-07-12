from django.urls import path

from Blog import views

urlpatterns = [
    path('',views.home,name='home'),
    path('python',views.python,name='python'),
    path('java',views.java,name='java'),
    path('c#',views.csharp,name='csharp'),
    path('html',views.html,name='html'),
]
