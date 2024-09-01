from src.head_hunter_api import HeadHunterAPI
from src.vacancies import Vacancy
from src.utils import get_vacancies_list, filter_vacancies, get_vacancies_by_salary

# # Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()
#
# # Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies("Python")
#
# # Преобразование набора данных из JSON в список объектов
# vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
#
# # Пример работы контструктора класса с одной вакансией
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.delete_vacancy(vacancy)

# Функция для взаимодействия с пользователем
def user_interaction():
    """
    Функция для взаимодействия с пользователем
    """

    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат (Пример: 100000 - 150000): ") # Пример: 100000 - 150000
    currency = input("Введите валюту зарплаты (RUR, USD, EUR): ") # RUR, USD, EUR

    hh_api = HeadHunterAPI()
    hh_vacancies = hh_api.get_vacancies(search_query)

    vacancies_list = get_vacancies_list(hh_vacancies)
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words, salary_range, currency, top_n)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies)

    return ranged_vacancies


if __name__ == "__main__":
    print(user_interaction())
