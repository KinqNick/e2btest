```python
import random

# Game State
game_state = {
    "snake": [(5, 5)],
    "food": (10, 10),
    "score": 0
}

# Game Settings
BOARD_SIZE = 20
DIRECTIONS = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}
current_direction = "RIGHT"

def update_game(keydown):
    global game_state, current_direction

    # Update direction
    if keydown in DIRECTIONS:
        current_direction = keydown

    # Update snake position
    old_head = game_state["snake"][0]
    movement = DIRECTIONS[current_direction]
    new_head = (old_head[0] + movement[0], old_head[1] + movement[1])

    # Check for game over conditions
    if (new_head in game_state["snake"]) or (new_head[0] < 0 or new_head[0] >= BOARD_SIZE or new_head[1] < 0 or new_head[1] >= BOARD_SIZE):
        return False

    # Check for food
    if new_head == game_state["food"]:
        game_state["score"] += 1
        game_state["food"] = spawn_food()
    else:
        game_state["snake"].pop()

    # Add new head to snake
    game_state["snake"].insert(0, new_head)

    return True

def spawn_food():
    while True:
        position = (random.randint(0, BOARD_SIZE - 1), random.randint(0, BOARD_SIZE - 1))
        if position not in game_state["snake"]:
            return position
```