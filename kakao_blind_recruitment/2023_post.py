def solution(cap, n, deliveries, pickups):
    # 배달할 물건이 남아있거나 수거할 물건이 남아있는 동안 반복합니다.
    total_distance = 0
    delivery_remain = 0  # 배달할 물건의 남은 양을 기록
    pickup_remain = 0  # 수거할 물건의 남은 양을 기록
    
    # 모든 집을 역순으로 확인합니다.
    for i in range(n - 1, -1, -1):
        delivery_remain += deliveries[i]  # 해당 집에서 배달해야 할 물건 추가
        pickup_remain += pickups[i]  # 해당 집에서 수거해야 할 물건 추가
        
        # 만약 배달할 물건이나 수거할 물건이 있다면, 트럭을 이동시킵니다.
        while delivery_remain > 0 or pickup_remain > 0:
            # 트럭을 해당 집까지 보내고 돌아옵니다.
            total_distance += (i + 1) * 2  # 물류창고로 돌아오기 때문에 왕복 거리
            
            # 트럭에 실을 수 있는 만큼 배달과 수거를 진행합니다.
            delivery_remain = max(0, delivery_remain - cap)
            pickup_remain = max(0, pickup_remain - cap)
    
    return total_distance
