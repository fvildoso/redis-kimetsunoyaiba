import json

import redis

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # hacemos la conexion a redis
    r = redis.Redis(host='localhost', port=6379, db=0)

    # agregamos una variable foo con valor bar
    r.set('foo', 'bar')

    # leemos la variable foo y la dejamos en la variable test de python
    test = r.get('foo')
    print(test)

    # hacemos un diccionario
    some_dict = {'nombre': 'Nezuko', 'edad': 32}

    # pasamos el diccionario a json
    json_object = json.dumps(some_dict, indent=4)

    # guardamos el diccionario
    r.set('json_object', json_object)

    # leemos el json y lo pasamos a diccionario
    get_json = json.loads(r.get('json_object'))

    # printiamos la edad
    print(get_json['edad'])
