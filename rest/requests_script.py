import requests


def generate_dict(id, color, body_type, year, country, name):
    return {
    'id': id, 
    'color': color, 
    'body_type': body_type, 
    'year': year, 
    'country': country,
    'name': name
}


requests.post('http://127.0.0.1:5000/cars', json=generate_dict(
    1, ['black'], body_type='five-door hatchback', year=2016, country='USA', name='Tesla Model S'
    ))
requests.post('http://127.0.0.1:5000/cars', json=generate_dict(
    2, ['green'], body_type='hatchback', year=2003, country='RUS', name='LADA ВАЗ(2109)'
))
requests.patch('http://127.0.0.1:5000/cars', json={
    'id': 2,
    'color': 'green'
})
requests.delete('http://127.0.0.1:5000/cars/1')
