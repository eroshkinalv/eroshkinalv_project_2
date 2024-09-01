from abc import ABC, abstractmethod


class BaseHH(ABC):
    """
    Класс BaseHH - абстрактый класс для работы с классом HeadHunterAPI
    """

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def get_vacancies(self, *args, **kwargs):
        pass
