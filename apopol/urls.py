from django.urls import path
from . import views

app_name = "apopol"

urlpatterns = [

    # path("index/", views.index, name="index"),
    # path("index/upload/",views.upload, name="upload"),

    path("index/", views.PortListView.as_view(), name="index"),
    path("index/upload/", views.UploadPortView.as_view(), name="upload"),
    path("delete/<pk>", views.delete, name="delete")
]