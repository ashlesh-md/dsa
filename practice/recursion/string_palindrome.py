# TC : O(N)
# SC : O(N) Internal Stack
# def reverse(string):
#     if len(string) == 0:
#         return string
#     return reverse(string[1:]) + string[0]

# TC : O(N / 2)
# SC : O(N / 2) Internal Stack

def reverse(string , index = 0):
    if index >= len(string) // 2:
        return True
    if string[index] != string[len(string) - 1 - index]:
        return False
    return reverse(string , index + 1)

if __name__ == '__main__':
    string = input()
    if reverse(string):
        print('Palindrome')
    else:
        print('Not Palindrome')
    print(string)
