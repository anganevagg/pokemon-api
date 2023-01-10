from fastapi import APIRouter, HTTPException, Depends
from ..database import get_db
from sqlalchemy.orm import Session
from ..models.pokemon import Pokemon
from ..schemas.pokemon import PokemonBaseSchema

pokedex = APIRouter(prefix='/pokedex')

lists = {}

@pokedex.get('/seen')
def get_seen(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
	skip = (page - 1) * limit
	pokemons = db.query(Pokemon).filter(Pokemon.seen == True).limit(limit).offset(skip).all()
	return {
		"data": pokemons
	}

@pokedex.put('/seen')
def set_seen(pokemon: PokemonBaseSchema, db: Session = Depends(get_db)):
	try:
		query = db.query(Pokemon).filter(Pokemon.id==pokemon.id)
		pokemon_found = query.first()
		if not pokemon_found:
			pokemon_found = Pokemon(**pokemon.dict())
			db.add(pokemon_found)
		pokemon_found.seen = True
		update_data = pokemon.dict(exclude_unset=True)
		query.filter(Pokemon.id == pokemon_found.id).update(update_data, synchronize_session=False)
		db.commit()
		db.refresh(pokemon_found)
		return {
			"status": "success"
		}
	except:
		raise HTTPException(500, "Error saving pokemon")
	
@pokedex.get('/catch')
def get_catch(db: Session = Depends(get_db), limit: int = 10, page: int = 1):
	skip = (page - 1) * limit
	pokemons = db.query(Pokemon).filter(Pokemon.catch == True).limit(limit).offset(skip).all()

	return {
		"data": pokemons
	}

@pokedex.put('/catch')
def set_catch(pokemon: PokemonBaseSchema, db: Session = Depends(get_db)):
	try:
		query = db.query(Pokemon).filter(Pokemon.id==pokemon.id)
		pokemon_found = query.first()
		if not pokemon_found:
			pokemon_found = Pokemon(**pokemon.dict())
			db.add(pokemon_found)
		pokemon_found.seen = True
		pokemon_found.catch = True
		update_data = pokemon.dict(exclude_unset=True)
		query.filter(Pokemon.id == pokemon_found.id).update(update_data, synchronize_session=False)
		db.commit()
		db.refresh(pokemon_found)
		return {
			"status": "success"
		}
	except:
		raise HTTPException(500, "Error saving pokemon")