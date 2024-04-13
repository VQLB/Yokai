from src.entity.Entity import Entity
from uuid import UUID
class Character(Entity):
    def __init__(self, texturePath: str,id: UUID | None = None):
        super().__init__(texturePath, id)

