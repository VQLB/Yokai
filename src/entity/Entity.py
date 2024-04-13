import pygame

from uuid import UUID
import uuid

class Entity:
    def __init__(self, id: UUID | None = None):
        if not id:
            id = uuid.uuid4()
        self.id = id

    def render_self(self, surface: pygame.Surface):
        raise RuntimeError("render_self isn't implemented for this entity")

