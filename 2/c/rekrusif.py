def parse_json_recursively(json_object, target_key):
    if type(json_object) is dict and json_object:
        for name in json_object:
            if name == target_key:
                print("{}: {}".format(target_key, json_object[name]))
            parse_json_recursively(json_object[name], target_key)

    elif type(json_object) is list and json_object:
        for item in json_object:
            parse_json_recursively(item, target_key)


json_object = [{
    "name": "Buku",
    "childs": [
        {
            "name": "Arsitektur Desain",
            "childs": [{
                "name": "buku bangunan",
                "childs": []
            }]
        },
        {
            "name": "kedokteran",
            "childs": [{
                "name": "buku farmasi",
                "childs": [{
                    "name": "category lain"
                }]

            }
            ]
        },
    ]
},
    {
    "name": "Category 2",
    "childs": [
        {
            "name": "Sub category",
            "childs": [{
                "name": "Sub category",
                "name": "Sub category",
            }]
        },
        {
            "name": "Sub category",
            "childs": [{
                "name": "Sub category",
                "name": "Sub category",
            }]
        }
    ]
}]
target_key = "name"
parse_json_recursively(json_object, target_key)
