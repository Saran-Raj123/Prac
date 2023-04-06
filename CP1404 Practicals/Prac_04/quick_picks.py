import random

NUM_QUICK_PICKS = 5
MIN_NUM = 1
MAX_NUM = 45
NUM_PER_PICK = 6

for i in range(NUM_QUICK_PICKS):
    numbers = []
    while len(numbers) < NUM_PER_PICK:
        num = random.randint(MIN_NUM, MAX_NUM)
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    print(' '.join('{:2d}'.format(num) for num in numbers))
