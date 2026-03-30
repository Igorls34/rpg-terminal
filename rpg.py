import random
import time
import sys

class Player:
    def __init__(self, name, job_class):
        self.name = name
        self.job_class = job_class
        self.hp = 100
        self.max_hp = 100
        self.level = 1
        self.gold = 10
        self.exp = 0
        self.exp_to_level = 50
        self.inventory = ["Teclado de Madeira", "Café Frio", "Documentação Desatualizada"]
        self.attack_power = 10

    def show_status(self):
        print("\n" + "📊 Status do Personagem:".center(50))
        print(f"HP: [{self.hp}/{self.max_hp}] | Nível: [{self.level}] | Ouro: [{self.gold}]")
        print(f"Inventário: {', '.join(self.inventory)}")
        print("-" * 50)

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
        self.attack = attack
        self.gold = gold
        self.exp = exp

class Game:
    def __init__(self):
        self.player = None
        self.running = True

    def clear_screen(self):
        print("\n" * 5)

    def start(self):
        print("=== BEM-VINDO AO RPG SYNTAXIA (MEDIEVAL DEV) ===")
        name = input("Digite o nome do seu Developer: ") or "Developer"
        job = input("Digite sua classe (ex: Junior Backend): ") or "Junior Backend"
        self.player = Player(name, job)
        
        self.game_loop()

    def game_loop(self):
        while self.running:
            if self.player.hp <= 0:
                print("\n💀 GAME OVER! Seu código deu SEGFAULT na vida real.")
                self.running = False
                break
                
            self.player.show_status()
            self.generate_scene()

    def generate_scene(self):
        # Biomes e eventos procedurais simples
        biomes = [
            "Floresta dos Loops Infinitos",
            "Deserto de Dados Sem Estrutura",
            "Montanha do Stack Overflow",
            "Pântano dos Bugs de Legado"
        ]
        current_biome = random.choice(biomes)
        
        events = [
            {"desc": f"Você encontrou um Bug Selvagem no {current_biome}!", "type": "combat"},
            {"desc": f"Você encontrou um Baú de Código Aberto no {current_biome}!", "type": "loot"},
            {"desc": f"Um NPC Senior aparece e te dá um Code Review útil.", "type": "heal"},
            {"desc": f"A documentação no {current_biome} está errada. Você se perdeu.", "type": "trap"}
        ]
        
        event = random.choice(events)
        
        print("\n📖 História / Cena Atual:")
        print(event["desc"])
        
        if event["type"] == "combat":
            self.handle_combat()
        elif event["type"] == "loot":
            gold_found = random.randint(5, 20)
            self.player.gold += gold_found
            print(f"💰 Você encontrou {gold_found} de Ouro!")
            self.wait_input()
        elif event["type"] == "heal":
            self.player.hp = min(self.player.max_hp, self.player.hp + 20)
            print("💖 Você se sente mais otimizado. HP recuperado!")
            self.wait_input()
        elif event["type"] == "trap":
            self.player.take_damage(15)
            self.wait_input()

    def handle_combat(self):
        enemies = [
            Enemy("NullPointerException", 30, 10, 10, 20),
            Enemy("Zombie Process", 40, 8, 15, 25),
            Enemy("Merge Conflict", 50, 15, 30, 40)
        ]
        enemy = random.choice(enemies)
        print(f"⚔️ Um {enemy.name} apareceu! (HP: {enemy.hp})")
        
        while enemy.hp > 0 and self.player.hp > 0:
            print(f"\n[HP do Inimigo: {enemy.hp}]")
            print("1. Atacar (git commit -m 'fix')")
            print("2. Fugir (ctrl+c)")
            print("3. Usar Café Frio (Cura 20 HP)")
            
            choice = input("\nO que você faz? ")
            
            if choice == "1":
                damage = random.randint(self.player.attack_power - 2, self.player.attack_power + 5)
                enemy.hp -= damage
                print(f"⚔️ Você atacou o {enemy.name} e causou {damage} de dano!")
                
                if enemy.hp > 0:
                    enemy_damage = random.randint(enemy.attack - 3, enemy.attack + 2)
                    self.player.take_damage(enemy_damage)
            elif choice == "2":
                print("🏃 Você fugiu da thread de combate!")
                return
            elif choice == "3":
                if "Café Frio" in self.player.inventory:
                    self.player.hp = min(self.player.max_hp, self.player.hp + 20)
                    self.player.inventory.remove("Café Frio")
                    print("☕ Café Frio ingerido. HP +20!")
                else:
                    print("❌ Você não tem mais Café!")
            else:
                print("⌨️ Comando desconhecido. Você hesitou e o inimigo atacou!")
                self.player.take_damage(enemy.attack)

        if self.player.hp > 0:
            print(f"🏆 Você derrotou o {enemy.name}!")
            self.player.gold += enemy.gold
            self.player.gain_exp(enemy.exp)
            self.wait_input()

    def wait_input(self):
        input("\n[Pressione Enter para continuar...]")

if __name__ == "__main__":
    game = Game()
    game.start()
