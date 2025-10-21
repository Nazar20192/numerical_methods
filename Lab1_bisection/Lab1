
def guess_number_game():
    print("=== Гра 'Вгадай число' ===")
    print("Загадай ціле число від 1 до n, а комп'ютер спробує його вгадати!")

    # Користувач задає верхню межу
    n = int(input("Введи максимальне число n: "))

    low = 1
    high = n
    guesses = 0

    input("Натисни Enter, коли загадаєш число...")

    while low <= high:
        guesses += 1
        mid = (low + high) // 2
        print(f"Мій варіант: {mid}")

        response = input("Це твоє число? (так/більше/менше): ").lower()

        if response == "так":
            print(f"Я вгадав твоє число {mid} за {guesses} спроб(и)!")
            break
        elif response == "більше":
            low = mid + 1
        elif response == "менше":
            high = mid - 1
        else:
            print("Будь ласка, відповідай лише: 'так', 'більше' або 'менше'.")

    print("Дякую за гру!")

guess_number_game()
