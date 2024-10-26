import psycopg2
from src.base_db_manager import BaseDB
import logging


logging.basicConfig(
    filename=r"../log/db_manager.log",
    encoding="utf-8",
    filemode="a",
    format="%(asctime)s, %(filename)s, %(funcName)s, %(levelname)s: %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class DBManager(BaseDB):
    """
    Класс для работы с БД PostgreSQL
    """

    def __init__(
        self,
        host: str = "localhost",
        port: str = "5432",
        database: str = "test",
        user: str = "postgres",
        password: str = "123zaq",
    ) -> None:

        self._host = host
        self._port = port
        self._database = database
        self._user = user
        self._password = password

    def get_companies_and_vacancies_count(self) -> None:
        """
        Получает список всех компаний и количество вакансий у каждой компании
        """
        with psycopg2.connect(
            host=self._host, port=self._port, database=self._database, user=self._user, password=self._password
        ) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        "SELECT company_name, COUNT(job_name) " "FROM hh_vacancies_of_companies GROUP BY company_name"
                    )

                except Exception as e:
                    logging.info(e)

                else:
                    for company in cur.fetchall():
                        print(f"{company[0]}: {int(company[1])}")

        conn.close()

        print("_______________________")

    def get_all_vacancies(self) -> None:
        """
        Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        """
        with psycopg2.connect(
            host=self._host, port=self._port, database=self._database, user=self._user, password=self._password
        ) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        "SELECT company_name, job_name, salary_from, salary_to, currency, vacancy_url "
                        "FROM hh_vacancies_of_companies ORDER BY company_name"
                    )

                except Exception as e:
                    logging.info(e)

                else:
                    companies_and_vacancies = cur.fetchall()
                    for vacancy in companies_and_vacancies:
                        print(
                            f"{vacancy[0]} -- {vacancy[1]} -- {vacancy[2]}-{vacancy[3]} {vacancy[4]} -- "
                            f"{vacancy[5]}"
                        )

        conn.close()

        print("_______________________")

    def get_avg_salary(self) -> None:
        """
        Получает среднюю зарплату по вакансиям
        """
        with psycopg2.connect(
            host=self._host, port=self._port, database=self._database, user=self._user, password=self._password
        ) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        "SELECT AVG((salary_from + salary_to)/2), currency, job_name "
                        "FROM hh_vacancies_info WHERE salary_from > 0 AND salary_to > 0 "
                        "GROUP BY job_name, currency"
                    )
                    salary_info = cur.fetchall()

                    for vacancy in salary_info:
                        print(f"{vacancy[2]}: {round(vacancy[0])} {vacancy[1]}")
                    cur.execute(
                        "SELECT AVG((salary_from + salary_to)/2), currency, job_name "
                        "FROM hh_vacancies_info WHERE salary_from = 0 OR salary_to = 0 "
                        "GROUP BY job_name, currency"
                    )
                    salary_info = cur.fetchall()

                    for vacancy in salary_info:
                        print(f"{vacancy[2]}: {round(vacancy[0])} {vacancy[1]}")

                except Exception as e:
                    logging.info(e)

        conn.close()

        print("_______________________")

    def get_vacancies_with_higher_salary(self) -> None:
        """
        Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        """
        with psycopg2.connect(
            host=self._host, port=self._port, database=self._database, user=self._user, password=self._password
        ) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        "SELECT * FROM hh_vacancies_of_companies WHERE salary_from > "
                        "(SELECT AVG((salary_from + salary_to)/2) FROM hh_vacancies_of_companies) "
                        "OR salary_to > (SELECT AVG((salary_from + salary_to)/2) FROM hh_vacancies_of_companies)"
                    )

                except Exception as e:
                    logging.info(e)

                else:
                    high_salary_vacancies = cur.fetchall()
                    for vacancy in high_salary_vacancies:
                        print(
                            f"{vacancy[11]} -- {vacancy[3]} ({vacancy[4]}) -- {vacancy[5]}-{vacancy[6]} "
                            f"{vacancy[7]} -- {vacancy[8]} -- {vacancy[9]} "
                        )

        conn.close()

        print("_______________________")

    def get_vacancies_with_keyword(self, keyword: str) -> None:
        """
        Получает список всех вакансий, в названии которых содержится переданное в метод слово.
        """
        with psycopg2.connect(
            host=self._host, port=self._port, database=self._database, user=self._user, password=self._password
        ) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        f"SELECT * FROM hh_vacancies_of_companies WHERE LOWER(job_name) "
                        f"LIKE LOWER('%{keyword}%') OR LOWER(requirement) LIKE LOWER('%{keyword}%') "
                        f"OR LOWER(responsibility) LIKE LOWER('%{keyword}%')"
                    )

                except Exception as e:
                    logging.info(e)

                else:
                    for vacancy in cur.fetchall():
                        if keyword.lower() in vacancy[3].lower():
                            print(
                                f"{vacancy[11]} -- {vacancy[3]} ({vacancy[4]}) -- {vacancy[5]}-{vacancy[6]} "
                                f"{vacancy[7]} -- {vacancy[8]} -- {vacancy[9]} "
                            )

                        if vacancy[8] is not None and keyword.lower() in vacancy[8].lower():
                            print(
                                f"{vacancy[11]} -- {vacancy[3]} ({vacancy[4]}) -- {vacancy[5]}-{vacancy[6]} "
                                f"{vacancy[7]} -- {vacancy[8]} -- {vacancy[9]} "
                            )

        conn.close()

        print("_______________________")
