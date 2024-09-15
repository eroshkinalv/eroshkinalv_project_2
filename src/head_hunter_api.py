import requests

from src.base_hh import BaseHH


class HeadHunterAPI(BaseHH):
    """
    Класс для работы с API HeadHunter
    """

    __url: str
    __vacancies: list
    __connection: bool

    @property
    def get_status(self) -> bool:
        """
        Проверка подключения к hh.ru
        """

        if requests.get('https://httpbin.org/get').status_code == 200:
            self.__connection = True

        else:
            self.__connection = False

        return self.__connection

    def get_vacancies(self, search_query: str, per_page: int = 100) -> list:
        """
        Возвращаает список вакансий, содержащих поисковый запрос (search_query)
        """

        if self.get_status:
            self.__url = f'https://api.hh.ru/vacancies?text={search_query}&per_page={per_page}&only_with_salary={True}'
            self.__vacancies = requests.get(self.__url).json()['items']

        return self.__vacancies
