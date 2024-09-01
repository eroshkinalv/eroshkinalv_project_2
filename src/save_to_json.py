import json
from src.base_save_to_file import BaseSaveToFile
from src.vacancies import Vacancy


class JSONSaver(BaseSaveToFile):
    """
    Класс для сохранения вакансий в JSON-файл
    """

    __filename: str

    def __init__(self, filename='vacancies_file') -> None:
        self.__filename = filename
        self.open_file()

    def open_file(self):
        """Открывает файл с вакансиями"""

        try:
            with open(rf'..\data\{self.__filename}.json') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}

    def save_data(self):
        """Сохраняет файл с вакансиями"""

        with open(self.__filename, 'a', encoding='utf-8') as file:
            json.dump(self.data, file, indent=4, ensure_ascii=False)

    def add_vacancy(self, vacancy: Vacancy):
        """Добавляет вакансии в файл"""

        self.data = {
            'name': vacancy.job_name,
            'url': vacancy.vacancy_url,
            'salary': vacancy.salary,
            'currency': vacancy.currency,
            'resposibility': vacancy.responsibility,
            'requirements': vacancy.requirement
            }
        self.save_data()

    def delete_vacancy(self, vacancy):
        """Удаляет вакансии"""

        if vacancy['name'] == self.data.name:
            del self.data
        self.save()

    def get_vacancy(self):
        """Получает вакансии"""

        return self.data


    # def save_to_file(self, vacancy: Vacancy) -> None:
    #     """
    #     Сохряняет объект класса Vcancy в файл
    #     """
    #
    #     data = vars(vacancy)
    #
    #     with open(rf'..\data\{self.filename}.json', 'w') as file:
    #         json.dump(data, file, indent=4, ensure_ascii=False)
    #
    #     return data, dict_data

    # def class_to_dict(self, vacancy: Vacancy):
    #     """
    #     Переводит объект класса Vacancy в слооварь
    #     """
    #
    #     vacancies = []
    #     vacancy_dict = {
    #         'name': vacancy.job_name,
    #         'url': vacancy.vacancy_url,
    #         'salary': vacancy.salary,
    #         'currency': vacancy.currency,
    #         'resposibility': vacancy.responsibility,
    #         'requirements': vacancy.requirement
    #     }
    #     vacancies.append(vacancy_dict)
    #
    #     return vacancies

    # def data_to_add(self, vacancies):
    #     """
    #     Формирует список вакансий для добавления/удаления
    #     """
    #
    #     with open(r'..\data\vacancies_file.json', 'r', encoding='utf-8') as file:
    #         data = json.load(file)
    #
    #     return data

    # def add_vacancy(self, vacancies):
    #
    #     for vacancy in vacancies:
    #
    #         with open(r'..\data\vacancies_file.json', 'a', encoding='utf-8') as file:
    #             json.dump(vacancy, file, indent=4, ensure_ascii=False)
    #
    #
    # def delete_vacancy(self, vacancy):
    #     pass
    #
    # # def __exit__(self):
    # #     self.json_file.close()


if __name__ == '__main__':

    vacancy1 = Vacancy('Разработчик', 'http://hh.ru', '100000 - 150000', 'RUR', 'Администрирование серверов Linux',
                       'Опыт работы с Linux в качестве администратора от 2 лет')
    # j_saver = JSONSaver(vacancy1)
    # print(j_saver.vacancy)
    # vacancy_dict = j_saver.class_to_dict(vacancy1)
    # print(j_saver.data_to_add(vacancy_dict))
    # # data = j_saver.data_to_add(vacancy_dict)
    # print(j_saver.add_vacancy(vacancy_dict))

    j_saver = JSONSaver()

    print(j_saver.data)

    j_saver.add_vacancy(vacancy1)

    j_saver.save_data()