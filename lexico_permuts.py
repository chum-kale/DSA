def generate_unique_permutations_lexicographical(s):
    def backtrack(start):
        if start == len(s):
            permutations.append(''.join(s))
            return
        
        used = set()  # To keep track of used characters in the current position
        for i in range(start, len(s)):
            if s[i] in used:
                continue
            s[start], s[i] = s[i], s[start]  # Swap characters
            backtrack(start + 1)             # Recurse
            s[start], s[i] = s[i], s[start]  # Restore original order
            used.add(s[i])                  # Mark character as used
        
    s = list(s)
    permutations = []
    backtrack(0)
    permutations.sort()  # Sort the permutations lexicographically
    return permutations

input_string = "aab"
permutations = generate_unique_permutations_lexicographical(input_string)
for perm in permutations:
    print(perm)