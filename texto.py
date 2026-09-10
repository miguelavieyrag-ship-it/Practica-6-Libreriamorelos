import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://libreriamorelos.mx/top100/index.html"
response = requests.get(url)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, "html.parser")

libros = soup.find_all("div", class_="product-detail")

datos = []

for libro in libros:
    top_pos = libro.find("p", class_="theme-color fw-bold mb-2 text-center")
    Top_libro = int(top_pos.text.replace("TOP", "").strip())

    Titulo = libro.find("p", class_="name").text.strip()

    Autor_tag = libro.find("p", class_="unit mb-3 link text-center")
    Autor = Autor_tag.text.strip()

    precio_texto = libro.find("div", class_="mt-2 price theme-color text-center").text
    Precio = float(precio_texto.replace("$", "").strip())

    datos.append({
        "Top_libro": Top_libro,
        "Titulo": Titulo,
        "Autor": Autor,
        "Precio_mxn": Precio
    })

df = pd.DataFrame(datos)
df.to_csv("top_librosmorelos.csv", index=False)
print("Scraping exitoso y archivo top_librosmorelos.csv creado.")


with open("texto.py", "w", encoding="utf-8") as f:
    f.write(script_code)
