# Inserimento dei dati

peso = input("Qual'è il tuo peso? ")
altezza = input("Qual'è la tua altezza? ")

peso = float(peso)
altezza = float(altezza)

massaCorporea = peso / (altezza * altezza)
massaCorporea = str(round(massaCorporea))

print("Il tuo indice di massa corporea è:", massaCorporea)

massaCorporea = int(massaCorporea)

if massaCorporea < 18:
  print("Sottopeso")
elif massaCorporea > 25:
  print("Sovrappeso")
else:
  print("Normapeso")
