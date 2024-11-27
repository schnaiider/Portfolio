
from dataclasses import dataclass

@dataclass
class processFiles:
    urlBase: str
    period: str
    year: int
    fullPath: str 
    
    def __str__(self):
        return f"{self.fullPath}"
    
