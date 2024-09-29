from abc import ABC, abstractmethod
from typing import Any


class BaseDB(ABC):
    """
    Класс BaseDB - абстрактый класс для работы с клаcсом вызаимодействующим с БД PostgreSQL
    """

    @abstractmethod
    def get_companies_and_vacancies_count(self) -> None:
        pass

    @abstractmethod
    def get_all_vacancies(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def get_avg_salary(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def get_vacancies_with_higher_salary(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def get_vacancies_with_keyword(self, *args: Any, **kwargs: Any) -> None:
        pass
