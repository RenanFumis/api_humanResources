# Aqui coloquei as constantes de nacionalidade e estado civil em um arquivo separado para facilitar a manutenção do código.

def nationality_choices():

  return (
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

def marital_status_choices():

  return (
        ('solteiro', 'Solteiro(a)'),
        ('casado', 'Casado(a)'),
        ('divorciado', 'Divorciado(a)'),
        ('viuvo', 'Viúvo(a)'),
        ('uniao_estavel', 'União Estável'),
    )
