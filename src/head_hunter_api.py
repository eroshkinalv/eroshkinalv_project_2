import requests

from src.base_hh import BaseHH


class HeadHunterAPI(BaseHH):
    """
    Класс для работы с API HeadHunter
    """

    __url: str
    __vacancies: list
    __connection: bool
    __employers: list

    @property
    def get_status(self) -> bool:
        """
        Проверка подключения к hh.ru
        """

        if requests.get("https://httpbin.org/get").status_code == 200:
            self.__connection = True

        else:
            self.__connection = False

        return self.__connection

    def get_vacancies(self, search_query: str, per_page: int = 100) -> list:
        """
        Возвращаает список вакансий, содержащих поисковый запрос (search_query)
        """

        if self.get_status:
            self.__url = f"https://api.hh.ru/vacancies?text={search_query}&per_page={per_page}&only_with_salary={True}"
            self.__vacancies = requests.get(self.__url).json()["items"]

        return self.__vacancies

    def get_employers(self, search_query: str, location: str = "RU", per_page: int = 100) -> list:
        """
        Возвращает список компаний, содержащих поисковый запрос (search_query)
        """

        if self.get_status:
            self.__url = f"https://api.hh.ru/employers?text={search_query}&locale={location}&per_page={per_page}"
            self.__employers = [
                v for v in requests.get(self.__url).json()["items"] if v["name"].lower() == search_query.lower()
            ]

        return self.__employers

    def get_employers_vacancies_list(self, url: str) -> list:

        self.__url = url
        self.__vacancies = requests.get(f"{self.__url}&per_page=100").json()["items"]

        return self.__vacancies
