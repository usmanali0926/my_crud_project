from django.urls import path
from my_crud_app import views
from my_crud_app.views import add_show

urlpatterns = [
    path('', add_show, name='add_show'),
    path('delete/<int:id>/', views.delete_data, name='delete_data'),
    path('<int:id>/', views.edit_data, name='edit_data'),
]
