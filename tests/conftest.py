import json

import pytest

from src.head_hunter_api import HeadHunterAPI
from src.save_to_json import JSONSaver
from src.vacancies import Vacancy


@pytest.fixture
def hh_status():
    return HeadHunterAPI()


@pytest.fixture
def json_saver():
    return JSONSaver(filename='test_vacancies')


@pytest.fixture
def json_opener():
    with open(r'..\data\test_vacancies.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


@pytest.fixture
def vacancy_a():
    return Vacancy('Разработчик',
                   'http://hh.ru',
                   '100000 - 150000',
                   'RUR',
                   'Администрирование серверов Linux',
                   'Опыт работы с Linux в качестве администратора от 2 лет')


@pytest.fixture
def vacancy_b():
    return Vacancy('Разработчик',
                   'http://hh.ru',
                   '100000 - 150000',
                   'RUR',
                   'Администрирование серверов Linux',
                   'Опыт работы с Linux в качестве администратора от 2 лет')


@pytest.fixture
def vacancy_c():
    return Vacancy('Разработчик',
                   'http://hh.ru',
                   '100000 - 120000',
                   'RUR',
                   'Администрирование серверов Linux',
                   'Опыт работы с Linux в качестве администратора от 2 лет')


@pytest.fixture
def vacancy_d():
    return Vacancy('Разработчик',
                   'http://hh.ru',
                   '100000 - 200000',
                   'RUR',
                   'Администрирование серверов Linux',
                   'Опыт работы с Linux в качестве администратора от 2 лет')


@pytest.fixture
def vacancies():
    return [{'id': '106529103',
             'premium': False, 'name': 'Python – разработчик', 'department': None, 'has_test': True,
             'response_letter_required': False,
             'area': {'id': '1', 'name': 'Москва', 'url': 'https://api.hh.ru/areas/1'},
             'salary': {'from': None, 'to': 230000, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Москва', 'street': 'Рубцовская набережная', 'building': '3с1', 'lat': 55.776613,
                         'lng': 37.699975, 'description': None, 'raw': 'Москва, Рубцовская набережная, 3с1',
                         'metro': {'station_name': 'Бауманская', 'line_name': 'Арбатско-Покровская',
                                   'station_id': '3.17', 'line_id': '3', 'lat': 55.772405, 'lng': 37.67904},
                         'metro_stations': [{'station_name': 'Бауманская', 'line_name': 'Арбатско-Покровская',
                                             'station_id': '3.17', 'line_id': '3', 'lat': 55.772405, 'lng': 37.67904}],
                         'id': '1885643'}, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2024-08-29T18:31:09+0300', 'created_at': '2024-08-29T18:31:09+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106529103',
             'show_logo_in_search': None,
             'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/106529103?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/106529103', 'relations': [],
             'employer': {'id': '3202190', 'name': 'KTS', 'url': 'https://api.hh.ru/employers/3202190',
                          'logo_urls': {'90': 'https://img.hhcdn.ru/employer-logo/5626348.png',
                                        '240': 'https://img.hhcdn.ru/employer-logo/5626349.png',
                                        'original': 'https://img.hhcdn.ru/employer-logo-original/1001392.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=3202190',
                          'accredited_it_employer': True,
                          'trusted': True},
             'snippet': {'requirement': 'От 2+ лет коммерческого опыта в релевантном стеке. '
                                        'Опыт проектирования сервисов. Опыт работы с асинхронным кодом. '
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


@pytest.fixture
def vacancies_data():
    return [{'id': '106501725', 'premium': False, 'name': 'Аналитик', 'department': None, 'has_test': False,
             'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва',
                                                         'url': 'https://api.hh.ru/areas/1'},
             'salary': {'from': 90000, 'to': None, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Москва', 'street': 'Переведеновский переулок', 'building': '13с4',
                         'lat': 55.780289, 'lng': 37.690354, 'description': None,
                         'raw': 'Москва, Переведеновский переулок, 13с4',
                         'metro': {'station_name': 'Бауманская', 'line_name': 'Арбатско-Покровская',
                                   'station_id': '3.17', 'line_id': '3', 'lat': 55.772405, 'lng': 37.67904},
                         'metro_stations': [{'station_name': 'Бауманская', 'line_name': 'Арбатско-Покровская',
                                             'station_id': '3.17', 'line_id': '3', 'lat': 55.772405, 'lng': 37.67904},
                                            {'station_name': 'Электрозаводская', 'line_name': 'Арбатско-Покровская',
                                             'station_id': '3.161', 'line_id': '3', 'lat': 55.782057, 'lng': 37.7053}],
                         'id': '1451179'},
             'response_url': None, 'sort_point_distance': None, 'published_at': '2024-08-29T12:26:17+0300',
             'created_at': '2024-08-29T12:26:17+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106501725',
             'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True,
             'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/106501725?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/106501725', 'relations': [],
             'employer': {'id': '27735', 'name': 'EcoStandard group',
                          'url': 'https://api.hh.ru/employers/27735',
                          'alternate_url': 'https://hh.ru/employer/27735',
                          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/787783.png',
                                        '240': 'https://img.hhcdn.ru/employer-logo/3592024.png',
                                        '90': 'https://img.hhcdn.ru/employer-logo/3592023.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=27735',
                          'accredited_it_employer': False, 'trusted': True},
             'snippet': {'requirement': 'Высшее техническое образование будет преимуществом. '
                                        'Высокий уровень владения Power BI, Excel. Знание DAX. '
                                        'Приветствуется знание SQL и <highlighttext>Python</highlighttext>. ',
                         'responsibility': 'Разработка, внедрение, поддержка отчетов на платформе Power BI. '
                                           'Сбор исходных данных. Взаимодействие с внутренним заказчиком. '
                                           'Уточнение требований к отчету. '},
             'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'},
             'working_days': [], 'working_time_intervals': [], 'working_time_modes': [],
             'accept_temporary': False, 'professional_roles': [{'id': '10', 'name': 'Аналитик'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None},
            {'id': '106437323', 'premium': False, 'name': 'ГИС-специалист', 'department': None, 'has_test': False,
             'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва',
                                                         'url': 'https://api.hh.ru/areas/1'},
             'salary': {'from': None, 'to': 90000, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Москва', 'street': '3-я Рыбинская улица', 'building': '18с2',
                         'lat': 55.790514, 'lng': 37.660161, 'description': None,
                         'raw': 'Москва, 3-я Рыбинская улица, 18с2', 'metro': None, 'metro_stations': [],
                         'id': '13633656'}, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2024-08-28T11:29:57+0300', 'created_at': '2024-08-28T11:29:57+0300',
             'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106437323',
             'show_logo_in_search': None, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/106437323?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/106437323',
             'relations': [], 'employer': {'id': '4021702', 'name': 'Градостроительный Институт МИРПРОЕКТ',
                                           'url': 'https://api.hh.ru/employers/4021702',
                                           'alternate_url': 'https://hh.ru/employer/4021702',
                                           'logo_urls': {
                                               'original': 'https://img.hhcdn.ru/employer-logo-original/1001538.jpeg',
                                               '90': 'https://img.hhcdn.ru/employer-logo/5626932.jpeg',
                                               '240': 'https://img.hhcdn.ru/employer-logo/5626933.jpeg'},
                                           'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4021702',
                                           'accredited_it_employer': False, 'trusted': True},
             'snippet': {'requirement': 'Навыки работы в ПО: MapInfo, Панорамма, Adobe Photoshop, Illustrator, '
                                        'SketchUp, Blender, Revit. Понимание: PostgreSQL, '
                                        '<highlighttext>Python</highlighttext>, др. языки программирования.',
                         'responsibility': 'Сбор и анализ исходных картографических, градостроительных, '
                                           'аналитических данных. Перепроецирование данных в различные '
                                           'системы координат (WGS84, ГСК, МСК). '},
             'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'},
             'working_days': [], 'working_time_intervals': [], 'working_time_modes': [],
             'accept_temporary': False, 'professional_roles': [{'id': '27', 'name': 'Геодезист'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None},
            {'id': '106497337', 'premium': False, 'name': 'Аналитик второй линии поддержки', 'department': None,
             'has_test': True, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва',
                                                                           'url': 'https://api.hh.ru/areas/1'},
             'salary': {'from': 100000, 'to': None, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': None, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2024-08-29T11:34:46+0300', 'created_at': '2024-08-29T11:34:46+0300',
             'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106497337',
             'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True,
             'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/106497337?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/106497337', 'relations': [],
             'employer': {'id': '17713', 'name': 'ЮТэйр, Авиакомпания', 'url': 'https://api.hh.ru/employers/17713',
                          'alternate_url': 'https://hh.ru/employer/17713',
                          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/939772.png',
                                        '240': 'https://img.hhcdn.ru/employer-logo/4199633.png', '90':
                                            'https://img.hhcdn.ru/employer-logo/4199632.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=17713',
                          'accredited_it_employer': True, 'trusted': True},
             'snippet': {'requirement': 'Знание основ web-технологий и навыки программирования, желательно на '
                                        '<highlighttext>Python</highlighttext>. Опыт работы с DBeaver. Опыт работы с '
                                        'Postman. ',
                         'responsibility': 'Вести деловую переписку и писать техническую документацию. Составлять '
                                           'запросы к MongoDB или SQL.'},
             'contacts': None, 'schedule': {'id': 'remote', 'name': 'Удаленная работа'},
             'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '121', 'name': 'Специалист технической поддержки'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None},
            {'id': '106047009', 'premium': False, 'name': 'Тестировщик', 'department': None, 'has_test': False,
             'response_letter_required': False, 'area': {'id': '79', 'name': 'Саратов',
                                                         'url': 'https://api.hh.ru/areas/79'},
             'salary': {'from': 80000, 'to': None, 'currency': 'RUR', 'gross': True},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Саратов', 'street': 'Бахметьевская улица', 'building': '34/42',
                         'lat': 51.525864, 'lng': 46.015652, 'description': None, 'raw': 'Саратов, '
                                                                                         'Бахметьевская улица, 34/42',
                         'metro': None, 'metro_stations': [], 'id': '604432'},
             'response_url': None, 'sort_point_distance': None, 'published_at': '2024-08-20T11:18:49+0300',
             'created_at': '2024-08-20T11:18:49+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106047009',
             'show_logo_in_search': None, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/106047009?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/106047009', 'relations': [],
             'employer': {'id': '2138838', 'name': 'ЮКЕЙСОФТ', 'url': 'https://api.hh.ru/employers/2138838',
                          'alternate_url': 'https://hh.ru/employer/2138838',
                          'logo_urls': {'240': 'https://img.hhcdn.ru/employer-logo/2379621.png',
                                        '90': 'https://img.hhcdn.ru/employer-logo/2379620.png',
                                        'original': 'https://img.hhcdn.ru/employer-logo-original/484442.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=2138838',
                          'accredited_it_employer': False, 'trusted': True},
             'snippet': {'requirement': 'Работа с баг-трекинговыми системами. Знание JavaScript или '
                                        '<highlighttext>Python</highlighttext> для написания авто-тестов в '
                                        'Selenium. Будет плюсом: Опыт работы с...',
                         'responsibility': 'Проведение функционального, интеграционного, системного тестирования, '
                                           'проверка бизнес-процесса, тестирование удобства пользования. '
                                           'Взаимодействие с командами разработчиков.'}, 'contacts': None,
             'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '124', 'name': 'Тестировщик'}], 'accept_incomplete_resumes': False,
             'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None},
            {'id': '106501725', 'premium': False, 'name': 'Аналитик', 'department': None, 'has_test': False,
             'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва',
                                                         'url': 'https://api.hh.ru/areas/1'},
             'salary': {'from': 90000, 'to': 100000, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': {'city': 'Москва', 'street': 'Переведеновский переулок', 'building': '13с4',
                         'lat': 55.780289, 'lng': 37.690354, 'description': None,
                         'raw': 'Москва, Переведеновский переулок, 13с4',
                         'metro': {'station_name': 'Бауманская', 'line_name': 'Арбатско-Покровская',
                                   'station_id': '3.17', 'line_id': '3', 'lat': 55.772405, 'lng': 37.67904},
                         'metro_stations': [{'station_name': 'Бауманская', 'line_name': 'Арбатско-Покровская',
                                             'station_id': '3.17', 'line_id': '3', 'lat': 55.772405, 'lng': 37.67904},
                                            {'station_name': 'Электрозаводская', 'line_name': 'Арбатско-Покровская',
                                             'station_id': '3.161', 'line_id': '3', 'lat': 55.782057, 'lng': 37.7053}],
                         'id': '1451179'}, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2024-08-29T12:26:17+0300', 'created_at': '2024-08-29T12:26:17+0300',
             'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106501725',
             'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/106501725?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/106501725', 'relations': [],
             'employer': {'id': '27735', 'name': 'EcoStandard group',
                          'url': 'https://api.hh.ru/employers/27735',
                          'alternate_url': 'https://hh.ru/employer/27735',
                          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/787783.png',
                                        '240': 'https://img.hhcdn.ru/employer-logo/3592024.png',
                                        '90': 'https://img.hhcdn.ru/employer-logo/3592023.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=27735',
                          'accredited_it_employer': False, 'trusted': True},
             'snippet': {'requirement': 'Высшее техническое образование будет преимуществом. '
                                        'Высокий уровень владения Power BI, Excel. Знание DAX. '
                                        'Приветствуется знание SQL и <highlighttext>Python</highlighttext>. ',
                         'responsibility': 'Разработка, внедрение, поддержка отчетов на платформе Power BI. '
                                           'Сбор исходных данных. Взаимодействие с внутренним заказчиком. '
                                           'Уточнение требований к отчету. '}, 'contacts': None,
             'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '10', 'name': 'Аналитик'}], 'accept_incomplete_resumes': False,
             'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None},
            {'id': '106437323', 'premium': False, 'name': 'ГИС-специалист', 'department': None, 'has_test': False,
             'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва',
                                                         'url': 'https://api.hh.ru/areas/1'},
             'salary': {'from': None, 'to': 50000, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'}, 'address': {'city': 'Москва', 'street': '3-я Рыбинская улица',
                                                                     'building': '18с2', 'lat': 55.790514,
                                                                     'lng': 37.660161, 'description': None,
                                                                     'raw': 'Москва, 3-я Рыбинская улица, 18с2',
                                                                     'metro': None, 'metro_stations': [],
                                                                     'id': '13633656'}, 'response_url': None,
             'sort_point_distance': None, 'published_at': '2024-08-28T11:29:57+0300',
             'created_at': '2024-08-28T11:29:57+0300', 'archived': False,
             'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106437323',
             'show_logo_in_search': None, 'insider_interview': None,
             'url': 'https://api.hh.ru/vacancies/106437323?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/106437323', 'relations': [],
             'employer': {'id': '4021702', 'name': 'Градостроительный Институт МИРПРОЕКТ',
                          'url': 'https://api.hh.ru/employers/4021702',
                          'alternate_url': 'https://hh.ru/employer/4021702',
                          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/1001538.jpeg',
                                        '90': 'https://img.hhcdn.ru/employer-logo/5626932.jpeg',
                                        '240': 'https://img.hhcdn.ru/employer-logo/5626933.jpeg'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=4021702',
                          'accredited_it_employer': False, 'trusted': True},
             'snippet': {'requirement': 'Навыки работы в ПО: MapInfo, Панорамма, Adobe Photoshop, Illustrator, '
                                        'SketchUp, Blender, Revit. Понимание: PostgreSQL, '
                                        '<highlighttext>Python</highlighttext>, др. языки программирования.',
                         'responsibility': 'Сбор и анализ исходных картографических, градостроительных, '
                                           'аналитических данных. Перепроецирование данных в различные системы '
                                           'координат (WGS84, ГСК, МСК). '},
             'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'},
             'working_days': [], 'working_time_intervals': [], 'working_time_modes': [],
             'accept_temporary': False, 'professional_roles': [{'id': '27', 'name': 'Геодезист'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None},
            {'id': '106497337', 'premium': False, 'name': 'Аналитик второй линии поддержки', 'department': None,
             'has_test': True, 'response_letter_required': False, 'area': {'id': '1', 'name': 'Москва',
                                                                           'url': 'https://api.hh.ru/areas/1'},
             'salary': {'from': 1000000, 'to': None, 'currency': 'RUR', 'gross': False},
             'type': {'id': 'open', 'name': 'Открытая'},
             'address': None, 'response_url': None, 'sort_point_distance': None,
             'published_at': '2024-08-29T11:34:46+0300', 'created_at': '2024-08-29T11:34:46+0300',
             'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=106497337',
             'branding': {'type': 'MAKEUP', 'tariff': None}, 'show_logo_in_search': True,
             'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/106497337?host=hh.ru',
             'alternate_url': 'https://hh.ru/vacancy/106497337', 'relations': [],
             'employer': {'id': '17713', 'name': 'ЮТэйр, Авиакомпания',
                          'url': 'https://api.hh.ru/employers/17713',
                          'alternate_url': 'https://hh.ru/employer/17713',
                          'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/939772.png',
                                        '240': 'https://img.hhcdn.ru/employer-logo/4199633.png',
                                        '90': 'https://img.hhcdn.ru/employer-logo/4199632.png'},
                          'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=17713',
                          'accredited_it_employer': True, 'trusted': True},
             'snippet': {'requirement': 'Знание основ web-технологий и навыки программирования, '
                                        'желательно на <highlighttext>Python</highlighttext>. '
                                        'Опыт работы с DBeaver. Опыт работы с Postman. ',
                         'responsibility': 'Вести деловую переписку и писать техническую документацию. '
                                           'Составлять запросы к MongoDB или SQL.'}, 'contacts': None,
             'schedule': {'id': 'remote', 'name': 'Удаленная работа'}, 'working_days': [],
             'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
             'professional_roles': [{'id': '121', 'name': 'Специалист технической поддержки'}],
             'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
             'employment': {'id': 'full', 'name': 'Полная занятость'}, 'adv_response_url': None,
             'is_adv_vacancy': False, 'adv_context': None}]


@pytest.fixture
def vacancies_dict():
    return {
        'name': 'Разработчик',
        'url': 'http://hh.ru',
        'salary': '100000 - 150000',
        'currency': 'RUR',
        'resposibility': 'Администрирование серверов Linux',
        'requirements': 'Опыт работы с Linux в качестве администратора от 2 лет'
    }


@pytest.fixture
def json_file():
    data = [{
        'name': 'Разработчик',
        'url': 'http://hh.ru',
        'salary': '100000 - 150000',
        'currency': 'RUR',
        'resposibility': 'Администрирование серверов Linux',
        'requirements': 'Опыт работы с Linux в качестве администратора от 2 лет'
    }]
    file = json.dumps(data)
    return file
