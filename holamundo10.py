def longest_substring_k_distinct(s, k):
    if k == 0:
        return 0

    char_count = {}
    start = 0
    max_length = 0

    for end, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            char_count[s[start]] -= 1
            if char_count[s[start]] == 0:
                del char_count[s[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length

# Example usage:
s_example = "abcba"
k_example = 2
result = longest_substring_k_distinct(s_example, k_example)
print(result)
