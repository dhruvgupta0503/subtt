import re

def count_words(string):
    # count the number of words in a given string
    return len(re.findall(r'\w+', string))

def count_chars(string):
    # count the number of characters in a given string
    return len(string)

def count_lines(file):
    # count the number of lines in a given file
    with open(file, 'r', encoding='utf-8') as f:
        return len(f.readlines())

def count_blank_lines(file):
    # count the number of blank lines in a given file
    with open(file, 'r', encoding='utf-8') as f:
        return len([line for line in f.readlines() if line.strip() == ''])

def subtitle_quality(file):
    # calculate the subtitle quality metrics for a given file
    num_lines = count_lines(file)
    num_blank_lines = count_blank_lines(file)
    num_words = 0
    num_chars = 0
    with open(file, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if line.strip() != '':
                num_words += count_words(line)
                num_chars += count_chars(line)
    avg_chars_per_line = num_chars / (num_lines - num_blank_lines)
    avg_words_per_line = num_words / (num_lines - num_blank_lines)
    return {'num_lines': num_lines,
            'num_blank_lines': num_blank_lines,
            'num_words': num_words,
            'num_chars': num_chars,
            'avg_chars_per_line': avg_chars_per_line,
            'avg_words_per_line': avg_words_per_line}

# example usage
file = 'example.srt'
metrics = subtitle_quality(file)
for key, value in metrics.items():
    print(f'{key}: {value}')