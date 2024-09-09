import os
import json
import re
from django.db import models
from datetime import datetime
from validation.choices import nationality_choices, marital_status_choices
from validation.save_data import to_save_data
from validation.json_model import to_dict as json_to_dict

class Employee_card_creation(models.Model):
    complete_name = models.CharField(max_length=300)
    date_of_birth = models.DateField(default=datetime.now)
    nationality = models.CharField(
        max_length=100,
        choices=nationality_choices(),
        blank=True,
        default='BRA',
    )
    marital_status = models.CharField(
        max_length=20,
        choices=marital_status_choices()
        )
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20, unique=True)
    mother_name = models.CharField(max_length=300, default='N/A')
    father_name = models.CharField(max_length=300, null=False, default='N/A')
    address = models.JSONField()
    phone = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    job_title = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    admission_date = models.DateField()
    pis = models.CharField(max_length=20, unique=True, null=True, blank=True)
    employment_type = models.CharField(max_length=20)

    def get_choice_display(self, field_value, choices_func):
        # Retorna o valor legível de um campo de escolha
        choices = choices_func()
        choices_dict = dict(choices)
        return choices_dict.get(field_value, field_value)

    def save(self, *args, **kwargs):
        # Ajustando os campos para o formato correto
        if isinstance(self.date_of_birth, str):
            self.date_of_birth = self.format_date(self.date_of_birth, 'Data de Nascimento')

        if isinstance(self.admission_date, str):
            self.admission_date = self.format_date(self.admission_date, 'Data de Admissão')

        self.cpf = f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        self.rg = f"{self.rg[:2]}.{self.rg[2:5]}.{self.rg[5:8]}-{self.rg[8:]}"
        self.pis = f"{self.pis[:3]}.{self.pis[3:8]}.{self.pis[8:10]}-{self.pis[10]}"
        self.phone = f"({self.phone[:2]}) {self.phone[2:7]}-{self.phone[7:]}"
        if self.phone2:
            self.phone2 = f"({self.phone2[:2]}) {self.phone2[2:7]}-{self.phone2[7:]}"

        self.cep = f"{self.address.get('cep', '')[:5]}-{self.address.get('cep', '')[5:]}"

        super().save(*args, **kwargs)
        to_save_data(self)

    def to_dict(self):
        return json_to_dict(self)
        