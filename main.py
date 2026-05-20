from pcountry import CountryAPI

if __name__ == "__main__":
    api = CountryAPI()
    
    names = [
        "ecuador", "switzerland", "turkey", "italy", "venezuela", 
        "egypt", "norway", "yemen", "estonia", "ireland", 
        "france", "ethiopia", "russia"
    ]
    
    print("Solicitando informacion de los 13 paises en paralelo (Concurrencia)...")
    paises = api.by_names(names)
    
    if paises:
        print("\nRESULTADOS DEL PARCIAL (13 Paises):\n")
        paises[0].comparar(paises[1:])
    else:
        print("No se pudo obtener informacion de los paises.")