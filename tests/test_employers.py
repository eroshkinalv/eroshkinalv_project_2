def test_employers_init(employer_a):

    assert employer_a.company_name == 'MONSTER inc.'
    assert employer_a.company_url == 'https://hh.ru/employer/123456'
    assert employer_a.company_id == '123456'
    assert employer_a.vacancies_url == 'https://api.hh.ru/vacancies?employer_id=123456&locale=RU'
    assert employer_a.open_vacancies == '123'
    assert employer_a.vacancies_list == []
