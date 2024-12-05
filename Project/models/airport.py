from dataclasses import dataclass

@dataclass
class airport:
    id_aerodromo: int = None
    sg_icao: str = None
    sg_iata: str = None
    nm_aerodromo: str = None
    nm_municipio: str = None
    sg_uf: str = None
    nm_regiao: str = None
    nm_pais: str = None
    nm_continente: str = None
