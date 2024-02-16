print("Witaj w Życzeniomacie!")
print("Ten program wygeneruje dla Ciebie krótkie życzenia urodzinowe.\nW kolejnych krokach postępuj zgodnie z "
      "poleceniami:\n")
print("Podaj dzisiejszą datę:\nDzień/Miesiąc...:") 
data_dzien = input()
print("...oraz rok")
data_rok = int(input())
print("Podaj swoje imię:") 
imie_nadawcy = str(input())
print("Podaj swoją płeć (K/M):")
sex = input()
print("Podaj imię jubilat/ka:")
imie_odbiorcy = input()
print("Podaj rok urodzenia jubilata/ki:")
data_urodzenia = int(input())
print("Dokończ zdanie: życzę Ci...")
zyczenia = input()
wiek = (data_rok - data_urodzenia)
print("\n __________________________________________________________________________________________<3\n|")
print(f"|Witaj {imie_odbiorcy}!\n|\n|Z okazji Twoich {wiek} urodzin, życzę Ci {zyczenia}!\n|")
if sex == "K":
      print(f"|~Twoja serdeczna przyjaciółka {imie_nadawcy}!")
elif sex == "M":
      print(f"|~Twój serdeczny przyjaciel {imie_nadawcy}!")
else:
      print(f"|~{imie_nadawcy}!")
print("|__________________________________________________________________________________________<3\n")
#ver1.2 - wersja rozwojowa