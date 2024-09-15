def test_vacancies_init(vacancy_a):
    assert vacancy_a.job_name == 'Разработчик'
    assert vacancy_a.vacancy_url == 'http://hh.ru'
    assert vacancy_a.salary == '100000 - 150000'
    assert vacancy_a.currency == 'RUR'
    assert vacancy_a.requirement == 'Опыт работы с Linux в качестве администратора от 2 лет'
    assert vacancy_a.responsibility == 'Администрирование серверов Linux'


def test_vacancies_str(vacancy_a):
    assert str(vacancy_a) == ('Разработчик (http://hh.ru) -- Зарплата: 100000 - 150000 RUR -- '
                              'Обязанности: Администрирование серверов Linux -- '
                              'Требования: Опыт работы с Linux в качестве администратора от 2 лет')


def test_vacancies_eq(vacancy_a, vacancy_b):
    assert vacancy_a.salary == vacancy_b.salary


def test_vacancies_lt(vacancy_a, vacancy_c):
    assert vacancy_a.salary > vacancy_c.salary


def test_vacancies_le(vacancy_a, vacancy_d):
    assert vacancy_a.salary < vacancy_d.salary
