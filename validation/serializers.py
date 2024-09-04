from rest_framework import serializers
import re
from validation.models import Employee_card_creation

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

# Aqui estou validando o estado civil com termos pré-definidos
def authenticate_marital_status(estado_civil):
        return estado_civil.lower() in ['solteiro(a)', 'casado(a)', 'divorciado(a)', 'viuvo(a)', 'uniao_estavel']

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
    
    def validate_marital_status(self, value):
        if not authenticate_marital_status(value):
            raise serializers.ValidationError("Estado Civil Inválido, escolha entre: solteiro(a), casado(a), divorciado(a), viuvo(a), uniao_estavel")
        return value
    
    def validate_email(self, value):
        if not authenticate_email(value):
            raise serializers.ValidationError("E-mail Inválido!")
        return value
    
    