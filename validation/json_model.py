from validation.choices import nationality_choices, marital_status_choices

def to_dict(model_instance):
        return {
            "complete_name": model_instance.complete_name,
            "date_of_birth": model_instance.date_of_birth.strftime('%d/%m/%Y') if model_instance.date_of_birth else '',
            "nationality": model_instance.get_choice_display(model_instance.nationality, nationality_choices),
            "marital_status": model_instance.get_choice_display(model_instance.marital_status, marital_status_choices),
            "rg": model_instance.rg,
            "cpf": model_instance.cpf,
            "mother_name": model_instance.mother_name,
            "father_name": model_instance.father_name,
            "address": {
                "street": model_instance.address.get('street', ''),
                "number": model_instance.address.get('number', ''),
                "complement": model_instance.address.get('complement', ''),
                "neighborhood": model_instance.address.get('neighborhood', ''),
                "state": model_instance.address.get('state', ''),
                "city": model_instance.address.get('city', ''),
                "cep": model_instance.cep,
            },
            "phone": model_instance.phone,
            "phone2": model_instance.phone2,
            "email": model_instance.email,
            "job_title": model_instance.job_title,
            "salary": str(model_instance.salary),
            "admission_date": model_instance.admission_date.strftime('%d/%m/%Y') if model_instance.admission_date else '',
            "pis": model_instance.pis,
            "employment_type": model_instance.employment_type,
        }