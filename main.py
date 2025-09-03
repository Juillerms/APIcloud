from fastapi import FastAPI, Request
app = FastAPI()

@app.get("/ola/{nome}")
async def ola_nome(nome: str):
    return {"mensagem": f"Olá, {nome}! Bem-vindo(a)!"}

@app.get("/me")
async def identify_me(request: Request):
    client_ip = request.client.host if request.client else "desconhecido"
    user_agent = request.headers.get("user-agent", "desconhecido")
    
    return {
        "seu_endereco_ip": client_ip,
        "seu_navegador_ou_cliente": user_agent
    }
