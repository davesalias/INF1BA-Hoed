def vragen_ophalen():
    with open('meerkeuzevragen.txt') as f:
        data = f.read()

    vragenlijst = data.split('\n')

    return vragenlijst


def vraag_en_antwoord(datastructuur):
    teller = 0

    if teller == 0:
        print(datastructuur[0])
        antwoord_1 = input('Antwoord: ')
        teller += 1

    if teller == 1:
        print(datastructuur[1])
        antwoord_2 = input('Antwoord: ')
        teller += 1

    if teller == 2:
        print(datastructuur[2])
        antwoord_3 = input('Antwoord: ')
        teller += 1

    with open('antwoorden_gebruiker', "a") as g:
        g.write(f'\n{antwoord_1} \n{antwoord_2} \n{antwoord_3}')
        g.close()


def main():
    meerkeuzevragen = vragen_ophalen()
    vraag_en_antwoord(meerkeuzevragen)
    input_actie = input(
        "Type 'q' als je het programma wilt stoppen "
        "\nType '1' Als je alle vragen wilt doorlopen "
        "\nType '2' Als je de laatste uitslag wilt zien"
        "\n "
    )

    if input_actie == 'q':
        quit()
    if input_actie == '1':
        vraag_en_antwoord(meerkeuzevragen)
    if input_actie == '2':
        with open("antwoorden_gebruiker") as k:
            antwoorden_bestand = k.read()
            print(antwoorden_bestand)


if __name__ == "__main__":
    main()
