import pygame
import random
import sys

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bible Pixel Quiz")
clock = pygame.time.Clock()


Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Blue = (0, 100, 255)
Red = (255, 50, 50)

Font = pygame.font.SysFont("consolas", 24)


events = {
    "Garden of Eden": [
        ("Who created the world?", "A", ["A) God", "B) Adam", "C) Moses", "D) Noah"]),
        ("First man created?", "B", ["A) Cain", "B) Adam", "C) Noah", "D) Abel"]),
        ("First woman created?", "C", ["A) Mary", "B) Ruth", "C) Eve", "D) Sarah"]),
        ("Forbidden fruit from which tree?", "D", ["A) Apple Tree", "B) Fig Tree", "C) Oak Tree", "D) Knowledge of Good and Evil"])
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


# class FallingPiece:
#     def __init__(self):
#         self.x = random.randint(100, 700)
#         self.y = 0
#         self.size = 20

#     def update(self):
#         self.y += 5

#     def draw(self):
#         pygame.draw.rect(screen, Green, (self.x, self.y, self.size, self.size))

# class PixelGuy:
#     def __init__(self):
#         self.x = 380
#         self.y = 500
#         self.frame = 0

#     def dance(self):
#         self.frame = (self.frame + 1) % 2

#     def draw(self):
#         color = Blue if self.frame == 0 else Red
#         pygame.draw.rect(screen, color, (self.x, self.y, 30, 30))


def ask_question(question, correct, answers):
    print("\n" + question)
    for ans in answers:
        print(ans)
    choice = input("Your answer (A/B/C/D): ").upper()
    return choice == correct


# pieces = []
# pixel_guy = PixelGuy()

for event_name, questions in events.items():
    print(f"\n=== {event_name} ===")
    for q, correct, options in questions:
        if ask_question(q, correct, options):
            print("Correct!")
            # pieces.append(FallingPiece())
            # pixel_guy.dance()
        else:
            print("Wrong!")

#         running = True
#         ticks = 0
#         while running:
#             screen.fill(Black)
#             for piece in pieces:
#                 piece.update()
#                 piece.draw()
#             pixel_guy.draw()
#             pygame.display.flip()
#             # clock.tick(30)
#             ticks += 1
#             if ticks > 30:
#                 running = False

print("\nGame Complete! Thanks for playing.")
pygame.quit()
sys.exit()