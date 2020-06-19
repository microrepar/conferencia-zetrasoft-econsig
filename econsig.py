import pprint
from pathlib import Path


def descontos():

    matricula = slice(0, 8)
    cpf = slice(8, 21)
    nome = slice(21,71)
    cod_prefeitura = slice(71,77)
    verba = slice(77, 80)
    valor = slice(80, 90)
    cod_econsig = slice(90, 96)
    data = slice(96, 104)

    path = list(Path.cwd().glob('*.txt'))[-1]

    descontos = {}
    lista_verbas = {}

    for row in path.read_text().splitlines():
        # if row[verba] == '276' and int(row[matricula]) == 7680:
        #     print(row[matricula], row[nome], row[verba], row[valor])
        
        rgf = int(row[matricula])
        cod_verba = int(row[verba])
        nome_servidor = row[nome]

        descontos.setdefault(rgf, {})
        descontos[rgf].setdefault(nome_servidor, {})
        descontos[rgf][nome_servidor].setdefault(cod_verba, 0)
        descontos[rgf][nome_servidor][cod_verba] += float(row[valor])

        lista_verbas.setdefault(cod_verba, '')

    rows = []        
    for rgf in sorted(list(descontos.keys())):
        for nome in descontos[rgf]:
            for vb in sorted(list(descontos[rgf][nome].keys())):
                # print(f'{rgf:0>5}', nome, f'{vb:0>3}', f'{descontos[rgf][nome][vb]:0>7.2f}')
                rows.append([f'{rgf:0>5}', nome, f'{vb:0>3}', f'{descontos[rgf][nome][vb]:0>7.2f}'])    

    # for vb in lista_verbas:
    #     print(vb)

    return descontos


if __name__ == "__main__":
    descontos()
