import pygame

from src.ui.UIPanel import UIPanel


class UIManager:
    def __init__(self, window_size: tuple[int, int]):
        self.window_size = window_size
        self.panels: dict[UIPanel, bool] = {}

    def add_panel(self, panel: UIPanel):
        self.panels[panel] = False

    def toggle_active(self, panel: UIPanel):
        self.panels[panel] = not self.panels[panel]

    def render_self(self, surface: pygame.Surface):
        active_panels: list[UIPanel] = [panel for panel, active in self.panels.items() if active]
        for panel in active_panels:
            x = (self.window_size[0] - panel.dimensions[0]) // 2
            y = (self.window_size[1] - panel.dimensions[1]) // 2
            panel.render_self(surface, (x, y))
