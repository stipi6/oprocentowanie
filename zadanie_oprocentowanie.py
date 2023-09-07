# pytanka

print("\nprogram wyliczajacy wartosc zadluzenia dla kazdego miesiaca \n ")

kwota_kredytu = int(input("ile wynosi calkowita kwota kredytu? \n "))

oprocentowanie = int(input("jakie jest oprocentowanie kredytu? \n "))

stala_rata = int(input("ile wynosi stala rata? \n "))

# tabela inflacji

inflacja_styczen1 = 1.59282448436825

inflacja_luty1 = -0.453509101198007

inflacja_marzec1 = 2.32467171712441

inflacja_kwiecien1 = 1.26125440724877

inflacja_maj1 = 1.78252628571251

inflacja_czerwiec1 = 2.32938454145522

inflacja_lipiec1 = 1.50222984223283

inflacja_sierpien1 = 1.78252628571251

inflacja_wrzesien1 = 2.32884899407637

inflacja_pazdziernik1 = 0.616921348207244

inflacja_listopad1 = 2.35229588637833

inflacja_grudzien1 = 0.337779545187098

inflacja_styczen2 = 1.57703524727525

inflacja_luty2 = -0.292781442607648

inflacja_marzec2 = 2.48619659017508

inflacja_kwiecien2 = 0.267110317834564

inflacja_maj2 = 1.41795267229799

inflacja_czerwiec2 = 1.05424326726375

inflacja_lipiec2 = 1.4805201044812

inflacja_sierpien2 = 1.57703524727525

inflacja_wrzesien2 = -0.0774206903147018

inflacja_pazdziernik2 = 1.16573339872354

inflacja_listopad2 = -0.404186717638335

inflacja_grudzien2 = 1.49970852083123

# obliczenia

wzor1 = (1 + ((inflacja_styczen1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

styczen1 = wzor1
mniej1 = kwota_kredytu - styczen1

print(f"\nw styczniu twoja pozostala kwota kredytu to {(round(styczen1, 2))} to o {(round(mniej1, 2))} "
      f"mniej niz w zeszlym miesiacu ")

wzor2 = (1 + ((inflacja_luty1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej2 = kwota_kredytu - wzor2
luty1 = styczen1 - mniej2

print(f"w lutym twoja pozostala kwota kredytu to {(round(luty1, 2))} to o {(round(mniej2, 2))} "
      f"mniej niz w zeszlym miesiacu ")

wzor3 = (1 + ((inflacja_marzec1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej3 = kwota_kredytu - wzor3
marzec1 = luty1 - mniej3

print(f"w marcu twoja pozostala kwota kredytu to {(round(marzec1, 2))} to o {(round(mniej3, 2))} "
      f"mniej niz w zeszlym miesiacu \n")

wzor4 = (1 + ((inflacja_kwiecien1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej4 = kwota_kredytu - wzor4
kwiecien1 = marzec1 - mniej4

print(f"w kwietniu twoja pozostala kwota kredytu to {(round(kwiecien1, 2))} to o {(round(mniej4, 2))} "
      f"mniej niz w zeszlym miesiacu")

wzor5 = (1 + ((inflacja_maj1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej5 = kwota_kredytu - wzor5
maj1 = kwiecien1 - mniej5

print(f"w maju twoja pozostala kwota kredytu to {(round(maj1, 2))} to o {(round(mniej5, 2))} "
      f"mniej niz w zeszlym miesiacu")

wzor6 = (1 + ((inflacja_czerwiec1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej6 = kwota_kredytu - wzor6
czerwiec1 = maj1 - mniej6

print(f"w czerwcu twoja pozostala kwota kredytu to {(round(czerwiec1, 2))} to o {(round(mniej6, 2))} "
      f"mniej niz w zeszlym miesiacu \n")

wzor7 = (1 + ((inflacja_lipiec1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej7 = kwota_kredytu - wzor7
lipiec1 = czerwiec1 - mniej7

print(f"w lipcu twoja pozostala kwota kredytu to {(round(lipiec1, 2))} to o {(round(mniej7, 2))} "
      f"mniej niz w zeszlym miesiacu")

wzor8 = (1 + ((inflacja_sierpien1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej8 = kwota_kredytu - wzor8
sierpien1 = lipiec1 - mniej8

print(f"w sierpniu twoja pozostala kwota kredytu to {(round(sierpien1, 2))} to o {(round(mniej8, 2))} "
      f"mniej niz w zeszlym miesiacu")

wzor9 = (1 + ((inflacja_wrzesien1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej9 = kwota_kredytu - wzor9
wrzesien1 = sierpien1 - mniej9

print(f"we wrzesniu twoja pozostala kwota kredytu to {(round(wrzesien1, 2))} to o {(round(mniej9, 2))} "
      f"mniej niz w zeszlym miesiacu \n")

wzor10 = (1 + ((inflacja_pazdziernik1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej10 = kwota_kredytu - wzor10
pazdziernik1 = wrzesien1 - mniej10

print(f"w pazdzierniku twoja pozostala kwota kredytu to {(round(pazdziernik1, 2))} to o {(round(mniej10, 2))} "
      f"mniej niz w zeszlym miesiacu")

wzor11 = (1 + ((inflacja_listopad1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej11 = kwota_kredytu - wzor11
listopad1 = pazdziernik1 - mniej11

print(f"w listopadzie twoja pozostala kwota kredytu to {(round(listopad1, 2))} to o {(round(mniej11, 2))} "
      f"mniej niz w zeszlym miesiacu")

wzor12 = (1 + ((inflacja_grudzien1 + oprocentowanie) / (1000 + stala_rata))) * kwota_kredytu - stala_rata

mniej12 = kwota_kredytu - wzor12
grudzien1 = listopad1 - mniej12

print(f"w grudniu twoja pozostala kwota kredytu to {(round(grudzien1, 2))} to o {(round(mniej12, 2))} "
      f"mniej niz w zeszlym miesiacu \n")
