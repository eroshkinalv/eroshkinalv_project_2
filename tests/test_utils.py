from src.utils import filter_vacancies, get_vacancies_by_salary, get_vacancies_list


def test_get_vacancies_list(capsys, vacancies):
    print(*get_vacancies_list(vacancies))
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == ('Python – разработчик '
                                                   '(https://api.hh.ru/vacancies/106529103?host=hh.ru) -'
                                                   '- Зарплата: 0 - 230000 RUR -'
                                                   '- Обязанности: Проектирование и '
                                                   'разработка новых фич и интеграций. '
                                                   'Небольшой процент поддержки и оптимизации кода. '
                                                   'Ревью кода других разработчиков команды.  -'
                                                   '- Требования: От 2+ лет коммерческого опыта в релевантном стеке. '
                                                   'Опыт проектирования сервисов. Опыт работы с асинхронным кодом. '
                                                   'Понимание алгоритмов и...')


def test_filter_vacancies(capsys, vacancies_data):
    vacancies_list = get_vacancies_list(vacancies_data)
    filtered_vacancies = filter_vacancies(vacancies_list,
                                          ['SQL'],
                                          '90000 - 100000',
                                          'RUR',
                                          5)
    print(*filtered_vacancies)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == ('Аналитик (https://api.hh.ru/vacancies/106501725?host=hh.ru) -'
                                                   '- Зарплата: 90000 - 0 RUR -- Обязанности: Разработка, внедрение, '
                                                   'поддержка отчетов на платформе Power BI. Сбор исходных данных. '
                                                   'Взаимодействие с внутренним заказчиком. '
                                                   'Уточнение требований к отчету.  -'
                                                   '- Требования: Высшее техническое образование будет преимуществом. '
                                                   'Высокий уровень владения Power BI, Excel. Знание DAX. '
                                                   'Приветствуется знание SQL и '
                                                   '<highlighttext>Python</highlighttext>.  '
                                                   'Аналитик (https://api.hh.ru/vacancies/106501725?host=hh.ru) -'
                                                   '- Зарплата: 90000 - 100000 RUR -- Обязанности: Разработка, '
                                                   'внедрение, поддержка отчетов на платформе Power BI. '
                                                   'Сбор исходных данных. Взаимодействие с внутренним заказчиком. '
                                                   'Уточнение требований к отчету.  -'
                                                   '- Требования: Высшее техническое образование будет преимуществом. '
                                                   'Высокий уровень владения Power BI, Excel. Знание DAX. '
                                                   'Приветствуется знание SQL и '
                                                   '<highlighttext>Python</highlighttext>.')


def test_get_vacancies_by_salary(capsys, vacancies_data):
    vacancies_list = get_vacancies_list(vacancies_data)
    filtered_vacancies = filter_vacancies(vacancies_list,
                                          ['SQL'],
                                          '90000 - 100000',
                                          'RUR',
                                          5)

    get_vacancies_by_salary(filtered_vacancies)

    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == ('Аналитик (https://api.hh.ru/vacancies/106501725?host=hh.ru) -'
                                                   '- Зарплата: 90000 - 0 RUR -- Обязанности: Разработка, внедрение, '
                                                   'поддержка отчетов на платформе Power BI. Сбор исходных данных. '
                                                   'Взаимодействие с внутренним заказчиком. '
                                                   'Уточнение требований к отчету.  -'
                                                   '- Требования: Высшее техническое образование будет преимуществом. '
                                                   'Высокий уровень владения Power BI, Excel. Знание DAX. '
                                                   'Приветствуется знание SQL и '
                                                   '<highlighttext>Python</highlighttext>.')


def test_get_vacancies_by_salary_return(capsys, vacancies_data):
    vacancies_list = get_vacancies_list(vacancies_data)
    filtered_vacancies = filter_vacancies(vacancies_list,
                                          ['SQL'],
                                          '90000 - 100000',
                                          'RUR',
                                          5)

    get_vacancies_filtered_by_salary = get_vacancies_by_salary(filtered_vacancies)
    print(get_vacancies_filtered_by_salary)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == ('_______________________')
