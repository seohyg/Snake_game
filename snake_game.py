import cv2  # OpenCV 라이브러리
import numpy as np  # numpy 라이브러리
import random  # random 라이브러리

board_size = 18
cell_size = 20
start_index = 4
end_index = 14
window_size = board_size * cell_size

# 보드 생성 함수
def create_board():
    # 18x18 크기의 빈 보드 생성
    board = []
    for i in range(18):
        row = []
        for j in range(18):
            # 테두리인 경우 "wall", 아니면 빈칸
            if i == 0 or i == 17 or j == 0 or j == 17:
                row.append("wall")
            else:
                row.append("")
        board.append(row)
    return board

# 먹이 생성 함수
def place_food(board):
    while True:
        food_x = random.randint(1, 16)
        food_y = random.randint(1, 16)
        if board[food_x][food_y] == "":  # 벽에 없는 곳인지 확인
            board[food_x][food_y] = "food"
            break

# 보드 꾸미기 함수
def draw_board(board, snake):
    img = np.zeros((window_size, window_size, 3), dtype=np.uint8)
    for i in range(board_size):
        for j in range(board_size):
            x, y = i * cell_size, j * cell_size  # 각 격자 하나의 좌표에 해당
            if board[i][j] == "wall":
                cv2.rectangle(img, (x, y), (x + cell_size, y + cell_size), (255, 255, 255), -1)
            elif board[i][j] == "food":  # 음식일 경우 원으로 표시
                cv2.circle(img, (x + cell_size // 2, y + cell_size // 2), cell_size // 3, (0, 0, 255), -1)

    for (x, y) in snake:  # 뱀의 몸을 그리기
        cv2.rectangle(img, (x * cell_size, y * cell_size), (x + cell_size, y + cell_size), (0, 255, 0), -1)

    return img

# 방향 별 이동 방향 벡터 고정
directions = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}

opposite_direction = {
    "UP": "DOWN",
    "DOWN": "UP",
    "LEFT": "RIGHT",
    "RIGHT": "LEFT"
}

# 뱀 이동 함수 - 이동시 머리와 꼬리를 처리해 삭제하는 방식으로 움직임
def move_snake(current_direction, snake, board):
    head_x, head_y = snake[0]
    move_x, move_y = directions[current_direction]
    new_head = (head_x + move_x, head_y + move_y)  # 생성될 머리의 위치 계산
    new_head[0] == "SI"  # 생성될 머리의 좌표

    # 벽이나 자기 자신과 충돌 체크
    if board[new_head[0]][new_head[1]] == "wall" or new_head in snake:
        return False, snake, board  # 게임 오버 신호

    snake.insert(0, new_head)  # 뱀의 몸에 새로운 머리를 추가

    # 먹이를 찾았을 경우 뱀의 몸이 길어지고 그렇지 않으면 꼬리를 제거
    if board[new_head[0]][new_head[1]] == "food":
        place_food(board)  # 새로운 먹이 배치
    else:
        tail = snake.pop()
        board[tail[0]][tail[1]] = ""

    # 보드 업데이트
    board[new_head[0]][new_head[1]] = "SI"

    return True, snake, board

def main():
    board = create_board()
    random_x = random.randint(start_index, end_index - 1)
    random_y = random.randint(start_index, end_index - 1)
    snake = [(random_x, random_y)]  # 뱀의 초기 위치

    directions = ["UP", "DOWN", "LEFT", "RIGHT"] # 랜덤으로 초기 방향 설정
    current_direction = random.choice(directions)

    place_food(board)

    while True:
        img = draw_board(board, snake)
        cv2.imshow("Snake Game", img)

        key = cv2.waitKey(200) & 0xFF  ######### 200밀리초마다 입력대기 /// 비트연산자 이유분 문법 좀 미묘
        new_direction = current_direction
        if key == ord("w") and current_direction != "DOWN" and current_direction != "UP": # 진행방향과 나란하지 않는 경우에만 새 진행방향 업데이트
            new_direction = "UP"
        elif key == ord("s") and current_direction != "UP" and current_direction != "DOWN":
            new_direction = "DOWN"
        elif key == ord("a") and current_direction != "RIGHT" and current_direction != "LEFT":
            new_direction = "LEFT"
        elif key == ord("d") and current_direction != "LEFT" and current_direction != "RIGHT":
            new_direction = "RIGHT"

        current_direction = new_direction
        game_continue, snake, board = move_snake(current_direction, snake, board)
        if game_continue == False:
            print("Game Over!")
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
