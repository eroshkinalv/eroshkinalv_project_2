import pytest


def test_create_db_employers(capsys, db_b):
    db_b.create_db_employers()
    with pytest.raises(Exception) as e:
        assert e == 'Ошибка в БД'


def test_create_db_vacancies(capsys, db_b):
    db_b.create_db_vacancies()
    with pytest.raises(Exception) as e:
        assert e == 'Ошибка в БД'


def test_add_employer_to_db(capsys, db_b, employers_list_a):
    db_b.add_employer_to_db(employers_list_a)
    with pytest.raises(Exception) as e:
        assert e == 'Ошибка в БД'


def test_add_vacancy_to_db(capsys, db_b, vacancies_list_a):
    db_b.add_employer_to_db(vacancies_list_a)
    with pytest.raises(Exception) as e:
        assert e == 'Ошибка в БД'