from dataclasses import dataclass

@dataclass
class authClass:
    server: str
    database: str
    username: str
    schema: str
    warehouse: str
    role: str
    authenticator: str
    conn: object = None

def get_auth_data():
    return {
        "server": "zd49589.east-us-2.azure",
        "database": "SANDBOX_AZULCARGO",
        "username": "bruno.droguett@voeazul.com.br",
        "schema": "ANACBR",
        "warehouse": "AZULCARGO_WH",
        "role": "AZULCARGO_USERS",
        "authenticator": "externalbrowser"
    }

