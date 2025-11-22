from collections import deque

def is_palindrome(string) -> bool:
    """Check if the given string is a palindrome using a deque."""
    
    normalized_string = ''.join(char.lower() for char in string if char.isalnum())
    d = deque(normalized_string)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

def main():
    test_strings = ["Racecar", "Hello", "A man, a plan, a canal: Panama", "Python"]
    for s in test_strings:
        if is_palindrome(s):
            print(f'"{s}" is a palindrome.')
        else:
            print(f'"{s}" is not a palindrome.')
        
if __name__ == "__main__":
    main()