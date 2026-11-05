def squared(text, length):
    total_chars = length * length
    repeated_text = text * (total_chars // len(text) + 1)
    for i in range(length):
        start_index = i * length
        end_index = start_index + length
        print(repeated_text[start_index:end_index])
if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)