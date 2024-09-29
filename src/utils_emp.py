from src.employers import Employers
from src.utils import get_vacancies_list
from src.db_manager import DBManager
from src.db_creator import DBCreator
import psycopg2


db_manager = DBManager()
db_creator = DBCreator()


def get_employers_list(hh_employers: list) -> list[Employers]:
    """
    Преобразовывает список компаний из общего списка компаний hh.ru в список объектов Employers
    """

    employers_list = []
    for employer in hh_employers:
        employers_list.append(
            Employers(
                employer["id"],
                employer["name"],
                employer["url"],
                employer["vacancies_url"],
                employer["open_vacancies"],
            )
        )

    return employers_list


def fill_in_db_hh_employers(employers: list) -> None:
    """
    Функция вносит данные о работодателях в БД PostgreSQL
    """

    if employers:
        db_creator.add_employer_to_db(employers)


def fill_in_db_hh_vacancies(employers: list) -> dict:
    """
    Функция вносит данные о вакансиях работодателей в БД PostgreSQL
    """
    company_vacancies = {}
    if employers:
        for employer in employers:
            company_vacancies_list = get_vacancies_list(employer.vacancies_list)
            company_vacancies[employer.company_id] = company_vacancies_list
        db_creator.add_vacancy_to_db(company_vacancies)

    return company_vacancies


def join_employers_and_vacancies(
    host: str = "localhost",
    port: str = "5432",
    database: str = "test",
    user: str = "postgres",
    password: str = "123zaq",
) -> None:
    """
    Соединяет БД с работодателями и БД с вакансиями
    """
    with psycopg2.connect(host=host, port=port, database=database, user=user, password=password) as conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS hh_vacancies_of_companies")
            cur.execute(
                "SELECT * INTO hh_vacancies_of_companies FROM hh_vacancies_info "
                "JOIN hh_employers_info USING (hh_company_id)"
            )

    conn.close()
