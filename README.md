# 👻 Game Ryan - Python

![Python](https://img.shields.io/badge/Python-000000?style=for-the-badge&logo=python&logoColor=00BFFF)
![Pygame](https://img.shields.io/badge/Pygame-000000?style=for-the-badge&logo=python&logoColor=00BFFF)

Jogo de tiro 2D (arcade) feito em Pygame, onde você controla um fantasma que
precisa sobreviver a ondas de morcegos que aparecem aleatoriamente na tela.
Atire feitiços para eliminá-los e pontuar — se um morcego encostar no
fantasma, é game over.

---

## Como jogar

| Tecla | Ação |
|---|---|
| `W` `A` `S` `D` | Mover o fantasma |
| `SPACE` | Atirar |

- Morcegos aparecem em intervalos aleatórios e se movem pela tela
- Cada morcego eliminado por um tiro soma um ponto no placar
- Se um morcego colidir com o fantasma, o jogo termina e aparece a tela de **GAME OVER**

---

## Funcionalidades

- Sistema de pontuação em tempo real
- Trilha sonora em loop e efeito sonoro de ataque
- Spawn aleatório de inimigos, com chance controlada a cada ciclo
- Colisão por máscara de pixels (`collide_mask`), mais precisa que colisão por retângulo
- Fonte pixelada customizada para placar e tela de game over
- Ícone e janela personalizados (840x480)

---

## Tecnologias

- **Python**
- **Pygame** — engine 2D usada para janela, sprites, colisão, áudio e fontes

---

## Estrutura do projeto

```
python-game/
├── data/            # imagens, ícone, música e efeitos sonoros
├── font/            # fonte pixelada (Pixeltype.ttf)
├── bat.py           # classe do inimigo (morcego)
├── ghost.py         # classe do personagem principal (fantasma)
├── shoot.py         # classe do projétil (feitiço)
├── main.py          # loop principal do jogo
└── pilares.md       # princípios de design do projeto
```

---

## Como executar

```bash
git clone https://github.com/Ryan-Oliv/python-game.git
cd python-game
pip install pygame
python main.py
```

---

## Créditos

Imagens, ícone, música e efeitos sonoros estão na pasta `data/`. Fonte pixelada
(`Pixeltype.ttf`) na pasta `font/`.

