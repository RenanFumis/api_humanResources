from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

class Employee_card_creation(models.Model):

  complete_name = models.CharField(max_length=300)
  age = models.IntegerField()
  marital_status = models.CharField(max_length=20)
  rg = models.CharField(max_length=20)
  cpf = models.CharField(max_length=20, unique=True)
  address = models.JSONField()
  phone = models.CharField(max_length=20)
  phone2 = models.CharField(max_length=20, blank=True, null=True)
  email = models.EmailField()
  job_title = models.CharField(max_length=50)
  salary = models.DecimalField(max_digits=10, decimal_places=2)
  admission_date = models.DateField()
  employment_type = models.CharField(max_length=20)


  def save(self, *args, **kwargs):
      # Ajustando os campos para o formato correto
      self.cpf = f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
      self.rg = f"{self.rg[:2]}.{self.rg[2:5]}.{self.rg[5:8]}-{self.rg[8:]}"
      self.phone = f"({self.phone[:2]}) {self.phone[2:7]}-{self.phone[7:]}"
      if self.phone2:
          self.phone2 = f"({self.phone2[:2]}) {self.phone2[2:7]}-{self.phone2[7:]}"
      self.admission_date = self.admission_date.strftime('%d/%m/%Y')
      self.cep = f"{self.address.get('cep', '')[:5]}-{self.address.get('cep', '')[5:]}"

      try:
          # Ajustando a data de admissão no formato DD/MM/YYYY (caso venha em outro formato)
        if isinstance(self.admission_date, str):
            self.admission_date = datetime.strptime(self.admission_date, '%d/%m/%Y').date()
      except ValueError:
            raise ValidationError('Data inválida. Deve ser no formato DD/MM/YYYY.')
  
      super().save(*args, **kwargs)


# Esta é forma de retornar um dicionário com os dados do objeto em formato JSON
  def to_dict(self):
        
        return {
            "complete_name": self.complete_name,
            "age": self.age,
            "marital_status": self.marital_status,
            "rg": self.rg,
            "cpf": self.cpf,
            "address":{
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
            "salary": self.salary,
            "admission_date": self.admission_date.strftime('%d/%m/%Y'),
            "employment_type": self.employment_type,
        }