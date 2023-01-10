from pydantic import BaseModel

class PokemonBaseSchema(BaseModel):
	id: int|None = None
	seen: bool = False
	catch: bool = False
	class Config:
		orm_mode = True
		allow_population_by_field_name = True
		arbitrary_types_allowed = True
