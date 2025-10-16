def process_single_string():
    str1 = input("Введіть перший рядок: ")
    str2 = input("Введіть другий рядок: ")
    unique_chars = []
    for char in str1:
        if char not in str2 and char not in unique_chars:
            unique_chars.append(char)
    if unique_chars:
        print("Символи, які є у першому рядку і відсутні у другому:")
        print(''.join(unique_chars))
    else:
        print("У першому рядку немає символів, яких би не було у другому рядку")
if __name__ == "__main__":
    process_single_string()