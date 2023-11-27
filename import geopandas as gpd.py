import geopandas as gpd
import matplotlib.pyplot as plt

# https://www.icgc.cat/ca/Descarregues/Cartografia-vectorial/Divisions-administratives
file_path = "divisions-administratives-v2r1-comarques-100000-20230928.json"
comarques = gpd.read_file(file_path)

# 
#print(comarcas.head())


comarques.plot(figsize=(12, 8), edgecolor="black", cmap="viridis")
plt.title("Comarques de Cataluya")
plt.axis("off")  # Desactiva los ejes
plt.show()
print (comarques['NOMCOMAR'])