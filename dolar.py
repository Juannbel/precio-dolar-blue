import requests
from bs4 import BeautifulSoup

html_dolar = requests.get("https://www.dolarhoy.com/cotizaciondolarblue")
soup_dolar = BeautifulSoup(html_dolar.content, 'lxml')
precios_dolar_compra_venta = soup_dolar.find_all(class_="value", limit=2)
precios= []
for precio in precios_dolar_compra_venta:
	precio = str(precio)
	precio = precio.strip('<div class="value">$ </div>')
	precio = precio.replace(",", ".")
	precio = float(precio)
	precio = precios.append(precio)

precio_dolar_venta = precios[1]
print("La cotizacion del dolar blue es: $ARS" + str(precio_dolar_venta))
