from src.vacancies import Vacancy


def get_vacancies_list(vacancies_info: list) -> list[Vacancy]:
    """
    Преобразовывает список вакансий из общего списка вакансий hh.ru в список объектов Vacancy
    """

    vacancies_list = []
    for vacancy in vacancies_info:
        vacancies_list.append(Vacancy(vacancy['name'],
                                      vacancy['url'],
                                      f'{vacancy['salary']['from'] if vacancy['salary']['from'] else '0'} - '
                                      f'{vacancy['salary']['to'] if vacancy['salary']['to'] else '0'}',
                                      vacancy['salary']['currency'],
                                      vacancy['snippet']['responsibility'],
                                      vacancy['snippet']['requirement']))

    return vacancies_list


def filter_vacancies(vacancies: list[Vacancy],
                     filter_words: list,
                     salary_range: str,
                     currency: str,
                     top_n: int) -> list[Vacancy]:
    """
    Фильтрует вакансии по ключевым словам и зарплате
    """
    salary = [int(i) for i in salary_range.split(' - ')]
    n = 0
    filtered_vacancies = []
    for vacancy in vacancies:

        if ([word for word in filter_words if word.lower() in str(vacancy.responsibility).lower().split()] != []
                or [word for word in filter_words if word.lower() in str(vacancy.requirement).lower().split()] != []):
            vacancy_salary = [int(i) for i in vacancy.salary.split(' - ')]
            if salary[0] <= vacancy_salary[0] and salary[1] >= vacancy_salary[1] and vacancy.currency == currency:
                n += 1
                filtered_vacancies.append(vacancy)

        elif filter_words == []:
            vacancy_salary = [int(i) for i in vacancy.salary.split(' - ')]
            if salary[0] <= vacancy_salary[0] and salary[1] >= vacancy_salary[1] and vacancy.currency == currency:
                n += 1
                filtered_vacancies.append(vacancy)

        if n == top_n:
            break

    print('_______________________')

    print(f'По Вашему запросу найдено {n} вакансий')

    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies: list) -> str:
    """
    Сортирует отобранные вакансии по зарплате
    """
    vacancies_by_salary = []
    for vacancy in sorted(filtered_vacancies,
                          key=lambda x: int(x.salary.split(
                              ' - ')[1]) if int(x.salary.split(' - ')[1]) > 0 else int(x.salary.split(' - ')[0]),
                          reverse=True):
        vacancies_by_salary.append(vacancy)
        print(vacancy)

    return '_______________________'
