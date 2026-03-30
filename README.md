# ⚔️ RPG Syntaxia: The Developer Quest

**RPG Syntaxia** é um jogo de RPG procedural via terminal com temática de desenvolvimento de software. Nele, você assume o papel de um desenvolvedor (Junior, Pleno ou Senior) e deve navegar pelo reino corrompido de Syntaxia para derrotar bugs lendários, resolver desafios técnicos e salvar o sistema do temível Monolito Legado.

---

## 🚀 Funcionalidades Principais

- **Trilhas de Carreira (Jornadas):** Escolha entre as jornadas de **Backend**, **Fullstack** ou **DevOps**, cada uma com biomas, inimigos e chefes finais exclusivos.
- **Níveis de Senioridade (Dificuldade):** Jogue como **Junior** (Fácil), **Pleno** (Normal) ou **Senior** (Difícil), com atributos iniciais e desafios condizentes.
- **Sistema de Quests Técnicas:** Resolva desafios reais de lógica de programação, Python, segurança cibernética e ética para ganhar buffs de status e experiência.
- **Navegação Dinâmica no Terminal:** Interface interativa navegável por setas (↑ ↓) e Enter, sem necessidade de digitação numérica para escolhas.
- **Digitação Rítmica Adaptativa:** Experiência narrativa imersiva com velocidades de texto que mudam conforme o contexto da cena.
- **Combate de Console:** Ataque usando comandos como `git push --force`, defenda analisando logs e recupere HP com café.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Interface:** Terminal (CLI) com suporte a cores ANSI e captura de teclas via `msvcrt`.
- **Arquitetura:** Modularizada para fácil expansão de biomas, inimigos e questões.

---

## 📁 Estrutura do Projeto

- `main.py`: Ponto de entrada com sequência de boot e menu principal.
- `engine.py`: O "cérebro" do jogo, gerenciando turnos, eventos e combate.
- `entities.py`: Definições das classes de Player e Inimigo.
- `database.py`: Banco de dados massivo com centenas de questões técnicas e chefes.
- `ui_utils.py`: Funções utilitárias para navegação por teclado e interface.
- `constants.py`: Configurações de cores, biomas e textos do sistema.

---

## 🎮 Como Jogar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Igorls34/rpg-terminal.git
   cd rpg-terminal
   ```

2. **Execute o jogo:**
   ```bash
   python main.py
   ```

3. **Controles:**
   - Use as **SETAS (↑ ↓)** para navegar entre as opções.
   - Pressione **ENTER** para confirmar sua escolha.
   - Utilize a **Ação Livre** para tentar comandos customizados.

---

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se à vontade para clonar, modificar e expandir o Reino de Syntaxia!

---

**Desenvolvido com ☕ e 🐍 por Igorls34 (e Gemini CLI)**
