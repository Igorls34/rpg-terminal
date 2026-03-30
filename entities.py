# Classes que definem os seres do mundo de Syntaxia

class Player:
    def __init__(self, name, seniority, journey):
        self.name = name
        self.seniority = seniority # JUNIOR, PLENO, SENIOR
        self.journey = journey
        
        # Definição de atributos por dificuldade
        if seniority == "JUNIOR":
            self.hp = 150
            self.max_hp = 150
            self.attack_power = 15
            self.gold = 20
        elif seniority == "SENIOR":
            self.hp = 70
            self.max_hp = 70
            self.attack_power = 8
            self.gold = 0
        else: # PLENO
            self.hp = 100
            self.max_hp = 100
            self.attack_power = 10
            self.gold = 10

        self.job_class = f"{seniority.capitalize()} {journey.capitalize()}"
        self.level = 1
        self.exp = 0
        self.exp_to_level = 50
        self.inventory = ["Teclado de Madeira", "Café Frio"]

    def show_status(self):
        from constants import GREEN, RED, RESET, YELLOW, CYAN, BOLD
        
        # Barra de HP visual
        hp_percent = (self.hp / self.max_hp) * 20
        hp_bar = "█" * int(hp_percent) + "░" * (20 - int(hp_percent))
        hp_color = GREEN if self.hp > (self.max_hp * 0.4) else (YELLOW if self.hp > (self.max_hp * 0.2) else RED)
        
        print(f"{BOLD}NOME:{RESET} {self.name} | {BOLD}CLASSE:{RESET} {self.job_class}")
        print(f"{BOLD}HP:{RESET} [{hp_color}{hp_bar}{RESET}] {self.hp}/{self.max_hp}")
        print(f"{BOLD}LVL:{RESET} {self.level} | {BOLD}GOLD:{RESET} {YELLOW}{self.gold}{RESET} | {BOLD}EXP:{RESET} {self.exp}/{self.exp_to_level}")
        print(f"{BOLD}INVENTÁRIO:{RESET} {', '.join(self.inventory)}")

    def gain_exp(self, amount):
        self.exp += amount
        print(f"✨ Ganhou {amount} EXP!")
        if self.exp >= self.exp_to_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp -= self.exp_to_level
        self.exp_to_level = int(self.exp_to_level * 1.5)
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack_power += 5
        print(f"🆙 LEVEL UP! Agora você é Nível {self.level}!")

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0
        print(f"💥 Você sofreu {amount} de dano!")

class Enemy:
    def __init__(self, name, hp, attack, gold, exp):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.gold = gold
        self.exp = exp
