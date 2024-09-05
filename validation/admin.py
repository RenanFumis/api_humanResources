from django.contrib import admin
from .models import Employee_card_creation

# Aqui é para fazer o teste diretamente no Django Admin
@admin.register(Employee_card_creation)
class EmployeeCardCreationAdmin(admin.ModelAdmin):
    list_display = (
        'complete_name', 'date_of_birth', 'marital_status', 'rg', 'cpf', 'display_address',
        'phone', 'phone2', 'email', 'job_title', 'salary', 'admission_date', 'employment_type'
    )
    search_fields = ('complete_name', 'cpf', 'email')
    list_filter = ('employment_type', 'job_title')
    
    def display_address(self, obj):
        address = obj.address
        return f"{address.get('street', '')}, {address.get('number', '')}, {address.get('city', '')}, {address.get('state', '')} - {address.get('cep', '')}"
    display_address.short_description = 'Address'
    

