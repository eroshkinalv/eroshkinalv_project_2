from src.head_hunter_api import HeadHunterAPI
from src.utils import filter_vacancies, get_vacancies_by_salary, get_vacancies_list
from src.db_manager import DBManager
from src.db_creator import DBCreator
from src.utils_emp import get_employers_list, fill_in_db_hh_employers, fill_in_db_hh_vacancies


def user_interaction() -> str:
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


def user_interaction_employers() -> str:
    """
    Функция для взаимодействия с пользователем по поиску компаний работодателей в БД
    """
    user_input = input("Изменить данные для взаимодействия с БД? (ДА/НЕТ): ")

    if user_input == "ДА":
        db_manager = DBManager(
            input("host: "), input("port: "), input("database: "), input("user: "), input("password: ")
        )
    elif user_input == "НЕТ":
        db_manager = DBManager()

    db_creator = DBCreator()

    db_creator.create_db_employers()
    db_creator.create_db_vacancies()

    user_input = input(
        "Введите названия компаний для внесения в БД "
        "(Яндекс, сбер, SberTech, ozon, Литрес, WILDBERRIES, 2ГИС, МТС, МОСГАЗ, "
        "Правительство Москвы, Московский метрополитен): "
    )

    print("Идет обработка данных...")

    for item in user_input.split(", "):
        search_query = item

        hh_api = HeadHunterAPI()
        hh_employers = hh_api.get_employers(search_query)
        employers = get_employers_list(hh_employers)

        fill_in_db_hh_employers(employers)
        fill_in_db_hh_vacancies(employers)

    db_creator.join_employers_and_vacancies()

    user_input = ""

    while user_input != "0":
        user_input = input(
            """
Что ищем?
1 - Количество вакансий в компаниях
2 - Список всех вакансий
3 - Среднюю зарплату по всем вакансиям
4 - Список вакансий с заплатой выше средней по всем вакансиям
5 - Список вакансий, содержащих ключевое слово
0 - Завершить поиск
Введите число: """
        )

        if user_input == "1":
            db_manager.get_companies_and_vacancies_count()
        if user_input == "2":
            db_manager.get_all_vacancies()
        if user_input == "3":
            db_manager.get_avg_salary()
        if user_input == "4":
            db_manager.get_vacancies_with_higher_salary()
        if user_input == "5":
            db_manager.get_vacancies_with_keyword(input("Введите слово для поиска: "))


if __name__ == "__main__":
    print(user_interaction_employers())
