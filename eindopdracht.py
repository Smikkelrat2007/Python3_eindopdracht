def print_lijst(nummersl):
  for key, value in nummersl.items():
    print(key,"-",value)

def nieuw_contact(nummers):
  nieuwecontactnaam = input('wat is de naam van je nieuwe contact?')
  nieuwenummervancontact = input('wat is het nummer van je nieuwe contact?')
  nummers[nieuwecontactnaam] = nieuwenummervancontact

def verwijder_contact(nummers):
  verwijderr = input('wil je het contact verwijderen met behulp van de naam van het contact of met het nummer van het contact??? \n1. met het nummer \n2. met de naam')
  if verwijderr == "2":
    keyver = input('wat is de naam die je wilt verwijderen?')
    del nummers[keyver]
  if verwijderr == "1":
    valver = input('wat is het nummer die je wilt verwijderen?')
    for key, value in nummers.items():
      if valver == value:
        del nummers[key]

def bewerk_contact(nummers):
  connabew = input('wil je het contact bewerken met behulp van de naam van het contact of met het nummer van het contact??? \n1. met de naam \n2. met het nummer')
  if connabew == "1":
    keybew = input('wat is de naam die je wilt bewerken?')
    valbew = nummers[keybew]
    naambewkeybew = input('wil je de naam bewerken of wil je het nummer bewerken? \n1. naam \n2. nummer')
    if naambewkeybew == "1":
      nieuwenaam = input('wat word de nieuwe naam?')
      del nummers[keybew]
      nummers[nieuwenaam] = valbew
    elif naambewkeybew == "2":
      nieuwnummer = input('wat word het nieuwe nummer?')
      del nummers[keybew]
      nummers[keybew] = nieuwnummer
  if connabew == "2":
    valbew = input('wat is het nummer die je wilt bewerken?')
    for key, value in nummers.items():
      if valbew == value:
        keybew = key
    naambewkeybew = input('wil je de naam bewerken of wil je het nummer bewerken? \n1. naam \n2. nummer')
    if naambewkeybew == "1":
      nieuwenaam = input('wat word de nieuwe naam?')
      del nummers[keybew]
      nummers[nieuwenaam] = valbew
    elif naambewkeybew == "2":
      nieuwnummer = input('wat word het nieuwe nummer?')
      del nummers[keybew]
      nummers[keybew] = nieuwnummer

def main():
  nummers = {"albert" : "1" , "berta" : "2", "clara" : "3"}
  homevraag = 0
  while homevraag != '5':
    homevraag = input('wil je: \n1. print lijst uit \n2. maak een nieuw contact aan \n3. verwijder een contact \n4. bewerk een contact \n5. stop het progamma  >>>')
    print(homevraag)
    if homevraag == "1": #1
      print_lijst(nummers)

    elif homevraag == "2": #2
      nieuw_contact(nummers)

    elif homevraag == "3": #3
      verwijder_contact(nummers)

    elif homevraag == "4": #4
      bewerk_contact(nummers)

    # stop optie toevoegen

  print('doei!! :)')

main()
