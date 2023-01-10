from fastapi import APIRouter, Header, HTTPException
from .pokemon import pokemon
from .pokedex import pokedex

router = APIRouter(prefix='/api', tags=['Pokemon'])

router.include_router(pokemon)
router.include_router(pokedex)