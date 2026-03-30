import time
import os
import sys
from entities import Player
from engine import GameEngine
from ui_utils import get_selection
from constants import HEADER, BOLD, GREEN, CYAN, RED, RESET, MAGENTA, YELLOW

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def boot_sequence():
    clear_screen()
    slow_print(f"{GREEN}[ OK ] Booting Syntaxia Kernel 5.10.0-backend...{RESET}")
    time.sleep(0.3)
    slow_print(f"{GREEN}[ OK ] Initializing Logic Engines...{RESET}")
    time.sleep(0.3)
    slow_print(f"{GREEN}[ OK ] Loading Legacy Bug Database...{RESET}")
    time.sleep(0.3)
    slow_print(f"{GREEN}[ OK ] Mounting /dev/brain...{RESET}")
    time.sleep(0.5)
    print(f"\n{BOLD}{CYAN}SISTEMA PRONTO PARA EXECUÇÃO.{RESET}\n")
    time.sleep(0.8)

def show_about():
    clear_screen()
    print(f"{BOLD}{MAGENTA}─── DOCUMENTAÇÃO DO SISTEMA SYNTAXIA ───{RESET}")
    slow_print(f"\n{BOLD}O MUNDO:{RESET}")
    print("Syntaxia é um reino construído sobre camadas de código legado.")
    print("O Grande Servidor do Norte, que mantinha a estabilidade, foi corrompido.")
    
    slow_print(f"\n{BOLD}SUA MISSÃO:{RESET}")
    print("Como um Developer, você deve atravessar biomas perigosos,")
    print("resolver desafios de lógica e derrotar o monstro final da sua trilha.")
    
    slow_print(f"\n{BOLD}AS REGRAS:{RESET}")
    print("- Seus conhecimentos técnicos serão testados.")
    print("- HP em 0 significa Processo Terminado (Game Over).")
    print("- Use as SETAS (↑ ↓) para navegar e ENTER para confirmar.")
    
    input(f"\n{YELLOW}[ Pressione Enter para voltar ao Menu ]{RESET}")

def main_menu():
    while True:
        header = f"{MAGENTA}" + "="*50 + f"{RESET}\n" + HEADER.center(60) + f"\n{MAGENTA}" + "="*50 + f"{RESET}"
        options = ["INICIAR NOVA INSTÂNCIA (JOGAR)", "DOCUMENTAÇÃO (SOBRE O JOGO)", "ENCERRAR PROCESSO (SAIR)"]
        
        choice_idx = get_selection(options, header=header)
        
        if choice_idx == 0:
            start_game()
        elif choice_idx == 1:
            show_about()
        elif choice_idx == 2:
            clear_screen()
            slow_print(f"{RED}Desligando sistema... Até logo, dev.{RESET}")
            sys.exit()

def start_game():
    from constants import JOURNEYS_DATA
    clear_screen()
    print(f"{BOLD}{CYAN}─── INICIALIZANDO NOVO DEVELOPER ───{RESET}\n")
    name = input(f"{BOLD}Nome do Personagem:{RESET} ") or "Developer"
    
    # Seleção de Senioridade
    header_sen = f"{BOLD}Escolha sua Senioridade (Dificuldade):{RESET}"
    options_sen = [f"{GREEN}JUNIOR{RESET} (Fácil)", f"{YELLOW}PLENO{RESET} (Normal)", f"{RED}SENIOR{RESET} (Difícil)"]
    sen_idx = get_selection(options_sen, header=header_sen)
    seniority = ["JUNIOR", "PLENO", "SENIOR"][sen_idx]
    
    # Seleção de Jornada
    header_path = f"{BOLD}Escolha sua Jornada de Carreira:{RESET}"
    options_path = [
        f"{BOLD}BACKEND{RESET} - {JOURNEYS_DATA['BACKEND']['desc']}",
        f"{BOLD}FULLSTACK{RESET} - {JOURNEYS_DATA['FULLSTACK']['desc']}",
        f"{BOLD}DEVOPS{RESET} - {JOURNEYS_DATA['DEVOPS']['desc']}"
    ]
    path_idx = get_selection(options_path, header=header_path)
    journey = ["BACKEND", "FULLSTACK", "DEVOPS"][path_idx]
    
    player = Player(name, seniority, journey)
    engine = GameEngine(player)
    
    boot_sequence()
    
    while engine.running:
        engine.process_turn()

if __name__ == "__main__":
    main_menu()
