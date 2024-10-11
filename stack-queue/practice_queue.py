class CustomQueue:
    def __init__(self, size):
        # 지정된 크기의 큐를 초기화하고, 초기 값은 0으로 설정
        self.queue = [0] * size
        self.size = size

    def enqueue(self, value):
        # 큐의 원소를 한 칸씩 앞으로 이동시키고, 마지막 위치에 새로운 값을 추가
        for i in range(self.size - 1):
            self.queue[i] = self.queue[i + 1]
        self.queue[-1] = value  # 새로운 값이 리스트의 끝에 추가
        self.display_queue()

    def display_queue(self):
        # 큐의 현재 상태를 출력
        print(f"Current Queue: {self.queue}")

# 큐 사용 예제
queue_size = 5
q = CustomQueue(queue_size)

# 값을 큐에 삽입
q.enqueue(7)  # [0, 0, 0, 0, 7]
q.enqueue(3)  # [0, 0, 0, 7, 3]
q.enqueue(5)  # [0, 0, 7, 3, 5]
q.enqueue(6)  # [0, 7, 3, 5, 6]
q.enqueue(8)  # [7, 3, 5, 6, 8]
q.enqueue(1)  # [3, 5, 6, 8, 1]
q.enqueue(2)  # [5, 6, 8, 1, 2]
