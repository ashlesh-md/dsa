def search(matrix, key):
        rows, columns = len(matrix), len(matrix[0])
        left, right = 0, rows * columns - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // columns][mid % columns]

            if   key < val: right = mid - 1
            elif key > val: left = mid + 1
            else: return True
        
        return False


def searchMatrix( matrix, target):

    for row in matrix:

        left,right=0,len(row)-1

        while left<=right:

            mid=(left+right)//2

            if row[mid]==target:
                return True

            if row[mid]>target:
                right = mid-1

            else:
                left = mid+1

    return False

if __name__ == "__main__":
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    key = 5
    result = searchMatrix(matrix, key)
    if result != -1:
        print(f"Key {key} found at position {result}")
    else:
        print(f"Key {key} not found in the matrix")
