# Parcial 2 - Programación Avanzada
## Consumo de APIs, POO y Concurrencia

### 👥 Integrantes del Grupo
* **Estiven Santana** - Usuario de GitHub: `theSantana307`
* **Yeifer Medina** - Usuario de GitHub: `yeifermedina`

### 🗺️ Asignación de Letras y Países Elegidos
Aplicando la regla del parcial (un país por cada letra de nuestros nombres, usando países diferentes para las letras repetidas), seleccionamos los siguientes 13 países:

| Letra | Estudiante | País Elegido (Español) | Nombre en Código (API) |
| :---: | :---: | :--- | :--- |
| **E** | Estiven | Ecuador | `ecuador` |
| **S** | Estiven | Suiza | `switzerland` |
| **T** | Estiven | Turquía | `turkey` |
| **I** | Estiven | Italia | `italy` |
| **V** | Estiven | Venezuela | `venezuela` |
| **E** | Estiven | Egipto (E repetida) | `egypt` |
| **N** | Estiven | Noruega | `norway` |

| **Y** | Yeifer | Yemen | `yemen` |
| **E** | Yeifer | Estonia (E repetida) | `estonia` |
| **I** | Yeifer | Irlanda (I repetida) | `ireland` |
| **F** | Yeifer | Francia | `france` |
| **E** | Yeifer | Etiopía (E repetida) | `ethiopia` |
| **R** | Yeifer | Rusia | `russia` |

### 🛠️ Características del Proyecto
1. **Modelado Orientado a Objetos:** Datos encapsulados en la clase `Country` y servicios en `CountryAPI`. El módulo `main` no importa `requests`.
2. **Concurrencia:** Uso de `ThreadPoolExecutor` para realizar las 13 solicitudes HTTP en paralelo.
3. **Robustez:** Control de excepciones para caídas de internet o respuestas erróneas de la API.