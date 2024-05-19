import timeit

from karp import rabin_karp_search
from knut import kmp_search
from mur import boyer_moore_search


def test_search(input_text: str, substring: str) -> dict:
    return {
        'Боєра-Мура': timeit.timeit(
            lambda: boyer_moore_search(input_text, substring),
            number=1_000
        ),
        'Кнута-Морріса-Пратта': timeit.timeit(
            lambda: kmp_search(input_text, substring),
            number=1_000
        ),
        'Рабіна-Карпа': timeit.timeit(
            lambda: rabin_karp_search(input_text, substring),
            number=1_000
        )
    }


VALID_SEARCH_1 = "Пошук – поширена дія, яка виконується в бізнес-додатках."
VALID_SEARCH_2 = "Створена програмна імітаційна модель рекомендаційної системи для проведення експериментів"
INVALID_SEARCH = "Не існуючий текст якого немає в жодній з статтей"


if __name__ == '__main__':

    with open('стаття 1.txt', 'r', encoding='utf-8') as input_file:
        text_1 = input_file.read()

    print('\nFor existing string, text 1')
    results = test_search(text_1, VALID_SEARCH_1)
    print('\n'.join(f"{key}: {value}" for key, value in results.items()))

    print('\nFor non existing string, text 1')
    results = test_search(text_1, INVALID_SEARCH)
    print('\n'.join(f"{key}: {value}" for key, value in results.items()))

    with open('стаття 2.txt', 'r', encoding='utf-8') as input_file:
        text_2 = input_file.read()

    print('\nFor existing string, text 2')
    results = test_search(text_2, VALID_SEARCH_2)
    print('\n'.join(f"{key}: {value}" for key, value in results.items()))

    print('\nFor non existing string, text 2')
    results = test_search(text_2, INVALID_SEARCH)
    print('\n'.join(f"{key}: {value}" for key, value in results.items()))