import random


def main():
    score = int(input('Enter your score: '))
    result = get_result(score)

    random_score = random.randint(0, 100)
    print('Random score:', random_score)
    result = get_result(random_score)


def get_result(score):
    if score < 50:
        print('Fail')
    elif score >= 50 and score <= 64:
        print('Pass')
    elif score >= 65 and score <= 74:
        print('Pass with Credit')
    elif score >= 75 and score <= 84:
        print('Pass with Distinction')
    elif score >= 85 and score <= 100:
        print('Pass with High Distinction')


main()
