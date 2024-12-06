from dataclasses import dataclass

@dataclass
class airport:
    id_aerodromo: int
    sg_icao: str
    sg_iata: str
    nm_aerodromo: str
    nm_municipio: str
    sg_uf: str
    nm_regiao: str
    nm_pais: str
    nm_continente: str
