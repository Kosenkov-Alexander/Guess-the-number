import random

user_number = int(input('Загадайте число компьютеру от 1 до 100: '))
min = 1
max = 100

while True:
    computer = random.randint(min, max)
    answer = input(f'Компьютер назвал число {computer} Ваш ответ? ')
    if answer == '>':
        min = computer
    elif answer == '<':
        max = computer
    elif computer == user_number:
        print('Победа!')
        break