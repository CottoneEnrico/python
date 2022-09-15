# Scrivere un programma che calcoli le tasse da pagare
# Se il redito è inferiore a 30.000€ si paga il 15%, se il redito è compreso tra 30.000€ a 60.000€ si paga 20%, se il redito è superiore a 60.000€ si paga 30%

reddito = input("Qual'è il tuo reddito? ")
reddito = int(reddito)
if reddito < 30000:
  reddito = (reddito / 100) * 15
elif reddito > 30000 and reddito < 60000:
  reddito = (reddito / 100) * 20
elif reddito > 60000:
  reddito = (reddito / 100) * 30

print("Le tasse che devi sfortunatamente pagare equivalgono a: " + str(reddito))
