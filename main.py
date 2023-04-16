txt=str(input("Inserte un texto para verificar si es palíndromo. \n"))
txtr=txt.replace(" ","")
txtl=txtr.lower()
txtr=txtl.replace("á","a")
txtr=txtr.replace("é","e")
txtr=txtr.replace("í","i")
txtr=txtr.replace("ó","o")
txtr=txtr.replace("ú","u")
txtrv=txtr[::-1]
if txtrv==txtr:
  print(f"El texto {txt} es palíndromo.")
else:
  print(f"El texto {txt} no es palíndromo.")
