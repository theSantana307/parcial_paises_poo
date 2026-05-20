import requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import HTTPError, ConnectionError, Timeout

class Country:
    def __init__(self, data: dict):
        
        self.nombre = data.get("name", {}).get("common", "Desconocido")
        self.capital = data.get("capital", ["—"])[0] if data.get("capital") else "—"
        self.poblacion = data.get("population", 0)
        self.area = data.get("area", 0.0)
        self.region = data.get("region", "—")

    def __str__(self) -> str:
        return f"{self.nombre} (Capital: {self.capital}, Población: {self.poblacion:,},Área: {self.area:,} km²)"

    def density(self) -> float:
        return self.poblacion / self.area if self.area > 0 else 0.0 
    
   
    def comparar(self, otros: list):
        todos_los_paises = [self] + otros
        print(f"\n{'Pais':<18} | {'Poblacion':<15} | {'Area (km²)':<12} | {'Densidad (hab/km²)'}")
        print("-" * 75)
        
        ganador_poblacion = self
        ganador_area = self
        ganador_densidad = self
        
        for pais in todos_los_paises:
            dens = pais.density()
            print(f"{pais.nombre:<18} | {pais.poblacion:<15,} | {pais.area:<12,} | {dens:<.2f} hab/km²")
            
            if pais.poblacion > ganador_poblacion.poblacion:
                ganador_poblacion = pais
            if pais.area > ganador_area.area:
                ganador_area = pais
            if dens > ganador_densidad.density():
                ganador_densidad = pais
                
        print("-" * 75)
        print(f" Mayor poblacion : {ganador_poblacion.nombre}")
        print(f" Mayor Area      : {ganador_area.nombre}")
        print(f" Mayor densidad  : {ganador_densidad.nombre}\n")


class CountryAPI:
    BASE = "https://restcountries.com/v3.1"

    def by_region(self, region: str) -> list:
        url = f"{self.BASE}/region/{region}"
        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            return [Country(item) for item in r.json()]
        except Exception as e:
            print(f"Error al buscar region {region}: {e}")
            return []

    def by_name(self, name: str) -> Country:
        url = f"{self.BASE}/name/{name}"
        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            return Country(r.json()[0])
        except Timeout:
            print(f"La API tardo demasiado para: {name}")
        except ConnectionError:
            print(f"Sin conexion a internet al buscar: {name}")
        except HTTPError as e:
            print(f"Error {e.response.status_code}: {name} no encontrado")
        return None


    def by_names(self, names: list) -> list:
        with ThreadPoolExecutor(max_workers=5) as executor:
            resultados = list(executor.map(self.by_name, names))
        return [pais for pais in resultados if pais is not None]
    

    