from fastapi import APIRouter
import requests as api
pokemon = APIRouter(prefix='/pokemon')

base_url = "https://pokeapi.co/api/v2/pokemon"

@pokemon.get('/')
def get_all():
	try:
		result = api.get(f"{base_url}")
		return result.json()
	except:
		return {}
@pokemon.get('/{pokemon_id}')
def get_one(pokemon_id: str):
	try:
		result = api.get(f"{base_url}/{pokemon_id}").json()
		return {
			"id": result['id'],
			"name": result["name"],
			"img": result['sprites']['front_default'],
			"types": result['types']
		}
	except:
		return {}