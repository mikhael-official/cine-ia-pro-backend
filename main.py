import os
import replicate
from fastapi import FastAPI, Body

# INTEGRANDO SEU TOKEN DIRETAMENTE
os.environ["REPLICATE_API_TOKEN"] = "R8_V5HvuMePFdqc5H4RUVaHtLo4i9hsuoH0D0pMw"

app = FastAPI()

@app.post("/criar_animacao")
async def criar_animacao(prompt: str = Body(..., embed=True), estilo: str = Body(..., embed=True)):
    """
    Este endpoint cria desenhos e filmes usando o seu token.
    Se o estilo for 'bíblico', ele foca em realismo. 
    Se for 'desenho', ele foca no estilo Pica-Pau/Tom & Jerry.
    """
    
    # Refinando o prompt para qualidade profissional de 2026
    prompt_completo = f"High-quality {estilo} animation, professional cinematography, 4k, vibrant colors, {prompt}"
    
    # Chamando o modelo Wan-2.1 (o mais potente para vídeos rápidos na Replicate hoje)
    output = replicate.run(
        "wan-video/wan-2.1-t2v-480p", 
        input={
            "prompt": prompt_completo,
            "aspect_ratio": "9:16", # Formato vital para redes sociais
            "num_frames": 81        # Duração otimizada
        }
    )
    
    return {"url_video": output}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
