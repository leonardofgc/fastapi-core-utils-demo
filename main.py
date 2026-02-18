from fastapi import FastAPI, HTTPException
from core_utils.validators import validate_email, validate_not_empty
from core_utils.exceptions import ValidationError
from core_utils.logger import get_logger

app = FastAPI()
logger = get_logger(__name__)

@app.get("/")
def root():
    logger.info("API Iniciada")
    return {
        "message": "API funcionando"
    }

@app.post("/users")
def create_user(name: str, email: str):
    try:
        name = validate_not_empty(name, "name")
        email = validate_email(email)

        logger.info("Usuário validado com sucesso: %s", email)

        return{
            "message": "Usuário criado com sucesso",
            "name": name,
            "email": email,
        }
    except ValidationError as e:
        logger.warning("Erro de validação: %s", str(e))
        raise HTTPException(status_code=400, detail=str(e))