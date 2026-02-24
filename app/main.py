from fastapi import FastAPI, HTTPException
from core_utils.validators import validate_email, validate_not_empty
from core_utils.exceptions import ValidationError
from core_utils.logger import get_logger
from app.config import settings

app = FastAPI(title=settings.app_name)
logger = get_logger(__name__)

@app.get("/")
def root():
    logger.info("Ambiente: %s", settings.app_name)
    return {
        "message": "API funcionando",
        "enviroment": settings.environment
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