# Tic-Tac-Toe with Minimax AI

A desktop Tic-Tac-Toe game built with Python and Pygame. You play against an AI that searches the entire game tree with the [minimax algorithm](https://en.wikipedia.org/wiki/Minimax), so it never loses — the best you can achieve is a draw.

## Features

- Play as **X** or **O**
- Optimal, unbeatable AI opponent
- Minimal Pygame interface with a start screen and instant restart
- Clean separation between game logic (`tictactoe.py`) and UI (`runner.py`)
- No third-party AI libraries — minimax is implemented from scratch

## Requirements

- Python 3.8+ (tested on 3.12)
- [Pygame](https://www.pygame.org/)

## Quick start

```bash
# 1. Clone or download the project
git clone <repository-url>
cd tictactoe

# 2. Create and activate a virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the game
python runner.py
```

> **Note:** `runner.py` loads `OpenSans-Regular.ttf` by relative path, so launch it from the project root. Keep the font file next to `runner.py`.

## How to play

1. Choose **Play as X** or **Play as O**.
2. Click any empty cell to place your mark.
3. The AI replies automatically after a short pause.
4. When the round ends, click **Play Again** to return to the start screen.

X always moves first, so if you choose **O** the AI opens the game.

## Project structure

```
tictactoe/
├── runner.py              # Pygame UI, event loop, and game flow
├── tictactoe.py           # Board rules and minimax AI
├── requirements.txt       # Python dependencies (pygame)
├── OpenSans-Regular.ttf   # Font used by the UI
└── README.md
```

## How it works

The board is a 3×3 list of lists whose cells are `"X"`, `"O"`, or `None` for empty.

### Game logic (`tictactoe.py`)

| Function | Description |
| --- | --- |
| `initial_state()` | Returns an empty 3×3 board. |
| `player(board)` | Returns whose turn it is; `X` moves first. |
| `actions(board)` | Returns the set of legal `(row, col)` moves. |
| `result(board, action)` | Returns a new board with the move applied. Raises `ValueError` if the move is out of bounds or the cell is taken. |
| `winner(board)` | Returns `"X"`, `"O"`, or `None` if nobody has won. |
| `terminal(board)` | Returns `True` when the game is over (a win or a full board). |
| `utility(board)` | Scores a terminal board: `1` for an X win, `-1` for an O win, `0` for a draw. |
| `minimax(board)` | Returns the optimal move for the current player, or `None` if the game is over. |
| `max_value(board)` | Recursively computes the best utility X can force. |
| `min_value(board)` | Recursively computes the best utility O can force. |

### The AI

`minimax(board)` tries every legal move and assumes both sides play perfectly:

- **X** is the maximizing player and pushes the utility toward `1`.
- **O** is the minimizing player and pushes the utility toward `-1`.

The resulting move is therefore optimal: the AI wins whenever a win exists and draws otherwise. Tic-Tac-Toe's game tree is small (a few hundred thousand states), so exhaustive search finishes instantly and no pruning or heuristics are needed.

## Customizing

- **AI thinking delay** — change `time.sleep(0.5)` in `runner.py`. Remove it for instant moves.
- **Window and board layout** — adjust `size`, `tile_size`, or `tile_origin` in `runner.py`.
- **Colors** — edit the `black` and `white` tuples at the top of `runner.py`.
- **Fonts** — swap `OpenSans-Regular.ttf` for any TrueType font and update the `pygame.font.Font(...)` calls.

## Troubleshooting

| Problem | Fix |
| --- | --- |
| `pygame.error: font not initialized` or missing font | Run the game from the project root so `OpenSans-Regular.ttf` can be found. |
| `ModuleNotFoundError: No module named 'pygame'` | Activate your virtual environment, then run `pip install -r requirements.txt`. |
| The window does not open (WSL/SSH/headless server) | Pygame needs a display. Run the game on a desktop session or use a virtual display such as Xvfb. |
| Clicks seem to register twice | Clicking is polled per frame; a very long press can place two marks. A normal click is fine. |

## Acknowledgements

Built as an exercise in adversarial search with minimax. The UI is inspired by the CS50 AI Tic-Tac-Toe project.
