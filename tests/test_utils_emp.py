from src.utils_emp import get_employers_list, fill_in_db_hh_vacancies


def test_get_employers_list(capsys, employers):
    assert len(get_employers_list(employers)) == 1
    for employer in get_employers_list(employers):

        assert employer.company_name == 'Ozon'
        assert employer.company_url == 'https://api.hh.ru/employers/2180?locale=RU'
        assert employer.company_id == '2180'
        assert employer.vacancies_url == 'https://api.hh.ru/vacancies?employer_id=2180&locale=RU'
        assert employer.open_vacancies == 15726


def test_fill_in_db_hh_vacancies(employers_list, vacancy_a):

    result = fill_in_db_hh_vacancies(employers_list)

    assert result == {}
