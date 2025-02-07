import cv2
import numpy as np
import random

board_size = 18
cell_size = 20
start_index = 4
end_index = 14
window_size = board_size * cell_size

def create_board():
    board = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            if i == 0 or i == board_size-1 or j == 0 or j == board_size-1:
                row.append("wall")
            else:
                row.append("")
        board.append(row)
    return board

def place_food(board):
    while True:
        food_x = random.randint(1, board_size-2)
        food_y = random.randint(1, board_size-2)
        if board[food_x][food_y] == "":
            board[food_x][food_y] = "food"
            break

def draw_board(board, snake):
    img = np.zeros((window_size, window_size, 3), dtype=np.uint8)
    # 보드 그리기
    for i in range(board_size):
        for j in range(board_size):
            x, y = i * cell_size, j * cell_size
            if board[i][j] == "wall":
                cv2.rectangle(img, (x, y), (x + cell_size, y + cell_size), (255, 255, 255), -1)
            elif board[i][j] == "food":
                cv2.circle(img, (x + cell_size // 2, y + cell_size // 2), cell_size // 3, (0, 0, 255), -1)
    # 뱀 그리기
    for (sx, sy) in snake:
        cv2.rectangle(img,
                      (sx * cell_size, sy * cell_size),
                      ((sx + 1) * cell_size, (sy + 1) * cell_size),
                      (0, 255, 0), -1)
    snake_length = len(snake)
    cv2.putText(img, f"{snake_length:03}", (170, 30 - cell_size), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 0), 1)
    return img

directions = {
    "UP": (0, -1),
    "DOWN": (0, 1),
    "LEFT": (-1, 0),
    "RIGHT": (1, 0)
}

def move_snake(current_direction, snake, board):
    head_x, head_y = snake[0]
    move_x, move_y = directions[current_direction]
    new_head = (head_x + move_x, head_y + move_y)

    # 벽이나 자기 자신과 충돌 체크
    if board[new_head[0]][new_head[1]] == "wall" or new_head in snake:
        return False, snake, board

    snake.insert(0, new_head)  # 뱀의 머리 추가

    # 먹이를 찾았을 경우
    if board[new_head[0]][new_head[1]] == "food":
        place_food(board)  # 새 먹이 배치
    else:
        tail = snake.pop()  # 꼬리 제거
        board[tail[0]][tail[1]] = ""

    # 보드 업데이트
    board[new_head[0]][new_head[1]] = "SI"
    return True, snake, board

def main():
    board = create_board()
    random_x = random.randint(start_index, end_index - 1)
    random_y = random.randint(start_index, end_index - 1)
    snake = [(random_x, random_y)]
    init_dirs = ["UP", "DOWN", "LEFT", "RIGHT"]
    current_direction = random.choice(init_dirs)

    place_food(board)

    while True:
        img = draw_board(board, snake)
        cv2.imshow("Snake Game", img)

        key = cv2.waitKey(200) & 0xFF
        new_direction = current_direction

        if key == ord("w") and current_direction not in ("UP", "DOWN"):
            new_direction = "UP"
        elif key == ord("s") and current_direction not in ("DOWN", "UP"):
            new_direction = "DOWN"
        elif key == ord("a") and current_direction not in ("LEFT", "RIGHT"):
            new_direction = "LEFT"
        elif key == ord("d") and current_direction not in ("RIGHT", "LEFT"):
            new_direction = "RIGHT"

        current_direction = new_direction
        game_continue, snake, board = move_snake(current_direction, snake, board)

        if not game_continue :
            print("Game Over!")
            break

    cv2.destroyAllWindows()
    print("뱀의 길이:", len(snake))

if __name__ == "__main__":
    main()
