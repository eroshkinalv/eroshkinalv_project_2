import json

from src.base_save_to_file import BaseSaveToFile
from src.vacancies import Vacancy


class JSONSaver(BaseSaveToFile):
    """
    Класс для сохранения вакансий в JSON-файл
    """

    __filename: str

    def __init__(self, filename: str = 'vacancies_file') -> None:
        self.__filename = filename
        self.open_file()

    def open_file(self) -> None:
        """
        Открывает файл с вакансиями
        """

        try:
            with open(rf'..\data\{self.__filename}.json', 'r', encoding='utf-8') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = []

    def vacancy_dict(self, vacancy: Vacancy) -> dict:
        """
        Преобразует объект Vacancy в словарь
        """

        vacancy_data = {
            'name': vacancy.job_name,
            'url': vacancy.vacancy_url,
            'salary': vacancy.salary,
            'currency': vacancy.currency,
            'resposibility': vacancy.responsibility,
            'requirements': vacancy.requirement
        }

        self.data.append(vacancy_data)
        self.add_vacancy()
        return vacancy_data

    def add_vacancy(self) -> None:
        """
        Сохраняет файл с вакансиями
        """

        with open(rf'..\data\{self.__filename}.json', 'w', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def delete_vacancy(self, vacancy: dict) -> None:
        """
        Удаляет вакансии
        """

        for i, datum in enumerate(self.data):
            if vacancy.get('url') == datum.get('url'):
                self.data.pop(i)
        self.add_vacancy()

    def get_vacancy(self) -> None:
        """
        Получает вакансии
        """

        return self.data
