# Reverse a string using recursion

def string_reverse(string):
    if len(string) == 1: return string
    return string_reverse(string[1:]) + string[0]

if __name__ == "__main__":
    print(string_reverse("aaaabbbb"))
    print(string_reverse("malayalam"))
    print(string_reverse("albert einstein"))
