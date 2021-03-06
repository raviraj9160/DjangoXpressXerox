from django.urls import path
from . import views

# Template tagging
app_name = "action"

urlpatterns = [
    path('userDashboard/', views.userDashboard, name = "userDashboard"),
    path('adminDashboard/', views.adminDashboard, name= "adminDashboard"),
    path('sendToPrint/', views.sendToPrint, name="sendToPrint"),
    path('handleRequest/', views.handleRequest, name="handleRequest"),
    path('pendingOrder/', views.pendingOrder, name="pendingOrder"),
    path('deleteOldOrderID/', views.deleteOldOrderID, name="deleteOldOrderID"),
    path('docxToPdf/', views.docxToPdf, name="docxToPdf"),

]