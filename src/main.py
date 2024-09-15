from src.head_hunter_api import HeadHunterAPI
from src.utils import filter_vacancies, get_vacancies_by_salary, get_vacancies_list


def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ")
    currency = input("Введите валюту зарплаты (RUR, USD, EUR): ")

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)

    vacancies_list = get_vacancies_list(hh_vacancies)
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words, salary_range, currency, top_n)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies)

    return ranged_vacancies
