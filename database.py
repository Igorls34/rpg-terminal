# Banco de Dados de Questões de Syntaxia
# Estrutura: {JORNADA: {SENIORIDADE: [Questões]}}

QUESTIONS_DB = {
    "BACKEND": {
        "JUNIOR": [
            {"q": "Qual o resultado de 2 ** 3 em Python?", "opts": ["A) 6", "B) 8", "C) 9"], "ans": "B"},
            {"q": "Qual método adiciona um item ao final de uma lista?", "opts": ["A) add()", "B) push()", "C) append()"], "ans": "C"},
            {"q": "O que o comando 'pip' faz?", "opts": ["A) Instala pacotes", "B) Executa código", "C) Debuga"], "ans": "A"},
            # ... (Seriam 33 questões aqui)
        ],
        "PLENO": [
            {"q": "O que é um 'Decorator' em Python?", "opts": ["A) Um padrão de design para UI", "B) Uma função que modifica outra", "C) Um erro de sintaxe"], "ans": "B"},
            {"q": "Qual a diferença entre list e tuple?", "opts": ["A) Tuple é mutável", "B) List é imutável", "C) Tuple é imutável"], "ans": "C"},
            {"q": "O que faz o método __init__?", "opts": ["A) Finaliza a classe", "B) Construtor da classe", "C) Limpa a memória"], "ans": "B"},
        ],
        "SENIOR": [
            {"q": "Qual o problema de usar 'id' como nome de variável?", "opts": ["A) Shadowing de built-in", "B) Erro de compilação", "C) Lentidão"], "ans": "A"},
            {"q": "O que é o GIL (Global Interpreter Lock)?", "opts": ["A) Um cadeado de segurança", "B) Limitação de multithreading", "C) Um tipo de banco"], "ans": "B"},
            {"q": "Para que serve o 'cProfile'?", "opts": ["A) Testes unitários", "B) Profiling de performance", "C) Criptografia"], "ans": "B"},
        ]
    },
    "FULLSTACK": {
        "JUNIOR": [
            {"q": "O que significa CSS?", "opts": ["A) Color Style Sheet", "B) Cascading Style Sheets", "C) Creative Style"], "ans": "B"},
            {"q": "Qual tag HTML cria um link?", "opts": ["A) <link>", "B) <a>", "C) <href>"], "ans": "B"},
            {"q": "O que o console.log() faz no JS?", "opts": ["A) Alerta na tela", "B) Imprime no terminal do navegador", "C) Salva no banco"], "ans": "B"},
        ],
        "PLENO": [
            {"q": "Qual a diferença entre '==' e '===' em JavaScript?", "opts": ["A) Nenhuma", "B) '===' checa valor e tipo", "C) '==' é mais rápido"], "ans": "B"},
            {"q": "O que é o Virtual DOM no React?", "opts": ["A) Uma cópia do DOM real", "B) Um óculos de realidade virtual", "C) O banco de dados"], "ans": "A"},
            {"q": "Qual hook é usado para efeitos colaterais?", "opts": ["A) useState", "B) useEffect", "C) useContext"], "ans": "B"},
        ],
        "SENIOR": [
            {"q": "O que é 'Hydration' em aplicações SSR?", "opts": ["A) Beber água no dev", "B) Adicionar interatividade ao HTML estático", "C) Limpar o cache"], "ans": "B"},
            {"q": "O que é um 'Race Condition' no Frontend?", "opts": ["A) Corrida de carros", "B) Conflito entre requisições assíncronas", "C) Erro de CSS"], "ans": "B"},
        ]
    },
    "DEVOPS": {
        "JUNIOR": [
            {"q": "O que é o Docker?", "opts": ["A) Um navio", "B) Uma plataforma de containers", "C) Um editor de texto"], "ans": "B"},
            {"q": "Qual o comando para listar containers rodando?", "opts": ["A) docker ps", "B) docker list", "C) docker run"], "ans": "A"},
            {"q": "Para que serve o Git?", "opts": ["A) Salvar fotos", "B) Controle de versão", "C) Compilar código"], "ans": "B"},
        ],
        "PLENO": [
            {"q": "O que é Infraestrutura como Código (IaC)?", "opts": ["A) Codar no terminal", "B) Gerenciar infra via scripts/config", "C) Comprar servidores"], "ans": "B"},
            {"q": "Qual a função do Kubernetes?", "opts": ["A) Criar imagens", "B) Orquestrar containers", "C) Editar YAML"], "ans": "B"},
            {"q": "O que é uma Pipeline de CI/CD?", "opts": ["A) Um cano de água", "B) Fluxo automatizado de build/deploy", "C) Um erro de rede"], "ans": "B"},
        ],
        "SENIOR": [
            {"q": "O que é 'Blue-Green Deployment'?", "opts": ["A) Deploy em dias frios", "B) Estratégia de alternância entre duas prod", "C) Mudar cores da UI"], "ans": "B"},
            {"q": "Para que serve o Prometheus?", "opts": ["A) Codar mais rápido", "B) Monitoramento e alertas", "C) Deletar bancos"], "ans": "B"},
        ]
    }
}

# Expansão de Chefes por Jornada
BOSSES = {
    "BACKEND": ["The Query Overlord", "The Deadlock Duke", "The Legacy Monolith"],
    "FULLSTACK": ["The Responsive Ripper", "The Redux Kraken", "The Hydrated Hydra"],
    "DEVOPS": ["The Jenkins Juggernaut", "The Cluster Chaos", "The Downtime Dragon"]
}
