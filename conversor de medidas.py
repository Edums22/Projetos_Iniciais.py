medida = float(input("Insira uma distância em metros: "))
km = medida /1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida}m corresponde a {dm}dm {cm}cm e {mm}mm')
print(f'A medida de {medida}m corresponde a {dam}dam {hm}hm e {km}km')