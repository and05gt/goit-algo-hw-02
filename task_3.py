def check_brackets_balance(string: str) -> str:
    """Check if the brackets in the string are balanced."""

    stack = []
    BRACKET_PAIRS = {')': '(', '}': '{', ']': '['}

    for char in string:
        if char in BRACKET_PAIRS.values():
            stack.append(char)
        elif char in BRACKET_PAIRS.keys():
            if not stack or stack[-1] != BRACKET_PAIRS[char]:
                return "Unbalanced"
            stack.pop()

    if not stack:
        return "Balanced"
    else:
        return "Unbalanced"
    
def main():
    test_strings = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]
    for s in test_strings:
        result = check_brackets_balance(s)
        print(f"{s}: {result}")

if __name__ == "__main__":
    main()