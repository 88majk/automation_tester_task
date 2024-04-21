import pytest
import logging
import services.data_service as data_service
import services.xml_service as xml_service
from models.people import People


class TestDataServices:
    @pytest.fixture(autouse=True)
    def setup_logger(self, request):
        test_name = request.node.name
        self.logger = logging.getLogger(f"{__name__}.{test_name}")
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s] TEST LOG %(levelname)s - %(message)s')
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

    @pytest.fixture
    def get_people(self):
        root = xml_service.get_root('tests/test_data/test.xml')
        return People(root)

    # Test if the function filter_people() works correct for no given arguments in the function call.
    def test_filter_with_no_args(self, get_people):
        self.logger.info(f'''TEST NAME: test_filter_with_no_args
                                EXPECTING RESULTS: whole data from XML
                                TESTING FILE: test.xml''')
        people = data_service.filter_people(people=get_people.people_list)
        assert vars(people[0]) == {'name': 'John', 'surname': 'Doe', 'age': 30,
                                   'gender': 'Male', 'rank': 'Manager', 'salary': 50000.0} and \
               vars(people[1]) == {'name': 'Jane', 'surname': 'Smith', 'age': 25,
                                   'gender': 'Female', 'rank': 'Developer', 'salary': 60000.0}

    # Test if the function filter_people() works correct for valid and invalid value of rank attribute.
    @pytest.mark.parametrize("rank, expected_result", [
        ('Manager',
         {'name': 'John', 'surname': 'Doe', 'age': 30, 'gender': 'Male', 'rank': 'Manager', 'salary': 50000.0}),
        ('Developer',
         {'name': 'Jane', 'surname': 'Smith', 'age': 25, 'gender': 'Female', 'rank': 'Developer', 'salary': 60000.0}),
        ('AH13ad4', [])
    ])
    def test_filter_by_rank(self, rank, expected_result, get_people):
        self.logger.info(f'''TEST NAME: test_filter_by_rank
                        EXPECTING RESULTS: {expected_result}
                        TESTING FILE: test.xml''')
        filtered_people = data_service.filter_people(get_people.people_list, rank=rank)
        assert vars(filtered_people[0]) == expected_result if filtered_people \
            else filtered_people == expected_result, "Error"

    # Test if the function filter_people() works correct for valid and invalid value of gender attribute.
    @pytest.mark.parametrize("test_data", [
        ('Male',
         {'name': 'John', 'surname': 'Doe', 'age': 30, 'gender': 'Male', 'rank': 'Manager', 'salary': 50000.0}),
        ('Female',
         {'name': 'Jane', 'surname': 'Smith', 'age': 25, 'gender': 'Female', 'rank': 'Developer', 'salary': 60000.0}),
        ('A34AGd', [])
    ])
    def test_filter_by_gender(self, test_data, get_people):
        gender, expected_result = test_data
        self.logger.info(f'''TEST NAME: test_filter_by_gender
                        EXPECTING RESULTS: {expected_result}
                        TESTING FILE: test.xml''')
        filtered_people = data_service.filter_people(get_people.people_list, gender=gender)
        assert vars(filtered_people[0]) == expected_result if filtered_people \
            else filtered_people == expected_result, "Error"

    @pytest.mark.parametrize("test_data", [
        ((45000, 50000),
         {'name': 'John', 'surname': 'Doe', 'age': 30, 'gender': 'Male', 'rank': 'Manager', 'salary': 50000.0}),
        ((55000, 65000),
         {'name': 'Jane', 'surname': 'Smith', 'age': 25, 'gender': 'Female', 'rank': 'Developer', 'salary': 60000.0}),
        ((35000, 25), [])
    ])
    # Test if the function filter_people() works correct for valid and invalid range of salary value.
    def test_filter_by_salary_range(self, test_data, get_people):
        salary_range, expected_result = test_data
        self.logger.info(f'''TEST NAME: test_filter_by_salary_range
                        EXPECTING RESULTS: {expected_result}
                        TESTING FILE: test.xml''')
        filtered_people = data_service.filter_people(get_people.people_list,
                                                     salary_range=(salary_range[0], salary_range[1]))
        assert vars(filtered_people[0]) == expected_result if filtered_people \
            else filtered_people == expected_result, "Error"

    # Test if the function filter_people() works correct for valid and invalid range of age value.
    @pytest.mark.parametrize("test_data", [
        ((27, 32),
         {'name': 'John', 'surname': 'Doe', 'age': 30, 'gender': 'Male', 'rank': 'Manager', 'salary': 50000.0}),
        ((20, 25),
         {'name': 'Jane', 'surname': 'Smith', 'age': 25, 'gender': 'Female', 'rank': 'Developer', 'salary': 60000.0}),
        ((55, 25), [])
    ])
    def test_filter_by_age_range(self, test_data, get_people):
        age_range, expected_result = test_data
        self.logger.info(f'''TEST NAME: test_filter_by_age_range
                           EXPECTING RESULTS: {expected_result}
                           TESTING FILE: test.xml''')
        filtered_people = data_service.filter_people(get_people.people_list, age_range=(age_range[0], age_range[1]))
        assert vars(filtered_people[0]) == expected_result if filtered_people \
            else filtered_people == expected_result, "Error"
