# Load environment variables first
import os
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import screenshot, generate_code, home, evals

app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)

# --- INÍCIO DA CORREÇÃO DE CORS ---

# Lista de domínios permitidos.
# Adicionamos a URL do seu frontend a partir de uma variável de ambiente para ser seguro em produção.
origins = [
    # Permite o desenvolvimento local
    "http://localhost",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    # Permite o seu frontend em produção
    os.environ.get("FRONTEND_DOMAIN_URL") 
]

# Filtra valores None caso a variável de ambiente não esteja definida
allowed_origins = [origin for origin in origins if origin]

# Se por algum motivo nenhuma origem for definida, usa o valor original como fallback
if not allowed_origins:
    allowed_origins = ["*"]


# Configure CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins, # Usa a lista de origens permitidas
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- FIM DA CORREÇÃO DE CORS ---


# Add routes
app.include_router(generate_code.router)
app.include_router(screenshot.router)
app.include_router(home.router)
app.include_router(evals.router)
