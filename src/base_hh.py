from abc import ABC, abstractmethod
from typing import Any


class BaseHH(ABC):
    """
    Класс BaseHH - абстрактый класс для работы с классом HeadHunterAPI
    """

    @abstractmethod
    def get_status(self) -> bool:
        pass

    @abstractmethod
    def get_vacancies(self, *args: Any, **kwargs: Any) -> list:
        pass
