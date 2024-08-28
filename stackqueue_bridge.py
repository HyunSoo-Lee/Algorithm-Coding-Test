# 스택/큐 > 다리를 지나는 트럭
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

class CustomQueue:
    def __init__(self, size):
        # 지정된 크기의 큐를 초기화하고, 초기 값은 0으로 설정
        self.queue = [0] * size
        self.size = size

    # def enqueue(self, value):
    #     # 큐의 원소를 한 칸씩 앞으로 이동시키고, 마지막 위치에 새로운 값을 추가
    #     for i in range(self.size - 1):
    #         self.queue[i] = self.queue[i + 1]
    #     self.queue[-1] = value  # 새로운 값이 리스트의 끝에 추가
    #     self.display_queue()

    def enqueue(self, value, max):
        # 큐의 원소를 한 칸씩 앞으로 이동시키고, 마지막 위치에 새로운 값을 추가
        for i in range(self.size - 1):
            self.queue[i] = self.queue[i + 1]
            self.queue[-1] = 0

        print(f"Current Weight: {sum(self.queue) + value}")
        if sum(self.queue) + value > max:
          self.display_queue()
          return False
        else: 
            self.queue[-1] = value
            self.display_queue()
            return True  

    def display_queue(self):
        # 큐의 현재 상태를 출력
        print(f"Current Queue: {self.queue}")

bridge_length = 100
weight = 100
truck_weights = [10]

# bridge_length = 2
# weight = 10
# truck_weights = [7,4,5,6]

size = bridge_length
q = CustomQueue(size)
i = 0
time = 0
while True:
    max_weight = q.enqueue(truck_weights[i], weight)
    if max_weight:
        i += 1
        time += 1
    else:
        time += 2
    if i == len(truck_weights):
        break

print(time)

