def solution(A):
    N = len(A)
    peaks = [0] * (N + 2)
    for i in range(1, N + 1):
        peaks[i] = peaks[i - 1] + (0 < i - 1 < N - 1 and A[i - 2] < A[i - 1] > A[i])

    for distance in range(N, 0, -1):
        flags = 0
        pos = 1
        while pos <= N and flags < distance:
            if peaks[min(pos + distance - 1, N)] > peaks[pos - 1]:
                flags += 1
                pos += distance
            else:
                pos += 1
        if flags == distance:
            return flags
    return 0