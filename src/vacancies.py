from src.head_hunter_api import HeadHunterAPI


class Vacancy(HeadHunterAPI):
    """
    Класс для работы с вакансиями.
    """

    __slots__ = ("job_name", "vacancy_url", "salary", "currency", "requirement", "responsibility", "job_id")

    def __init__(
        self,
        job_name: str,
        vacancy_url: str,
        salary: str,
        currency: str,
        responsibility: str,
        requirement: str,
        job_id: str,
    ) -> None:
        """
        Конструктор вакансий
        """
        self.job_id = job_id
        self.job_name = job_name
        self.vacancy_url = vacancy_url
        self.salary = salary
        self.currency = currency
        self.requirement = requirement
        self.responsibility = responsibility

    def __str__(self) -> str:
        return (
            f"{self.job_name} "
            f"({self.vacancy_url}) -- "
            f"Зарплата: {self.salary} {self.currency} -- "
            f"Обязанности: {self.responsibility} -- "
            f"Требования: {self.requirement}"
        )

    def __eq__(self, other: "Vacancy") -> bool:
        """
        Метод для проверки зарплат вакансий - равно
        """

        if int(self.salary.split(" - ")[0]) < int(other.salary.split(" - ")[0]) and int(
            self.salary.split(" - ")[1]
        ) == int(other.salary.split(" - ")[1]):
            return True
        else:
            return False

    def __lt__(self, other: "Vacancy") -> bool:
        """
        Метод для проверки зарплат вакансий - меньше
        """

        if int(self.salary.split(" - ")[0]) <= int(other.salary.split(" - ")[0]) and int(
            self.salary.split(" - ")[1]
        ) == int(other.salary.split(" - ")[1]):
            return True
        else:
            return False

    def __le__(self, other: "Vacancy") -> bool:
        """
        Метод для проверки зарплат вакансий - меньше или равно
        """

        if int(self.salary.split(" - ")[0]) <= int(other.salary.split(" - ")[0]) and int(
            self.salary.split(" - ")[1]
        ) == int(other.salary.split(" - ")[1]):
            return True
        else:
            return False
