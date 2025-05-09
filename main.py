def truncate_string(s, length):
    return s[:length] + '...' if length >= 0 and len(s) > length else s

# Пример использования функции
result = truncate_string('Привет, как дела?', 10)
print(result)
