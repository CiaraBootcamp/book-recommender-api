# personality.py
from fastapi import APIRouter, Body
from pydantic import BaseModel
from typing import List

router = APIRouter()

class BigFiveResponse(BaseModel):
    O: int  # Apertura
    C: int  # Responsabilidad
    E: int  # Extraversión
    A: int  # Amabilidad
    N: int  # Neuroticismo

@router.post("/personality-test")
def submit_personality(profile: BigFiveResponse):
    return {"message": "Perfil psicológico generado", "personality": profile}