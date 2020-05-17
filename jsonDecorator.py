def to_json(funk):
    import json
    data = funk()
    json_string = json.dumps(data)

    def data():
        return json_string

    return data


@to_json
def get_data():
    return {

        'data': 42

    }


print(get_data())
