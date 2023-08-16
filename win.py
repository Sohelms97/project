def solve_game(a, b, c):
    # The girl who can press c buttons will win if c is odd, otherwise, both can play optimally.
    if c % 2 == 0:
        return "First" if a > b else "Second"
    else:
        return "First" if a >= b else "Second"

# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    a, b, c = map(int, input().split())
    result = solve_game(a, b, c)
    print(result)
