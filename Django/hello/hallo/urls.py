from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("arda/",views.arda,name="arda"),
    path("david/",views.david,name="david"),
    path("newyear/", include("newyear.urls")),
    path('ToDo/', include('ToDo.urls'))
]   