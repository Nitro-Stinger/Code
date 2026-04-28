import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bible Monument Builder - Image Version")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (120, 120, 120)

FONT = pygame.font.SysFont("consolas", 20)
BIG_FONT = pygame.font.SysFont("consolas", 40)

events = {
    "Garden of Eden": [
        ("Who created the world?", "A", ["A) God", "B) Adam", "C) Moses", "D) Noah"]),
        ("First man created?", "B", ["A) Cain", "B) Adam", "C) Noah", "D) Abel"]),
        ("First woman created?", "C", ["A) Mary", "B) Ruth", "C) Eve", "D) Sarah"]),
        ("Forbidden fruit from which tree?", "D", ["A) Apple Tree", "B) Fig Tree", "C) Oak Tree", "D) Knowledge"])
    ],
    "Parting of the Red Sea": [
        ("Who led Israelites?", "A", ["A) Moses", "B) Joshua", "C) Aaron", "D) David"]),
        ("Sea parted by?", "B", ["A) Staff", "B) God", "C) Wind", "D) Soldiers"]),
        ("Enemies pursuing?", "C", ["A) Babylonians", "B) Romans", "C) Egyptians", "D) Philistines"]),
        ("Miracle showed God's?", "D", ["A) Anger", "B) Fear", "C) Weakness", "D) Power"])
    ],
    "David and Goliath": [
        ("Young hero?", "A", ["A) David", "B) Saul", "C) Jonathan", "D) Samuel"]),
        ("Weapon used?", "B", ["A) Sword", "B) Sling", "C) Spear", "D) Bow"]),
        ("Goliath was a?", "C", ["A) King", "B) Prophet", "C) Giant", "D) Soldier"]),
        ("Victory by?", "D", ["A) Luck", "B) Army", "C) Armor", "D) Faith"])
    ],
    "Jonah and the Whale": [
        ("Who ran from God?", "A", ["A) Jonah", "B) Noah", "C) Moses", "D) Paul"]),
        ("Swallowed by?", "B", ["A) Shark", "B) Whale", "C) Dragon", "D) Fish"]),
        ("Days inside?", "C", ["A) 1", "B) 2", "C) 3", "D) 7"]),
        ("Jonah preached in?", "D", ["A) Rome", "B) Egypt", "C) Israel", "D) Nineveh"])
    ],
    "Noah's Ark": [
        ("Built the ark?", "A", ["A) Noah", "B) Abraham", "C) Moses", "D) Jacob"]),
        ("Animals came by?", "B", ["A) Singles", "B) Pairs", "C) Threes", "D) Fours"]),
        ("Rain lasted?", "C", ["A) 10 days", "B) 20 days", "C) 40 days", "D) 100 days"]),
        ("Sign of promise?", "D", ["A) Fire", "B) Wind", "C) Star", "D) Rainbow"])
    ],
    "Jesus Death and Resurrection": [
        ("Who betrayed Jesus?", "A", ["A) Judas", "B) Peter", "C) John", "D) Pilate"]),
        ("Jesus died on a?", "B", ["A) Tree", "B) Cross", "C) Rock", "D) Throne"]),
        ("Rose on which day?", "C", ["A) 1st", "B) 2nd", "C) 3rd", "D) 7th"]),
        ("Jesus rose to bring?", "D", ["A) War", "B) Fear", "C) Wealth", "D) Salvation"])
    ]
}

def load_and_split(image_path):
    try:
        img = pygame.image.load(image_path).convert_alpha()
        w, h = img.get_width(), img.get_height()

        pieces = [
            img.subsurface((0, 0, w//2, h//2)),
            img.subsurface((w//2, 0, w//2, h//2)),
            img.subsurface((0, h//2, w//2, h//2)),
            img.subsurface((w//2, h//2, w//2, h//2))
        ]
        return pieces
    except:
        return None

image_files = {
    "Garden of Eden": "eden.png",
    "Parting of the Red Sea": "redsea.png",
    "David and Goliath": "david.png",
    "Jonah and the Whale": "whale.png",
    "Noah's Ark": "ark.png",
    "Jesus Death and Resurrection": "cross.png"
}

class FallingPiece:
    def __init__(self, image, target_x, target_y):
        self.image = image
        self.x = target_x
        self.y = 0
        self.target_y = target_y
        self.landed = False

    def update(self):
        if not self.landed:
            self.y += 6
            if self.y >= self.target_y:
                self.y = self.target_y
                self.landed = True

    def draw(self):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, GRAY, (self.x, self.y, 40, 40), 2)

class Monument:
    def __init__(self, event):
        self.positions = [(250,200),(450,200),(250,350),(450,350)]
        self.pieces = []
        self.images = load_and_split(image_files.get(event, ""))

    def add_piece(self):
        index = len(self.pieces)
        if index < 4:
            img = self.images[index] if self.images else None
            pos = self.positions[index]
            self.pieces.append(FallingPiece(img, pos[0], pos[1]))

    def update(self):
        for p in self.pieces:
            p.update()

    def draw(self):
        if not self.pieces:
            pygame.draw.rect(screen, GRAY, (250,200,300,300), 2)
        for p in self.pieces:
            p.draw()


def ask_question(screen, question, answers, correct):
    while True:
        screen.fill(BLACK)
        y = 100
        screen.blit(FONT.render(question, True, WHITE), (50, y))

        for ans in answers:
            y += 40
            screen.blit(FONT.render(ans, True, WHITE), (50, y))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key).upper()
                if key in ["A","B","C","D"]:
                    if key == correct:
                        return True
                    else:
                        show_wrong(screen)


def show_wrong(screen):
    timer = 0
    while timer < 60:
        screen.fill(BLACK)
        text = BIG_FONT.render("WRONG", True, RED)
        screen.blit(text, (WIDTH//2 - 100, HEIGHT//2 - 50))
        pygame.display.flip()
        clock.tick(60)
        timer += 1


for event_name, questions in events.items():
    monument = Monument(event_name)

    for q, correct, options in questions:
        ask_question(screen, q, options, correct)
        monument.add_piece()

        animating = True
        while animating:
            screen.fill(BLACK)

            monument.update()
            monument.draw()

            pygame.display.flip()
            clock.tick(60)

            if all(p.landed for p in monument.pieces):
                animating = False

print("Game Finished")
pygame.quit()
sys.exit()