def enum(**enums):
	return type('Enum', (), enums)

STATES = enum(ALIVE=1, DEAD=0)