def count_word_occurance(file_path, word):
    ctr = 0
    with open(file_path, 'r') as file:
        for line in file:
            words = line.strip().split()
            for w in words:
                if w == word:
                    ctr+=1
    return ctr


word = 'Py'
count = count_word_occurance('example.txt', word)
print(f'The word "{word}" occurs {count} times in the file.')

