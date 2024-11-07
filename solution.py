
def solution(A):
    # Find all the peaks
    peaks = []
    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)
    
    if len(peaks) == 0:
        return 0
    
    # Binary search for the maximum number of flags
    def can_place_flags(peaks, k):
        count = 1
        last_flag = peaks[0]
        for i in range(1, len(peaks)):
            if peaks[i] - last_flag >= k:
                count += 1
                last_flag = peaks[i]
                if count == k:
                    return True
        return False
    
    left, right = 1, len(peaks)
    max_flags = 0
    while left <= right:
        mid = (left + right) // 2
        if can_place_flags(peaks, mid):
            max_flags = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return max_flags


def solution_old3(A):
    # Find all the peaks
    peaks = []
    for i in range(1, len(A) - 1):
        if A[i] > A[i - 1] and A[i] > A[i + 1]:
            peaks.append(i)
    
    if len(peaks) == 0:
        return 0
    
    # Try to place the maximum number of flags
    max_flags = 0
    for k in range(1, len(peaks) + 1):
        flags = 1
        last_flag = peaks[0]
        for i in range(1, len(peaks)):
            if peaks[i] - last_flag >= k:
                flags += 1
                last_flag = peaks[i]
                if flags == k:
                    break
        flags = min(flags, k)
        max_flags = max(max_flags, flags)
    
    return max_flags

# max flagsの計算
def solution_old1(A):
    N = len(A)
    peaks = []
    distance_between = []
    for i in range(1, N-1):
        if A[i] > A[i - 1] and A[i] > A[i+1]:
            peaks.append(i)
    for i in range(1, len(peaks)):
        distance_between.append(peaks[i] - peaks[i-1])
    peak_max = len(peaks)
    count_peak = 0
    flags = 0
    for distance in range(1, peak_max):
        if len(peaks) < distance:
            break
        # peakの数がdistanceより少ない場合は、distanceの数を返す
        while flags == 0:
            for i in range(1, len(peaks)):
                if peaks[i] - peaks[i-1] < distance:
                    peaks, distance_between = calculate_redistance(peaks, distance_between, distance)
                    break
            if i == len(peaks) - 1:
                count_peak += 1
                break
            if i == 1:
                flags = 1
                break
    return len(peaks)

# 距離の調整を行う
def calculate_redistance(peaks, distance_between, distance_restrict):
    peaks_rearranged = [peaks[0]]
    distance_between_rearranged = []
    # dist_min = min(distance_between)
    is_rearranged = False
    for i in range(1, len(peaks)):
        if peaks[i] - peaks[i-1] < distance_restrict and not is_rearranged:
            is_rearranged = True
            pass
        elif is_rearranged:
            peaks_rearranged.append(peaks[i])
            distance_between_rearranged.append(peaks[i] - peaks[i-1])
    return peaks_rearranged, distance_between_rearranged

def solution_old2(A):
    N = len(A)
    peaks = [0] * (N + 1)
    for i in range(1, N):
        peaks[i] = peaks[i - 1] + (0 if i == 1 or i == N - 1 or A[i - 1] <= A[i - 2] or A[i - 1] <= A[i] else 1)
    peak_max = max(peaks)
    print(peaks)
    for distance in range(peak_max):
        flags = 1
        pos = 1
        while flags < distance:
            if pos + distance > N + 1 or peaks[pos + distance] <= flags:
                break
            pos += distance
            flags += 1
        else:
            return distance
    return peaks[N]

if __name__ == '__main__':
    A=[0 for _ in range(12)]
    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
    # A = [0,1,1]
    print(solution(A))