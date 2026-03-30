# Configurações e dados fixos do jogo

# Cores ANSI
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
WHITE = "\033[37m"

JOURNEYS_DATA = {
    "BACKEND": {
        "biomes": ["Cripta dos Datasets", "Vale dos Algoritmos", "Núcleo de Processamento"],
        "enemies": [
            {"name": "Query N+1", "hp": 40, "attack": 12, "gold": 20, "exp": 30},
            {"name": "Race Condition", "hp": 50, "attack": 15, "gold": 25, "exp": 40}
        ],
        "final_boss": "The Legacy Monolith",
        "desc": "Foco em eficiência, segurança e arquitetura de dados."
    },
    "FULLSTACK": {
        "biomes": ["Planície do DOM", "Pântano do State Management", "Ponte da API"],
        "enemies": [
            {"name": "Z-Index Ghost", "hp": 35, "attack": 10, "gold": 15, "exp": 25},
            {"name": "CORS Nightmare", "hp": 45, "attack": 18, "gold": 30, "exp": 45}
        ],
        "final_boss": "The Hydrated Hydra",
        "desc": "Equilíbrio entre UI impecável e integração robusta."
    },
    "DEVOPS": {
        "biomes": ["Nuvem de Docker", "Pipeline da Agonia", "Cluster de Kubernetes"],
        "enemies": [
            {"name": "Jenkins Fire", "hp": 55, "attack": 20, "gold": 40, "exp": 50},
            {"name": "Terraform Drift", "hp": 40, "attack": 15, "gold": 20, "exp": 35}
        ],
        "final_boss": "The Downtime Dragon",
        "desc": "O mestre da automação, escalabilidade e infraestrutura."
    }
}

ENEMIES_POOL = [
    {"name": "NullPointerException", "hp": 30, "attack": 10, "gold": 10, "exp": 20},
    {"name": "Zombie Process", "hp": 40, "attack": 8, "gold": 15, "exp": 25}
]

# Mensagens de interface
HEADER = f"{BOLD}{MAGENTA}=== RPG SYNTAXIA: MULTI-PATH QUEST ==={RESET}"
STATUS_LABEL = f"{BOLD}{CYAN}📊 STATUS DO DEVELOPER{RESET}"
HISTORY_LABEL = f"{BOLD}{YELLOW}📖 LOG DE NARRATIVA{RESET}"
ACTION_LABEL = f"{BOLD}{GREEN}⚔️ CONSOLE DE COMANDOS{RESET}"
