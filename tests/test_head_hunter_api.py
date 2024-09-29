import requests
import responses


def test_head_hunter_api_get_status(hh_status):
    assert hh_status.get_status is True


@responses.activate
def test_head_hunter_api_get_vacancies(vacancies):

    responses.add(responses.GET, 'http://example.com', json=vacancies, status=200)
    resp = requests.get('http://example.com')

    assert resp.json() == [{'id': '106529103',
                            'premium': False, 'name': 'Python – разработчик', 'department': None, 'has_test': True,
                            'response_letter_required': False,
                            'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
                            'salary': {'from': None, 'to': 230000, 'currency': 'RUR', 'gross': False},
                            'type': {'id': 'open', 'name': 'Открытая'},
                            'address': {'city': 'Москва', 'street': 'Рубцовская набережная', 'building': '3с1',
                                        'lat': 55.776613,
                                        'lng': 37.699975, 'description': None,
                                        'raw': 'Москва, Рубцовская набережная, 3с1',
                                        'metro': {'station_name': 'Бауманская', 'line_name': 'Арбатско-Покровская',
                                                  'station_id': '3.17', 'line_id': '3', 'lat': 55.772405,
                                                  'lng': 37.67904},
                                        'metro_stations': [{'station_name': 'Бауманская',
                                                            'line_name': 'Арбатско-Покровская',
                                                            'station_id': '3.17', 'line_id': '3', 'lat': 55.772405,
                                                            'lng': 37.67904}],
                                        'id': '1885643'}, 'response_url': None, 'sort_point_distance': None,
                            'published_at': '2024-08-29T18:31:09+0300', 'created_at': '2024-08-29T18:31:09+0300',
                            'archived': False,
                            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106529103',
                            'show_logo_in_search': None,
                            'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/106529103?host=hh.ru',
                            'alternate_url': 'https://hh.ru/vacancy/106529103', 'relations': [],
                            'employer': {'id': '3202190', 'name': 'KTS', 'url': 'https://api.hh.ru/employers/3202190',
                                         'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/5626348.png',
                                                       '240': 'https://img.hhcdn.ru/employer-logo/5626349.png',
                                                       'original': 'https://img.hhcdn.ru/employer-logo-original/'
                                                                   '1001392.png'},
                                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3202190',
                                         'accredited_it_employer': True,
                                         'trusted': True},
                            'snippet': {'requirement': 'От 2+ лет коммерческого опыта в релевантном стеке. '
                                                       'Опыт проектирования сервисов. '
                                                       'Опыт работы с асинхронным кодом. '
                                                       'Понимание алгоритмов и...',
                                        'responsibility': 'Проектирование и разработка новых фич и интеграций. '
                                                          'Небольшой процент поддержки и оптимизации кода. '
                                                          'Ревью кода других разработчиков команды. '},
                            'contacts': None,
                            'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
                            'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
                            'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                            'accept_incomplete_resumes': False,
                            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
                            'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
                            'is_adv_vacancy': False,
                            'adv_context': None}]


@responses.activate
def test_head_hunter_api_get_employers(employers):

    responses.add(responses.GET, 'http://example.com', json=employers, status=200)
    resp = requests.get('http://example.com')

    assert resp.json() == [{'id': '2180', 'name': 'Ozon', 'url': 'https://api.hh.ru/employers/2180?locale=RU',
                            'alternate_url': 'https://hh.ru/employer/2180',
                            'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1069622.png',
                                          '240': 'https://img.hhcdn.ru/employer-logo/5899118.png',
                                          '90': 'https://img.hhcdn.ru/employer-logo/5899117.png'},
                            'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=2180&locale=RU',
                            'open_vacancies': 15726}]


@responses.activate
def test_head_hunter_api_get_employers_vacancies_list(vacancies):

    responses.add(responses.GET, 'http://example.com', json=vacancies, status=200)
    resp = requests.get('http://example.com')

    assert resp.json() == [{'id': '106529103',
                            'premium': False, 'name': 'Python – разработчик', 'department': None, 'has_test': True,
                            'response_letter_required': False,
                            'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
                            'salary': {'from': None, 'to': 230000, 'currency': 'RUR', 'gross': False},
                            'type': {'id': 'open', 'name': 'Открытая'},
                            'address': {'city': 'Москва', 'street': 'Рубцовская набережная', 'building': '3с1',
                                        'lat': 55.776613,
                                        'lng': 37.699975, 'description': None,
                                        'raw': 'Москва, Рубцовская набережная, 3с1',
                                        'metro': {'station_name': 'Бауманская', 'line_name': 'Арбатско-Покровская',
                                                  'station_id': '3.17', 'line_id': '3', 'lat': 55.772405,
                                                  'lng': 37.67904},
                                        'metro_stations': [{'station_name': 'Бауманская',
                                                            'line_name': 'Арбатско-Покровская',
                                                            'station_id': '3.17', 'line_id': '3', 'lat': 55.772405,
                                                            'lng': 37.67904}],
                                        'id': '1885643'}, 'response_url': None, 'sort_point_distance': None,
                            'published_at': '2024-08-29T18:31:09+0300', 'created_at': '2024-08-29T18:31:09+0300',
                            'archived': False,
                            'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106529103',
                            'show_logo_in_search': None,
                            'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/106529103?host=hh.ru',
                            'alternate_url': 'https://hh.ru/vacancy/106529103', 'relations': [],
                            'employer': {'id': '3202190', 'name': 'KTS', 'url': 'https://api.hh.ru/employers/3202190',
                                         'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/5626348.png',
                                                       '240': 'https://img.hhcdn.ru/employer-logo/5626349.png',
                                                       'original': 'https://img.hhcdn.ru/employer-logo-original/'
                                                                   '1001392.png'},
                                         'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3202190',
                                         'accredited_it_employer': True,
                                         'trusted': True},
                            'snippet': {'requirement': 'От 2+ лет коммерческого опыта в релевантном стеке. '
                                                       'Опыт проектирования сервисов. '
                                                       'Опыт работы с асинхронным кодом. '
                                                       'Понимание алгоритмов и...',
                                        'responsibility': 'Проектирование и разработка новых фич и интеграций. '
                                                          'Небольшой процент поддержки и оптимизации кода. '
                                                          'Ревью кода других разработчиков команды. '},
                            'contacts': None,
                            'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
                            'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
                            'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
                            'accept_incomplete_resumes': False,
                            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
                            'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
                            'is_adv_vacancy': False,
                            'adv_context': None}]
