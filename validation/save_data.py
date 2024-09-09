import os
import re
import json



def to_save_data(self):

        if not self.nationality:
            self.nationality = 'BRA'

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
