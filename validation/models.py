import os
import json
import re
from django.db import models
from datetime import datetime

NATIONALITY_CHOICES = (
    ('BRA', 'Brasileira'),
    ('ARG', 'Argentina'),
    ('URU', 'Uruguaia'),
    ('PAR', 'Paraguaia'),
    ('VEN', 'Venezuelana'),
    ('COL', 'Colombiana'),
    ('PER', 'Peruana'),
    ('CHI', 'Chilena'),
    ('EQU', 'Equatoriana'),
    ('BOL', 'Boliviana'),
    ('EUA', 'Americana'),
    ('POR', 'Portuguesa'),
    ('ESP', 'Espanhola'),
    ('FRA', 'Francesa'),
    ('ITA', 'Italiana'),
    ('ALE', 'Alemã'),
    ('ING', 'Inglesa'),
)
MARITAL_STATUS_CHOICES = (
    ('solteiro', 'Solteiro(a)'),
    ('casado', 'Casado(a)'),
    ('divorciado', 'Divorciado(a)'),
    ('viuvo', 'Viúvo(a)'),
    ('uniao_estavel', 'União Estável'),
)
class Employee_card_creation(models.Model):
    complete_name = models.CharField(max_length=300)
    date_of_birth = models.DateField(default=datetime.now)
    nationality = models.CharField(
        max_length=100,
        default='Brasileira',
        choices=NATIONALITY_CHOICES
    )
    marital_status = models.CharField(
        max_length=20,
        choices=MARITAL_STATUS_CHOICES
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


    def save(self, *args, **kwargs):
        # Ajustando os campos para o formato correto
        if isinstance(self.date_of_birth, str):
            self.date_of_birth = self.format_date(self.date_of_birth, 'Data de Nascimento')

        if isinstance(self.admission_date, str):
            self.admission_date = self.format_date(self.admission_date, 'Data de Admissão')

        self.cpf = f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        self.rg = f"{self.rg[:2]}.{self.rg[2:5]}.{self.rg[5:8]}-{self.rg[8:]}"
        self.phone = f"({self.phone[:2]}) {self.phone[2:7]}-{self.phone[7:]}"
        if self.phone2:
            self.phone2 = f"({self.phone2[:2]}) {self.phone2[2:7]}-{self.phone2[7:]}"

        self.cep = f"{self.address.get('cep', '')[:5]}-{self.address.get('cep', '')[5:]}"

        super().save(*args, **kwargs)
        self.salvar_dados()

    def to_dict(self):
        return {
            "complete_name": self.complete_name,
            "date_of_birth": self.date_of_birth.strftime('%d/%m/%Y') if self.date_of_birth else '',
            "nationality": self.nationality,
            "marital_status": self.marital_status,
            "rg": self.rg,
            "cpf": self.cpf,
            "mother_name": self.mother_name,
            "father_name": self.father_name,
            "address": {
                "street": self.address.get('street', ''),
                "number": self.address.get('number', ''),
                "complement": self.address.get('complement', ''),
                "neighborhood": self.address.get('neighborhood', ''),
                "state": self.address.get('state', ''),
                "city": self.address.get('city', ''),
                "cep": self.cep,
            },
            "phone": self.phone,
            "phone2": self.phone2,
            "email": self.email,
            "job_title": self.job_title,
            "salary": str(self.salary),
            "admission_date": self.admission_date.strftime('%d/%m/%Y') if self.admission_date else '',
            "pis": self.pis,
            "employment_type": self.employment_type,
        }

    def salvar_dados(self):

        # Caminho para a área de trabalho e pasta CLT_RH
        desktop_path = os.path.expanduser("~/Desktop")
        clt_rh_path = os.path.join(desktop_path, "CLT_RH")
        os.makedirs(clt_rh_path, exist_ok=True)  # Cria a pasta CLT_RH se não existir


        nome_completo = re.sub(r'\W+', '_', self.complete_name).lower()
        arquivo = os.path.join(clt_rh_path, f'{nome_completo}_clt.json')

        dados = self.to_dict()
        print(f"Salvando dados no arquivo: {arquivo}")

        try:
            with open(arquivo, 'r', encoding='utf-8') as file:
                dados_existentes = json.load(file)
        except FileNotFoundError:
            dados_existentes = {}

        dados_existentes[self.cpf] = dados

        try:
            with open(arquivo, 'w', encoding='utf-8') as file:
                json.dump(dados_existentes, file, indent=4, ensure_ascii=False)
            print(f"Dados salvos no arquivo {arquivo}")
        except Exception as e:
            print(f"Erro ao salvar dados no arquivo {arquivo}: {e}")
