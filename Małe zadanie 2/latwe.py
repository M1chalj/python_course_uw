jezyki = {
    "pl" : "polski",
    "en" : "angielski",
    "ua" : "ukraiński",
    "de" : "niemiecki",
    "ck" : "czeski"
}

powitania = {
    "pl" : "Cześć",
    "en" : "Hello",
    "ua" : "Привіт",
    "de" : "Hallo",
    "ck" : "Ahoj"
}

def tekstPowitania(kod_jezyka):
    if(kod_jezyka in powitania.keys()):
        return powitania[kod_jezyka]
    else:
        return "Nierozpoznany kod języka: " + kod_jezyka

def powitaj():
    print("Dostępne języki:")
    for kod, jezyk in zip(jezyki.keys(), jezyki.values()):
        print(kod,"-",jezyk)
    kod = input("Podaj wybrany język: ")
    print(tekstPowitania(kod))

powitaj()