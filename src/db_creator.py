import psycopg2
import logging
from src.db_manager import DBManager


logging.basicConfig(
    filename=r"../log/db_manager.log",
    encoding="utf-8",
    filemode="a",
    format="%(asctime)s, %(filename)s, %(funcName)s, %(levelname)s: %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


class DBCreator(DBManager):
    """
    Класс для создания БД PostgreSQL
    """

    def __init__(
        self,
        host: str = "localhost",
        port: str = "5432",
        database: str = "test",
        user: str = "postgres",
        password: str = "123zaq",
    ) -> None:

        super().__init__(host, port, database, user, password)

    def create_db_employers(self) -> None:
        """
        Создает (локальную) базу данных для хранения данных о работодателях.
        """

        with psycopg2.connect(
            host=self._host, port=self._port, database=self._database, user=self._user, password=self._password
        ) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        "CREATE TABLE IF NOT EXISTS hh_employers_info"
                        "(db_company_id serial, "
                        "hh_company_id int PRIMARY KEY, "
                        "company_name varchar, "
                        "company_url varchar, "
                        "vacancies_url varchar, "
                        "open_vacancies varchar);"
                    )

                except Exception as e:
                    logging.info(e)

        conn.close()

    def create_db_vacancies(self) -> None:
        """
        Создает (локальную) базу данных для хранения данных о вакансиях.
        """
        with psycopg2.connect(
            host=self._host, port=self._port, database=self._database, user=self._user, password=self._password
        ) as conn:
            with conn.cursor() as cur:
                try:
                    cur.execute(
                        "CREATE TABLE IF NOT EXISTS hh_vacancies_info "
                        "(db_vacancy_id serial, "
                        "hh_company_id int, "
                        "hh_vacancy_id int PRIMARY KEY, "
                        "job_name varchar, "
                        "vacancy_url varchar, "
                        "salary_from int, "
                        "salary_to int, "
                        "currency varchar, "
                        "requirement varchar,"
                        "responsibility varchar);"
                    )

                except Exception as e:
                    logging.info(e)

        conn.close()

    def add_employer_to_db(self, employers_list: list) -> None:
        """
        Добавляет работодалей в БД
        """

        for employer in employers_list:
            with psycopg2.connect(
                host=self._host, port=self._port, database=self._database, user=self._user, password=self._password
            ) as conn:
                with conn.cursor() as cur:
                    try:
                        cur.execute(
                            "INSERT INTO hh_employers_info ("
                            "hh_company_id,"
                            "company_name,"
                            "company_url,"
                            "vacancies_url,"
                            "open_vacancies) VALUES (%s, %s, %s, %s, %s)",
                            (
                                int(employer.company_id),
                                employer.company_name,
                                f"{employer.company_url}&per_page=100",
                                employer.vacancies_url,
                                employer.open_vacancies,
                            ),
                        )

                    except Exception as e:
                        logging.info(e)

        conn.close()

    def add_vacancy_to_db(self, company_vacancies: dict) -> None:
        """
        Добавляет вакансии в БД
        """

        for company, vacancies in company_vacancies.items():

            for v in vacancies:

                with psycopg2.connect(
                    host=self._host, port=self._port, database=self._database, user=self._user, password=self._password
                ) as conn:
                    with conn.cursor() as cur:
                        try:
                            cur.execute(
                                "INSERT INTO hh_vacancies_info ("
                                "hh_company_id, "
                                "hh_vacancy_id, "
                                "job_name, "
                                "vacancy_url, "
                                "salary_from, "
                                "salary_to, "
                                "currency, "
                                "requirement, "
                                "responsibility) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                                (
                                    int(company),
                                    int(v.job_id),
                                    v.job_name,
                                    v.vacancy_url,
                                    v.salary.split(" - ")[0],
                                    v.salary.split(" - ")[1],
                                    v.currency,
                                    v.responsibility,
                                    v.requirement,
                                ),
                            )

                        except Exception as e:
                            logging.info(e)

        conn.close()

    def join_employers_and_vacancies(self) -> None:
        """
        Соединяет БД с работодателями и БД с вакансиями
        """
        with psycopg2.connect(
            host=self._host, port=self._port, database=self._database, user=self._user, password=self._password
        ) as conn:
            with conn.cursor() as cur:
                cur.execute("DROP TABLE IF EXISTS hh_vacancies_of_companies")
                cur.execute(
                    "ALTER TABLE hh_vacancies_info ADD FOREIGN KEY (hh_company_id) "
                    "REFERENCES hh_employers_info(hh_company_id)"
                )
                cur.execute(
                    "SELECT * INTO hh_vacancies_of_companies FROM hh_vacancies_info "
                    "JOIN hh_employers_info USING (hh_company_id)"
                )

        conn.close()
