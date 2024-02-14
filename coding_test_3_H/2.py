def count_bus_stops(residents, K):
    # 먼저 거주 지역을 오름차순으로 정렬합니다.
    # residents.sort()

    # 중복을 제거한 후 거주 지역을 오름차순으로 정렬합니다.
    unique_residents = sorted(set(residents))

    # 초기 정류장 수는 최소 하나 필요합니다.
    count = 1
    # 첫 번째 거주 지역을 현재 정류장으로 설정합니다.
    current_stop = residents[0]

    # 거주 지역을 순회하면서 정류장 수 계산
    for location in unique_residents:
        # 현재 정류장과 비교하여 K 이상 차이가 난다면 새로운 정류장 설정
        if location - current_stop >= K:
            count += 1
            current_stop = location

    return count
