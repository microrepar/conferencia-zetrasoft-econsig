import econsig
import relatorio1000


def main():
    descontos_econsig = econsig.descontos()
    descontos_relat1000 = relatorio1000.descontos()

    for rgf in sorted(list(descontos_econsig.keys())):
        if descontos_relat1000.get(rgf) is not None:
            for nome in descontos_econsig[rgf]:
                for verba in sorted(list(descontos_econsig[rgf][nome].keys())):
                    if not descontos_relat1000[rgf].get(verba):
                        print(f'RGF:{rgf: >5} Não foi encontrado valor={descontos_relat1000[rgf].get(verba)} no relatório 1000 para a verba={verba} do arquivo econsig')
        else:
            print(f'RGF:{rgf: >5} não encontrado no relatório 1000.' )

if __name__ == "__main__":
    main()