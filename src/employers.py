from src.head_hunter_api import HeadHunterAPI


class Employers(HeadHunterAPI):
    """
    Класс для работы с компаниями работодателей.
    """

    __slots__ = ("company_id", "company_name", "company_url", "vacancies_url", "open_vacancies")

    def __init__(
        self, company_id: str, company_name: str, company_url: str, vacancies_url: str, open_vacancies: str
    ) -> None:
        """
        Конструктор информации о компаниях.
        """

        self.company_name = company_name
        self.company_url = company_url
        self.company_id = company_id
        self.vacancies_url = vacancies_url
        self.open_vacancies = open_vacancies
        self.vacancies_list = super().get_employers_vacancies_list(vacancies_url)
