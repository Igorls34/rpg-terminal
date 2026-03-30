import sys
import os
import time

try:
    import msvcrt
    WINDOWS = True
except ImportError:
    WINDOWS = False

from constants import BOLD, GREEN, RESET, ACTION_LABEL

def get_selection(options, header=None):
    """
    Exibe um menu navegável por setas.
    Funciona no CMD, PowerShell e Terminais Windows.
    """
    selected_index = 0
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if header:
            print(header)
            
        print(f"\n{BOLD}{ACTION_LABEL}{RESET}")
        print(f"(Use as setas {BOLD}↑ ↓{RESET} e confirme com {BOLD}ENTER{RESET})")
        print("—" * 30)
        
        for i, opt in enumerate(options):
            if i == selected_index:
                print(f"{BOLD}{GREEN}  > {opt}{RESET}")
            else:
                print(f"    {opt}")
        print("—" * 30)
        
        if WINDOWS:
            # Captura de tecla no Windows
            key = msvcrt.getch()
            
            # Teclas de seta no Windows costumam enviar um prefixo 0 ou 224 (0xe0)
            if key in [b'\x00', b'\xe0']:
                key = msvcrt.getch()
                if key == b'H': # Seta para Cima
                    selected_index = (selected_index - 1) % len(options)
                elif key == b'P': # Seta para Baixo
                    selected_index = (selected_index + 1) % len(options)
            elif key == b'\r': # ENTER
                break
            elif key == b'\x03': # CTRL+C
                sys.exit()
        else:
            # Fallback para outros sistemas
            print(f"\nDigite o número (1-{len(options)}): ", end="")
            try:
                choice = input()
                if choice.isdigit() and 1 <= int(choice) <= len(options):
                    return int(choice) - 1
            except EOFError:
                sys.exit()
                
    return selected_index
