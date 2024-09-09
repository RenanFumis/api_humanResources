from rest_framework import serializers
import re
from datetime import datetime
from validation.models import Employee_card_creation
from django.core.exceptions import ValidationError


# Aqui estou validando o CPF com um padrão regex e a formula de validação do CPF
def authenticate_cpf(cpf):
        cpf = re.sub(r'\D', '', cpf)
        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        for i in range(9, 11):
            soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
            digito = (soma * 10) % 11
            if digito == 10:
                digito = 0
            if digito != int(cpf[i]):
                return False
        return True


# Aqui estou validando o email com um padrão regex
def authenticate_email(email):
        email_padrao = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
        return re.fullmatch(email_padrao, email) is not None


class Employee_cardSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee_card_creation
        fields = '__all__'

    def validate_cpf(self, value):
        if not authenticate_cpf(value):
            raise serializers.ValidationError("CPF Inválido!")
        return value
    
    
    def validate_email(self, value):
        if not authenticate_email(value):
            raise serializers.ValidationError("E-mail Inválido!")
        return value
    
    def validate(self, data):
        # Formatar e validar a data de nascimento
        date_of_birth_str = data.get('date_of_birth', '')
        if date_of_birth_str and isinstance(date_of_birth_str, str):
            data['date_of_birth'] = self.format_date(date_of_birth_str, 'date_of_birth')

        # Formatar e validar a data de admissão
        admission_date_str = data.get('admission_date', '')
        if admission_date_str and isinstance(admission_date_str, str):
            data['admission_date'] = self.format_date(admission_date_str, 'admission_date')

        return data
        
    def format_date(self, date_str, field_name):
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y').date()
            return date_obj
        except ValueError:
            raise ValidationError(f'Data inválida. O campo {field_name} deve ser no formato DD/MM/YYYY.')

