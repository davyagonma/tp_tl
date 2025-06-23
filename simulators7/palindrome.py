def is_palindrome(w: str) -> bool:
    tape = list(w)
    left = 0
    right = len(tape) - 1
    while left < right:
        if tape[left] != tape[right]:
            return False
        left += 1
        right -= 1
    return True
