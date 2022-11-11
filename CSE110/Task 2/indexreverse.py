string = input('Your string is: ')
index = input('Your index is: ')


def reverse(string, index):
    if index == 0:
        return string
    else:
        return string[index - 1] + reverse(string, index - 1)

print(reverse(string, int(index)))