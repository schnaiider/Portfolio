from dataclasses import dataclass

@dataclass
class company:
    id_empresa: int
    sg_empresa_icao: str
    sg_empresa_iata: str
    nm_empresa: str
    nm_pais: str
