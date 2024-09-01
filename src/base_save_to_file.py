from abc import ABC, abstractmethod


class BaseSaveToFile(ABC):
    """
    Класс BaseSaveToFile - абстрактый класс для сохранения данных в файл
    """

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        pass
