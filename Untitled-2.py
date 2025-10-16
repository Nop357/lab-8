def main():
    try:
        
        d1 = int(input("Введіть першу цифру: "))
        d2 = int(input("Введіть другу цифру: "))
        d3 = int(input("Введіть третю цифру: "))
        if not (0 <= d1 <= 9 and 0 <= d2 <= 9 and 0 <= d3 <= 9):
            raise ValueError("Введені значення повинні бути цифрами (0-9).")
        numbers = []
        for a in (d1, d2, d3):       
            for b in (d1, d2, d3):    
                for c in (d1, d2, d3): 
                    num = 100*a + 10*b + c
                    numbers.append(num)
        print("Всі можливі трицифрові числа:")
        
        for i, num in enumerate(numbers):
            print(f"{num:4d}", end=' ') 
            if (i + 1) % 5 == 0:       
                print()
        print()
        
    except ValueError as e:
        print(f"Помилка введення: {e}")
    except Exception as e:
        print(f"Сталася невідома помилка: {e}")

if __name__ == "__main__":
    main()