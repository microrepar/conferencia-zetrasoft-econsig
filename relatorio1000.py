from pathlib import Path
import csv
import pprint


def descontos():
    path = list(Path.cwd().glob('*.csv'))[-1]

    COLS = None
    descontos_por_rgf = {}
    with path.open(encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=';')
        for row in csv_reader:

            if csv_reader.line_num == 1:
                COLS = dict(zip(row, range(len(row))))
                continue
            
            matricula = int(row[COLS.get('Matric')])

            descontos_por_rgf.setdefault(matricula, {})

            for nome, col in COLS.items():
                if nome.startswith('VB') and row[COLS[nome]]:
                    verba = int(nome[2:5])
                    descontos_por_rgf[matricula].setdefault(verba, row[COLS[nome]])

    # pprint.pprint(descontos_por_rgf)
    return descontos_por_rgf

if __name__ == "__main__":
    descontos()