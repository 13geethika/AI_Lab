from collections import deque
def is_valid_state(state, total_missionaries, total_cannibals):
    left_missionaries, left_cannibals, boat, right_missionaries, right_cannibals = state
    if (
        left_missionaries < 0
        or left_cannibals < 0
        or right_missionaries < 0
        or right_cannibals < 0
    ):
        return False
    if (
        left_missionaries > total_missionaries
        or left_cannibals > total_cannibals
        or right_missionaries > total_missionaries
        or right_cannibals > total_cannibals
    ):
        return False
    if (
        (left_missionaries < left_cannibals and left_missionaries > 0)
        or (total_missionaries - left_missionaries < total_cannibals - left_cannibals and total_missionaries - left_missionaries > 0)
        or (right_missionaries < right_cannibals and right_missionaries > 0)
        or (total_missionaries - right_missionaries < total_cannibals - right_cannibals and total_missionaries - right_missionaries > 0)
    ):
        return False
    return True
def generate_next_states(current_state, total_missionaries, total_cannibals):
    next_states = []
    left_missionaries, left_cannibals, boat, right_missionaries, right_cannibals = current_state
    valid_actions = [(0, 1), (1, 0), (1, 1), (2, 0), (0, 2)]
    for m, c in valid_actions:
        if (0<= left_missionaries - m<= left_cannibals - c or 0 <= right_missionaries + m
            <= right_cannibals + c):
            new_left_missionaries = left_missionaries - m
            new_left_cannibals = left_cannibals - c
            new_right_missionaries = right_missionaries + m
            new_right_cannibals = right_cannibals + c
            new_boat = 1 - boat
            new_state = (
                new_left_missionaries,
                new_left_cannibals,
                new_boat,
                new_right_missionaries,
                new_right_cannibals,
            )
            if is_valid_state(new_state, total_missionaries, total_cannibals):
                next_states.append(new_state)
    return next_states
def bfs(initial_state, goal_state, total_missionaries, total_cannibals):
    visited = set()
    queue = deque([(initial_state, [])])
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path
        visited.add(current_state)
        for next_state in generate_next_states( current_state, total_missionaries, total_cannibals  ):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))
    return None
def main():
    total_missionaries = int(input("Enter the total number of missionaries: "))
    total_cannibals = int(input("Enter the total number of cannibals: "))
    if total_missionaries!=total_cannibals:
        print("Not possible")
        return None
    initial_left_missionaries = total_missionaries
    initial_left_cannibals = total_cannibals
    initial_right_missionaries = total_missionaries - initial_left_missionaries
    initial_right_cannibals = total_cannibals - initial_left_cannibals
    initial_boat = 1
    initial_state = (
        initial_left_missionaries,
        initial_left_cannibals,
        initial_boat,
        initial_right_missionaries,
        initial_right_cannibals,
    )
    goal_state = (0,0,0,total_missionaries,total_cannibals,)
    if not is_valid_state(initial_state, total_missionaries, total_cannibals):
        print("Invalid input configuration. No solution possible.")
    else:
        result = bfs(initial_state, goal_state, total_missionaries, total_cannibals)
        if result:
            print("Solution path:")
            for state in result:
                left_missionaries, left_cannibals, boat, right_missionaries, right_cannibals = state
                print("Left Side:")
                print(f"Missionaries: {left_missionaries}, Cannibals: {left_cannibals}")
                print("Right Side:")
                print(f"Missionaries: {right_missionaries}, Cannibals: {right_cannibals}")
                print("Boat: ", "Left" if boat == 0 else "Right")
                print("----------------")
        else:
            print("No solution possible.")
if __name__ == "__main__":
    main()