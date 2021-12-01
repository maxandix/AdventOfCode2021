def nums_in_file():
    with open('input.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield int(line.strip())


def task1():
    prev = float('inf')
    counter = 0
    for current in nums_in_file():
        counter = counter + int(current > prev)
        prev = current
    return counter


def task2():
    prev = float('inf')
    counter = 0
    second = third = None
    for num in nums_in_file():
        first, second, third = second, third, num
        if None in (first, second):
            continue
        current = first + second + third
        counter = counter + int(current > prev)
        prev = current
    return counter


print('task1', task1())
print('task2', task2())
