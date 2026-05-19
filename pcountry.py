import requests
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import HTTPError, ConnectionError, Timeout

class Country:
    def __init__(self, data: dict):
        # Extrae los atributos del diccionario crudo de la API
        self.nombre = data.get("name", {}).get("common", "Desconocido")
        self.capital = data.get("capital", ["—"])[0] if data.get("capital") else "—"
        self.poblacion = data.get("population", 0)
        self.area = data.get("area", 0.0)
        self.region = data.get("region", "—")
        