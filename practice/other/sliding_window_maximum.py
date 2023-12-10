from collections import deque

def sliding_window_maximum(array, k):
    _deque = deque()
    ans = []

    for i in range(len(array)):
        # Remove elements that are out of the current window
        while _deque and _deque[0] < i - k + 1:
            _deque.popleft()

        # Remove elements smaller than the current element from the back
        while _deque and array[i] >= array[_deque[-1]]:
            _deque.pop()

        # Add the current element's index to the deque
        _deque.append(i)

        # Append the maximum element in the current window to the result
        if i >= k + 1: ans.append(array[_deque[0]])

    return ans

if __name__ == "__main__":
    print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
