import random
import time
import sys
import os
from entities import Enemy
from ui_utils import get_selection
from database import QUESTIONS_DB, BOSSES
from constants import (JOURNEYS_DATA, ENEMIES_POOL, STATUS_LABEL, HISTORY_LABEL, 
                       ACTION_LABEL, BOLD, YELLOW, RED, GREEN, RESET, CYAN, MAGENTA, WHITE, BLUE)

class GameEngine:
    def __init__(self, player):
        self.player = player
        self.running = True
        self.chapter = 1
        self.stage = 1
        self.data = JOURNEYS_DATA[player.journey]
        self.story_flags = {"corrupcao": 0, "tecnica": 0}

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def slow_print(self, text, speed="normal"):
        speeds = {
            "fast": 0.005,
            "normal": 0.02,
            "slow": 0.05,
            "terminal": 0.01
        }
        delay = speeds.get(speed, 0.02)
        
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            if char in [".", "!", "?", ":"]:
                time.sleep(delay * 10)
            elif char == ",":
                time.sleep(delay * 4)
            else:
                time.sleep(delay)
        print()

    def describe_current_scene(self):
        biome = self.data["biomes"][self.chapter - 1]
        print(f"\n{HISTORY_LABEL}")
        
        if self.stage == 1:
            self.slow_print(f"Você acaba de entrar no {BOLD}{CYAN}{biome}{RESET}. O ar cheira a ozônio e silício.", "normal")
        elif self.stage < 5:
            self.slow_print(f"Explorando as profundezas do {biome}... Você nota rastros de código corrompido pelo chão.", "normal")
        elif self.stage == 5:
            self.slow_print(f"O clima no {biome} mudou drasticamente. Uma presença pesada bloqueia o caminho.", "slow")
        elif self.stage < 10:
            self.slow_print(f"A saída do {biome} parece próxima, mas os desafios técnicos estão se intensificando.", "normal")
        else:
            self.slow_print(f"Você alcançou o coração do {biome}. O núcleo do sistema está instável!", "fast")

    def process_turn(self):
        if self.player.hp <= 0:
            self.trigger_ending("MORTE")
            return

        self.clear_screen()
        print(f"\n {STATUS_LABEL} ".center(70, "—"))
        self.player.show_status()
        print(f"{BOLD}{self.player.journey} | CHAPTER {self.chapter} | STAGE {self.stage}/10{RESET}".center(70))
        print("—" * 70)

        # 1. Narrativa da Cena
        self.describe_current_scene()

        # 2. Lógica de Eventos
        if self.stage == 5:
            boss_name = BOSSES[self.player.journey][self.chapter-1]
            self.slow_print(f"\n{BOLD}{RED}⚠️ CONFLITO DE VERSÃO CRÍTICO: {boss_name} EMERGE!{RESET}", "fast")
            self.handle_combat(is_boss=True, boss_name=boss_name)
            self.stage += 1
        elif self.stage == 10:
            self.transition_chapter()
        else:
            # Sorteia entre combate narrativo ou desafio técnico
            if random.random() > 0.5:
                self.handle_combat()
            else:
                self.handle_quest()
            self.stage += 1

    def transition_chapter(self):
        self.clear_screen()
        if self.chapter == 3:
            self.trigger_ending("SUCESSO")
            return
            
        self.slow_print(f"\n{BOLD}{MAGENTA}>>> REFACTORING CONCLUÍDO NO CAPÍTULO {self.chapter} <<<{RESET}", "fast")
        if self.player.journey == "BACKEND":
            self.slow_print("O banco de dados está estável, mas a camada de infraestrutura pede socorro.", "normal")
        elif self.player.journey == "DEVOPS":
            self.slow_print("Os containers foram orquestrados, mas o monolito final ainda resiste.", "normal")
        elif self.player.journey == "FULLSTACK":
            self.slow_print("O Frontend está responsivo, agora é hora de conectar o núcleo da lógica.", "normal")
            
        self.chapter += 1
        self.stage = 1
        self.wait_input()

    def handle_quest(self):
        pool = QUESTIONS_DB[self.player.journey][self.player.seniority]
        q = random.choice(pool)
        
        # Construir o cabeçalho da questão para o get_selection não apagar
        header = f"\n{BOLD}{YELLOW}QUEST TÉCNICA:{RESET} Você encontrou um terminal com o seguinte erro:\n"
        header += f"\n{BOLD}Challenge [{self.player.seniority}]:{RESET}\n"
        header += f"{WHITE}{q['q']}{RESET}\n"
        
        ans_idx = get_selection(q["opts"], header=header)
        user_ans = ["A", "B", "C"][ans_idx]
        
        if user_ans == q["ans"]:
            self.slow_print(f"{GREEN}✔ Sucesso! Você otimizou o código. +2 Ataque / +50 EXP{RESET}", "fast")
            self.player.attack_power += 2
            self.player.gain_exp(50)
        else:
            self.slow_print(f"{RED}✘ Falha! O código quebrou em produção. -20 HP{RESET}", "fast")
            self.player.take_damage(20)
        self.wait_input()

    def handle_combat(self, is_boss=False, boss_name=None):
        if is_boss:
            enemy = Enemy(boss_name, 200 + (self.chapter * 50), 15 + (self.chapter * 5), 100, 500)
            self.slow_print(f"{RED}'Seu código não passará pelo meu Code Review!', ruge o {boss_name}.{RESET}", "slow")
        else:
            enemy_list = self.data["enemies"] + ENEMIES_POOL
            enemy_data = random.choice(enemy_list)
            enemy = Enemy(**enemy_data)
            self.slow_print(f"Um {BOLD}{RED}{enemy.name}{RESET} bloqueia sua thread de execução!", "terminal")

        while enemy.hp > 0 and self.player.hp > 0:
            hp_percent = (enemy.hp / enemy.max_hp) * 10
            enemy_bar = "█" * int(hp_percent) + "░" * (10 - int(hp_percent))
            
            header = f"\n{BOLD}{enemy.name}{RESET} [{RED}{enemy_bar}{RESET}] {enemy.hp}/{enemy.max_hp}\n"
            opts = [f"{GREEN}git push --force{RESET} (Atacar)", f"{CYAN}Analisar Logs{RESET} (Defesa)", f"{BLUE}Utilizar Café{RESET}"]
            
            # Navegação por setas no combate
            choice_idx = get_selection(opts, header=header)
            
            if choice_idx == 0: # Atacar
                dmg = random.randint(self.player.attack_power, self.player.attack_power + 10)
                enemy.hp -= dmg
                print(f"📡 Dano causado: {dmg}")
                time.sleep(0.5)
                if enemy.hp > 0: 
                    self.player.take_damage(enemy.attack)
                    time.sleep(1) # Espera para ler o dano sofrido
            elif choice_idx == 1: # Defesa
                self.slow_print("🛡️ Mitigando latência... Dano reduzido.", "fast")
                self.player.take_damage(enemy.attack // 4)
                time.sleep(1)
            elif choice_idx == 2: # Item
                if "Café Frio" in self.player.inventory:
                    self.player.hp = min(self.player.max_hp, self.player.hp + 30)
                    self.player.inventory.remove("Café Frio")
                    self.slow_print("☕ Café ingerido! Buffer de HP restaurado.", "fast")
                else:
                    self.slow_print("❌ Sem café no inventário!", "fast")
                time.sleep(1)
        
        if self.player.hp > 0:
            self.slow_print(f"🏆 {enemy.name} foi deletado da memória. Você coletou {enemy.gold} de ouro.", "normal")
            self.player.gain_exp(enemy.exp)
            self.player.gold += enemy.gold
            self.wait_input()

    def trigger_ending(self, result):
        self.clear_screen()
        if result == "MORTE":
            self.slow_print(f"{BOLD}{RED}RUNTIME ERROR: Your Life Process Terminated with Exit Code 1.{RESET}", "slow")
            self.slow_print("Syntaxia foi consumida pelo código legado... mas quem sabe uma nova instância ajude?", "normal")
        else:
            self.slow_print(f"{BOLD}{GREEN}DEPLOY SUCESSFUL! REINO DE SYNTAXIA SALVO!{RESET}", "fast")
            self.slow_print(f"Parabéns, {self.player.name}. Você provou ser um {self.player.job_class} lendário.", "normal")
            self.slow_print("O sistema agora roda com 99.9% de uptime graças a você.", "normal")
            
        self.running = False
        input("\n[ Pressione Enter para fechar o Terminal ]")

    def get_choice(self, options):
        # Apenas para compatibilidade se necessário, mas get_selection é o padrão agora
        return str(get_selection(options) + 1)

    def wait_input(self):
        input(f"\n{BOLD}[ Pressione Enter para continuar a jornada... ]{RESET}")
