try:
    import curses
except ImportError:
    import windows_curses as curses

import random

# Initialize the game screen
def init_screen():
    screen = curses.initscr()
    curses.curs_set(0)
    screen.nodelay(1)
    screen.timeout(100)  # Screen refresh rate
    return screen

# Create a new window for the game
def create_game_window(screen):
    height, width = screen.getmaxyx()
    game_window = curses.newwin(height, width, 0, 0)
    return game_window, height, width

# Draw the initial state of the game
def draw_initial_state(window, snake, food, obstacles):
    window.clear()
    height, width = window.getmaxyx()
    for y, x in snake:
        if 0 <= y < height and 0 <= x < width:
            window.addch(y, x, '#')
    if 0 <= food[0] < height and 0 <= food[1] < width:
        window.addch(food[0], food[1], 'π')
    for ob in obstacles:
        for y, x in ob:
            if 0 <= y < height and 0 <= x < width:
                window.addch(y, x, ' ', curses.A_REVERSE)
    window.refresh()

# Generate a random position for food or obstacle
def generate_random_position(height, width, snake, obstacles):
    while True:
        pos = (random.randint(1, height-2), random.randint(1, width-2))
        if pos not in snake and all(pos not in ob for ob in obstacles):
            return pos

# Initialize the snake
def init_snake():
    return [(4, 4), (4, 3), (4, 2)]

# Initialize the food
def init_food(height, width, snake, obstacles):
    return generate_random_position(height, width, snake, obstacles)

# Initialize obstacles
def init_obstacles(height, width, snake):
    obstacles = []
    num_obstacles = int((height * width) * 0.05 // 25)  # 5% of the game screen
    for _ in range(num_obstacles):
        ob_length = random.randint(5, 10)
        if random.choice([True, False]):  # Horizontal or vertical obstacle
            if width-2-ob_length > 0:
                start_y = random.randint(1, height-2)
                start_x = random.randint(1, width-2-ob_length)
                obstacles.append([(start_y, start_x+i) for i in range(ob_length)])
        else:
            if height-2-ob_length > 0:
                start_y = random.randint(1, height-2-ob_length)
                start_x = random.randint(1, width-2)
                obstacles.append([(start_y+i, start_x) for i in range(ob_length)])
    return obstacles

# Move the snake based on direction
def move_snake(snake, direction):
    head_y, head_x = snake[0]
    if direction == curses.KEY_UP:
        new_head = (head_y-1, head_x)
    elif direction == curses.KEY_DOWN:
        new_head = (head_y+1, head_x)
    elif direction == curses.KEY_LEFT:
        new_head = (head_y, head_x-1)
    elif direction == curses.KEY_RIGHT:
        new_head = (head_y, head_x+1)
    return [new_head] + snake[:-1]

# Check for collisions with boundaries, self, or obstacles
def check_collisions(snake, height, width, obstacles):
    if not snake:
        return True
    head_y, head_x = snake[0]
    if head_y in [0, height-1] or head_x in [0, width-1]:
        return True
    if snake[0] in snake[1:]:
        return True
    if any(snake[0] in ob for ob in obstacles):
        return True
    return False

# Wrap snake position around the screen boundaries
def wrap_around(snake, height, width):
    if not snake:
        return snake
    head_y, head_x = snake[0]
    if head_y == 0:
        head_y = height - 2
    elif head_y == height - 1:
        head_y = 1
    if head_x == 0:
        head_x = width - 2
    elif head_x == width - 1:
        head_x = 1
    snake[0] = (head_y, head_x)
    return snake

def main(screen):
    game_window, height, width = create_game_window(screen)
    snake = init_snake()
    food = init_food(height, width, snake, [])
    obstacles = init_obstacles(height, width, snake)
    direction = curses.KEY_RIGHT
    food_count = {'normal': 0, 'special': 0}
    paused = False

    while True:
        draw_initial_state(game_window, snake, food, obstacles)

        key = screen.getch()
        if key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            direction = key
        elif key == ord(' '):
            paused = not paused
        elif key == ord('q'):
            break

        if paused:
            continue

        # Automatically move the snake
        new_snake = move_snake(snake, direction)

        new_head = new_snake[0] if new_snake else None

        if check_collisions(new_snake, height, width, obstacles):
            game_window.addstr(height//2, width//2 - len("Game Over")//2, "Game Over")
            game_window.refresh()
            curses.napms(2000)
            break

        if new_head == food:
            if game_window.inch(food[0], food[1]) == ord('π'):
                food_count['normal'] += 1
            else:
                food_count['special'] += 1
            food = init_food(height, width, new_snake, obstacles)
            # 增加蛇的长度
            new_snake.append(snake[-1])
        else:
            new_snake.pop()  # 如果没有吃到食物,就缩短蛇身

        snake = wrap_around(new_snake, height, width)

    game_window.clear()
    game_window.addstr(height//2, width//2 - len(f"Normal food eaten: {food_count['normal']}, Special food eaten: {food_count['special']}")//2,
                       f"Normal food eaten: {food_count['normal']}, Special food eaten: {food_count['special']}")
    game_window.refresh()
    curses.napms(2000)

curses.wrapper(main)
