# Un negozio vuole incentivare gli acquisti applicando sconti maggiori a chi spende di più
# Se un cliente spende fino a 100€ deve essere fatto lo sconto del 15%
# Se spende da 200€ a 300€ lo sconto è del 40%
# Se spende oltre 400€ lo sconto è del 60%

# Scrivere un programma che dato il totale dell'acquiesto calcoli il prezzo finale che il cliente deve pagare.

spentMoney = input("Inserisci la quantità di soldi che spenderai: ")
spentMoney = float(spentMoney)
discount = 0

if spentMoney < 100:
  discount = (spentMoney / 100) * 15 # 15% off
  spentMoney -= discount
elif spentMoney >= 100 and spentMoney < 200:
  discount = (spentMoney / 100) * 20 # 20% off
  spentMoney -= discount
elif spentMoney >= 200 and spentMoney <= 300:
  discount = (spentMoney / 100) * 40 # 40% off
  spentMoney -= discount
elif spentMoney >= 400:
  discount = (spentMoney / 100) * 60 # 60% off
  spentMoney -= discount

print("Il totale da pagare sarà " + str(spentMoney))
