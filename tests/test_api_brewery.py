from jsonschema import validate
import pytest
import requests


@pytest.mark.parametrize('input_count, expected_count',
                         [
('san_diego', 'san diego'),
('fayetteville', 'fayetteville'),
('windsor', 'windsor')
                          ])
def test__check_filter(input_count, expected_count):
    
    res = requests.get('https://api.openbrewerydb.org/breweries?by_city={}'.format(input_count))
    res_to_json = res.json()
    assert res.status_code == 200
    for i in range(len(res_to_json)):
        assert expected_count in res_to_json[i]['city']#.lower()


@pytest.mark.parametrize('input_count, expected_count',
                         [('micro', 'micro'),
                          ('large', 'large'),
                          ('closed', 'closed')
                          ])
def test__check_filter_type(input_count, expected_count):
    
    res = requests.get('https://api.openbrewerydb.org/breweries?by_city={}'.format(input_count))
    res_to_json = res.json()
    assert res.status_code == 200
    for i in range(len(res_to_json)):
        assert expected_count in res_to_json[i]['brewery_type']


@pytest.mark.parametrize('input_count, expected_count',
                         [('West_virginia', 'West Virginia'),
                          ('California', 'California'),
                          ('Florida', 'Florida')
                          ])
def test__check_filter_state(input_count, expected_count):
    res = requests.get('https://api.openbrewerydb.org/breweries?by_state={}'.format(input_count))
    res_to_json = res.json()
    assert res.status_code == 200
    for i in range(len(res_to_json)):
        assert expected_count in res_to_json[i]['state']


@pytest.mark.parametrize('input_count, expected_count',
                         [('dog', 'dog'),
                          ('cat', 'cat'),
                          ('closed', 'closed')
                          ])
def test__check_filter(input_count, expected_count):
    res = requests.get('https://api.openbrewerydb.org/breweries/autocomplete?query={}'.format(input_count))
    res_to_json = res.json()
    assert res.status_code == 200
    for i in range(len(res_to_json)):
        assert expected_count in res_to_json[i]['name'].lower()
