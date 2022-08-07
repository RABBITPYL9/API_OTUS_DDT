from jsonschema import validate

import pytest
import requests

body = {
    'title': 'foo125364',
    'body': 'bar4445566',
    'userId': 1,
}
headers = {
    'Content-type': 'application/json; charset=UTF-8',
}


def test_new_post():
    res = requests.post('https://jsonplaceholder.typicode.com/posts', headers=headers, json=body)
    assert res.status_code == 201
    assert res.json()['body'] == body['body']
    assert res.json()['title'] == body['title']


@pytest.mark.parametrize('input_count, expected_count',
                         [(1, [1, 2, 3]),
                          (10, [91, 92, 93]),
                          (100, [])
                          ])
def test_filter_user(input_count, expected_count):
    res = requests.get('https://jsonplaceholder.typicode.com/posts?userId={}'.format(input_count))
    d = res.json()
    assert res.status_code == 200
    for i in range(len(expected_count)):
        assert expected_count[i] == d[i]['id']


def test_comments():
    res = requests.get('https://jsonplaceholder.typicode.com/posts/1/comments')
    assert res.status_code == 200


body1 = {
    'title': 'foo',
    'body': 'bar',
    'userId': 2,
}


def test_edit_post():
    res1 = requests.put('https://jsonplaceholder.typicode.com/posts/1', headers=headers, json=body)
    assert res1.status_code == 200


def test_edit_post_another_user():
    res = requests.put('https://jsonplaceholder.typicode.com/posts/1', headers=headers, json=body1)
    assert res.status_code == 200
