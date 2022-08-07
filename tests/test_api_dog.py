from jsonschema import validate
import pytest
import requests


#SRC DATA BLOCK START
breeds_list = [
    
    'australian',
    'basenji',
    'dhole',
    'hound'

]

expected_sub_breeds_list = [
   
    ['shepherd'],
    [],
    [],
    ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker']

]

#SRC DATA BLOCK END

@pytest.mark.parametrize('input_count, expected_count',
                         [('1', 1),
                          ('10', 10),
                          ('30', 30),
                          ('50', 50),
                          ('100', 50)])
def test_check_count_photo_in_response(input_count, expected_count):
    
    res = requests.get('https://dog.ceo/api/breeds/image/random/{}'.format(input_count))
    assert res.status_code == 200
    assert len(res.json()['message']) == expected_count


@pytest.mark.parametrize('breeds, expected_sub_breeds', [

    (breeds_list[0], expected_sub_breeds_list[0]),
    (breeds_list[1], expected_sub_breeds_list[1]),
    (breeds_list[3], expected_sub_breeds_list[3])
    
    ]
    )
def test_sub_breeds(breeds, expected_sub_breeds):
    
    res = requests.get('https://dog.ceo/api/breed/{}/list'.format(breeds))
    assert res.status_code == 200
    assert expected_sub_breeds == res.json()['message']


def test_count_img():
    
    res = requests.get('https://dog.ceo/api/breed/hound/images')
    assert res.status_code == 200
    assert len(res.json()['message']) == 1000


def test_img_type():
    
    res = requests.get('https://dog.ceo/api/breed/hound/images')

    schema = {"type": "object",
              "properties": {
                  "message": {"type": "array"},
              }
              }

    validate(instance=res.json(), schema=schema)
