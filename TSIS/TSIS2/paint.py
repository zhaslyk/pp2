import pygame
import os
from datetime import datetime
from tools import draw_shape, flood_fill

class PaintApp:
    def __init__(self):
        pygame.init()
        
        self.WIDTH, self.HEIGHT = 1000, 700
        self.TOOLBAR_H = 100
        self.FPS = 60
        
        self.CLR_BG = (30, 30, 35)       
        self.CLR_CANVAS = (255, 255, 255)
        self.CLR_UI_BAR = (45, 45, 50)
        self.CLR_BTN = (60, 60, 65)
        self.CLR_BTN_ACTIVE = (80, 110, 255)
        self.CLR_TXT = (220, 220, 220)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Paint")
        self.clock = pygame.time.Clock()
        
        self.canvas = pygame.Surface((self.WIDTH, self.HEIGHT - self.TOOLBAR_H))
        self.canvas.fill(self.CLR_CANVAS)
        
        self.font_sm = pygame.font.SysFont("Arial", 14)
        self.font_lg = pygame.font.SysFont("Arial", 32)

        self.tool = "pencil"
        self.color = (0, 0, 0)
        self.size = 5
        self.drawing = False
        self.start_pos = None
        self.last_pos = None
        
        self.text_mode = False
        self.text_pos = None
        self.text_val = ""

        self.tools = ["pencil", "line", "rectangle", "circle", "square", 
                      "right_triangle", "equilateral_triangle", "rhombus", 
                      "eraser", "fill", "text"]
        
        self.palette = [(0, 0, 0), (255, 50, 50), (50, 200, 50), (50, 100, 255), 
                        (255, 200, 0), (255, 100, 0), (180, 50, 255), (255, 255, 255)]

    def to_canvas_coords(self, pos):
        return pos[0], pos[1] - self.TOOLBAR_H

    def check_on_canvas(self, pos):
        return self.TOOLBAR_H <= pos[1] < self.HEIGHT

    def save_work(self):
        if not os.path.exists("saves"): os.makedirs("saves")
        fname = f"saves/paint_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pygame.image.save(self.canvas, fname)
        print(f"Project Saved: {fname}")

    def render_ui(self):
        pygame.draw.rect(self.screen, self.CLR_UI_BAR, (0, 0, self.WIDTH, self.TOOLBAR_H))
        
        x, y = 10, 10
        for t in self.tools:
            btn_rect = pygame.Rect(x, y, 85, 35)
            active = (self.tool == t)
            
            color = self.CLR_BTN_ACTIVE if active else self.CLR_BTN
            pygame.draw.rect(self.screen, color, btn_rect, border_radius=4)
            pygame.draw.rect(self.screen, self.CLR_TXT, btn_rect, 1, border_radius=4)
            
            lbl = self.font_sm.render(t.replace("_", " "), True, self.CLR_TXT)
            self.screen.blit(lbl, lbl.get_rect(center=btn_rect.center))
            
            x += 90
            if x + 90 > self.WIDTH: x, y = 10, y + 40

        sx = 10
        for c in self.palette:
            c_rect = pygame.Rect(sx, 70, 30, 25)
            pygame.draw.rect(self.screen, c, c_rect)
            border_clr = (255, 255, 255) if self.color == c else (0, 0, 0)
            pygame.draw.rect(self.screen, border_clr, c_rect, 2 if self.color == c else 1)
            sx += 35

        self.size_rects = []
        for i, (s, n) in enumerate([(2, "S"), (5, "M"), (12, "L")]):
            r = pygame.Rect(300 + (i * 45), 70, 40, 25)
            self.size_rects.append((r, s))
            pygame.draw.rect(self.screen, self.CLR_BTN_ACTIVE if self.size == s else self.CLR_BTN, r)
            pygame.draw.rect(self.screen, self.CLR_TXT, r, 1)
            lbl = self.font_sm.render(n, True, self.CLR_TXT)
            self.screen.blit(lbl, lbl.get_rect(center=r.center))

    def run(self):
        running = True
        while running:
            self.screen.fill(self.CLR_BG)
            preview_surf = self.canvas.copy()

            if self.drawing and self.start_pos and self.last_pos:
                if self.tool == "line":
                    pygame.draw.line(preview_surf, self.color, self.start_pos, self.last_pos, self.size)
                elif self.tool in self.tools[2:8]: # Shapes
                    draw_shape(preview_surf, self.tool, self.start_pos, self.last_pos, self.color, self.size)

            self.screen.blit(preview_surf, (0, self.TOOLBAR_H))

            if self.text_mode and self.text_pos:
                txt = self.font_lg.render(self.text_val + "|", True, self.color)
                self.screen.blit(txt, (self.text_pos[0], self.text_pos[1] + self.TOOLBAR_H))

            self.render_ui()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    mods = pygame.key.get_mods()
                    if event.key == pygame.K_s and (mods & pygame.KMOD_CTRL or mods & pygame.KMOD_META):
                        self.save_work()
                    
                    if self.text_mode:
                        if event.key == pygame.K_RETURN:
                            if self.text_val: self.canvas.blit(self.font_lg.render(self.text_val, True, self.color), self.text_pos)
                            self.text_mode = False
                        elif event.key == pygame.K_BACKSPACE: self.text_val = self.text_val[:-1]
                        elif event.key == pygame.K_ESCAPE: self.text_mode = False
                        else: self.text_val += event.unicode

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[1] < self.TOOLBAR_H:
                        x, y = 10, 10
                        for t in self.tools:
                            if pygame.Rect(x, y, 85, 35).collidepoint(event.pos):
                                self.tool, self.text_mode = t, False
                            x += 90
                            if x + 90 > self.WIDTH: x, y = 10, y + 40
                        
                        sx = 10
                        for c in self.palette:
                            if pygame.Rect(sx, 70, 30, 25).collidepoint(event.pos): self.color = c
                            sx += 35
                        
                        for r, s in self.size_rects:
                            if r.collidepoint(event.pos): self.size = s
                    
                    elif self.check_on_canvas(event.pos):
                        p = self.to_canvas_coords(event.pos)
                        if self.tool == "fill": flood_fill(self.canvas, p, self.color)
                        elif self.tool == "text": self.text_mode, self.text_pos, self.text_val = True, p, ""
                        else: self.drawing, self.start_pos, self.last_pos = True, p, p

                if event.type == pygame.MOUSEMOTION and self.drawing:
                    p = self.to_canvas_coords(event.pos)
                    if self.tool in ["pencil", "eraser"]:
                        c = (255, 255, 255) if self.tool == "eraser" else self.color
                        pygame.draw.line(self.canvas, c, self.last_pos, p, self.size)
                    self.last_pos = p

                if event.type == pygame.MOUSEBUTTONUP and self.drawing:
                    p = self.to_canvas_coords(event.pos)
                    if self.tool == "line": pygame.draw.line(self.canvas, self.color, self.start_pos, p, self.size)
                    elif self.tool in self.tools[2:8]: draw_shape(self.canvas, self.tool, self.start_pos, p, self.color, self.size)
                    self.drawing = False

            pygame.display.flip()
            self.clock.tick(self.FPS)
        pygame.quit()

if __name__ == "__main__":
    app = PaintApp()
    app.run()