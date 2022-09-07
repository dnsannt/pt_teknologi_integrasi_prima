import json

category = [{
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
            "childs": [
                {"name": "buku farmasi"}
            ]
        }
    ]
},
]

data = json.dumps(category, indent=4)
print(data)
