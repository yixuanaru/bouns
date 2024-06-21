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
    screen.timeout(100)
    return screen

# Create a new window for the game
def create_game_window(screen):
    height, width = screen.getmaxyx()
    game_window = curses.newwin(height, width, 0, 0)
    return game_window, height, width

# Draw the initial state of the game
def draw_initial_state(window, snake, food, obstacles):
    window.clear()
    for y, x in snake:
        window.addch(y, x, '▋')
    window.addch(food[0], food[1], 'π')
    for ob in obstacles:
        for y, x in ob:
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
    total_area = height * width
    obstacle_area = int(total_area * 0.05)
    covered_area = 0

    while covered_area < obstacle_area:
        ob_length = random.randint(5, 10)
        if random.choice([True, False]):  # Horizontal or vertical obstacle
            if width-2-ob_length > 0:
                start_y = random.randint(1, height-2)
                start_x = random.randint(1, width-2-ob_length)
                ob = [(start_y, start_x+i) for i in range(ob_length)]
        else:
            if height-2-ob_length > 0:
                start_y = random.randint(1, height-2-ob_length)
                start_x = random.randint(1, width-2)
                ob = [(start_y+i, start_x) for i in range(ob_length)]
        
        if all(pos not in snake for pos in ob):
            obstacles.append(ob)
            covered_area += ob_length
    
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
    snake = [new_head] + snake[:-1]
    return snake

# Check for collisions with boundaries, self, or obstacles
def check_collisions(snake, height, width, obstacles):
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

        new_head_y, new_head_x = snake[0]
        if direction == curses.KEY_UP:
            new_head_y -= 1
        elif direction == curses.KEY_DOWN:
            new_head_y += 1
        elif direction == curses.KEY_LEFT:
            new_head_x -= 1
        elif direction == curses.KEY_RIGHT:
            new_head_x += 1

        new_head_y %= height
        new_head_x %= width

        new_head = (new_head_y, new_head_x)

        if new_head in snake or any(new_head in ob for ob in obstacles):
            game_window.addstr(height//2, width//2 - len("Game Over")//2, "Game Over")
            game_window.refresh()
            curses.napms(2000)
            break

        snake.insert(0, new_head)
        if new_head == food:
            if game_window.inch(food[0], food[1]) == ord('π'):
                food_count['normal'] += 1
            else:
                food_count['special'] += 1
            food = init_food(height, width, snake, obstacles)
        else:
            snake.pop()

        snake = wrap_around(snake, height, width)

    game_window.clear()
    game_window.addstr(height//2, width//2 - len(f"Normal food eaten: {food_count['normal']}, Special food eaten: {food_count['special']}")//2,
                       f"Normal food eaten: {food_count['normal']}, Special food eaten: {food_count['special']}")
    game_window.refresh()
    curses.napms(2000)

curses.wrapper(main)
