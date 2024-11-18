
def calculator():
    while True:
        try:
            print("\nПростой калькулятор")
            print("1. Сложение (+)")
            print("2. Вычитание (-)")
            print("3. Умножение (*)")
            print("4. Деление (/)")
            print("5. Выход")
            
            choice = input("Выберите операцию (1-5): ")
            
            if choice == '5':
                print("До свидания!")
                break
                
            if choice not in ['1', '2', '3', '4']:
                print("Неверный выбор. Попробуйте снова.")
                continue
                
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            
            if choice == '1':
                print(f"Результат: {num1 + num2}")
            elif choice == '2':
                print(f"Результат: {num1 - num2}")
            elif choice == '3':
                print(f"Результат: {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Ошибка: деление на ноль!")
                else:
                    print(f"Результат: {num1 / num2}")
                    
        except ValueError:
            print("Ошибка: введите корректное число!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    calculator()
