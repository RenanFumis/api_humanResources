from django.contrib import admin
from django.urls import path
from validation.views import Employee_card_creation

urlpatterns = [
    path('admin/', admin.site.urls),

    path('create/', Employee_card_creation.as_view(), name='create_employee_card'),
]
