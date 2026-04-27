import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bible Monument Builder - Pixel Art")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
BLUE = (0, 120, 255)
GRAY = (120, 120, 120)
YELLOW = (255, 255, 0)

FONT = pygame.font.SysFont("consolas", 20)


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

# ==========================
# Pixel Art Pieces (Each event has 4 pieces)
# ==========================
def draw_piece(surface, event, x, y, part):
    size = 40

    try:
        if event == "Noah's Ark":
            pygame.draw.rect(surface, BROWN, (x, y, size, size//2))

        elif event == "Parting of the Red Sea":
            pygame.draw.rect(surface, BLUE, (x, y, size, size))

        elif event == "David and Goliath":
            pygame.draw.rect(surface, GRAY, (x, y, size, size))

        elif event == "Jonah and the Whale":
            pygame.draw.ellipse(surface, BLUE, (x, y, size, size//2))

        elif event == "Garden of Eden":
            pygame.draw.circle(surface, (0,200,0), (x+20, y+20), 15)

        elif event == "Jesus Death and Resurrection":
            pygame.draw.rect(surface, YELLOW, (x+15, y, 10, 40))
            pygame.draw.rect(surface, YELLOW, (x, y+15, 40, 10))

        else:
            raise Exception("Unknown event")

    except:
        # Backup placeholder
        pygame.draw.rect(surface, GRAY, (x, y, size, size), 2)


class FallingPiece:
    def __init__(self, target_x, target_y, event, part):
        self.x = target_x
        self.y = 0
        self.target_y = target_y
        self.event = event
        self.part = part
        self.landed = False

    def update(self):
        if not self.landed:
            self.y += 6
            if self.y >= self.target_y:
                self.y = self.target_y
                self.landed = True

    def draw(self):
        draw_piece(screen, self.event, self.x, self.y, self.part)

class Monument:
    def __init__(self, event):
        self.event = event
        self.positions = [(300,400),(340,400),(300,440),(340,440)]
        self.pieces = []

    def add_piece(self):
        if len(self.pieces) < 4:
            pos = self.positions[len(self.pieces)]
            self.pieces.append(FallingPiece(pos[0], pos[1], self.event, len(self.pieces)))

    def update(self):
        for p in self.pieces:
            p.update()

    def draw(self):
        if not self.pieces:
            pygame.draw.rect(screen, GRAY, (300, 400, 80, 80), 2)
        for p in self.pieces:
            p.draw()


def ask_question(screen, question, answers, correct):
    waiting = True
    while waiting:
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
                    return key == correct

for event_name, questions in events.items():
    monument = Monument(event_name)

    for q, correct, options in questions:
        correct_answer = ask_question(screen, q, options, correct)

        if correct_answer:
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
