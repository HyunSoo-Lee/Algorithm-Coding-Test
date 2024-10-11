# 스택/큐 > 다리를 지나는 트럭
# problem URL
# https://school.programmers.co.kr/learn/courses/30/lessons/42583

# 0 [0,0]
# 1 [0,7]
# 2 [7,0]
# 3 [0,4]
# 4 [4,5]
# 5 [5,0]
# 6 [0,6]
# 7 [6,0]
# 8 [0,0]

bridge_length = 2
weight = 10	
truck_weights = [7,4,5,6]

def bridge_control(queue, truck, weight, time):
    time += 1
    for i in range(len(queue)):
        if i == len(queue) - 1:
            if sum(queue) >= weight:
                queue[i] = 0
                print(time, queue)
                bridge_control(queue,truck, weight, time)    
            else: 
                queue[i] = truck
        else:
            queue[i] = queue[i+1]
    return queue, time

def answer(bridge_length, weight, truck_weights):
    queue = []    
    for j in range(bridge_length):
        queue.append(0)
    
    time = 0
    for i in truck_weights:
        q,time = bridge_control(queue, i, weight, time)


answer(bridge_length,weight,truck_weights)