from abc import ABC, abstractmethod
from typing import Any


class BaseSaveToFile(ABC):
    """
    Класс BaseSaveToFile - абстрактый класс для сохранения данных в файл
    """

    @abstractmethod
    def add_vacancy(self, *args: Any, **kwargs: Any) -> None:
        pass

    @abstractmethod
    def delete_vacancy(self, *args: Any, **kwargs: Any) -> None:
        pass
