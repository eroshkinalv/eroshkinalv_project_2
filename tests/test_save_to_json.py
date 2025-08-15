def test_save_to_json_add(json_saver, json_opener, vacancies, vacancy_a):
    json_saver.filename = 'test_vacancies'
    assert json_saver.filename == 'test_vacancies'
    json_saver.data = []
    json_saver.open_file = json_opener
    vacancy = json_saver.vacancy_dict(vacancy_a)
    assert json_saver.vacancy_dict(vacancy_a) == {
        'name': 'Разработчик',
        'url': 'http://hh.ru',
        'salary': '100000 - 150000',
        'currency': 'RUR',
        'resposibility': 'Администрирование серверов Linux',
        'requirements': 'Опыт работы с Linux в качестве администратора от 2 лет'
    }

    json_saver.delete_vacancy(vacancy)
    get_vacancy = json_saver.get_vacancy()
    assert get_vacancy == [{
        'name': 'Разработчик',
        'url': 'http://hh.ru',
        'salary': '100000 - 150000',
        'currency': 'RUR',
        'resposibility': 'Администрирование серверов Linux',
        'requirements': 'Опыт работы с Linux в качестве администратора от 2 лет'
    }]
