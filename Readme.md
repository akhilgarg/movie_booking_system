*How to start the app*

1. pip install -r requirements.txt
2. python manage.py loaddata fixtures.json
3. python manage.py runserver 0.0.0.0:8000


*Use the application in postman*

API-1

*API http://127.0.0.1:8000*

*API http://127.0.0.1:8000/shows*

Method: GET

Output:

[
    {
        "id": 1,
        "screen": {
            "id": 1,
            "theatre": {
                "id": 1,
                "name": "Theatre1",
                "created_at": "2022-08-16T12:54:50.265952Z"
            },
            "name": "SCREEN1",
            "created_at": "2022-08-16T12:54:53.133181Z"
        },
        "start": "2022-08-18T14:10:10Z",
        "end": "2022-08-18T16:10:28Z",
        "created_at": "2022-08-16T13:10:36.647764Z",
        "movie": 1
    },
    {
        "id": 2,
        "screen": {
            "id": 7,
            "theatre": {
                "id": 2,
                "name": "Theatre2",
                "created_at": "2022-08-16T12:55:35.183755Z"
            },
            "name": "SCREEN2",
            "created_at": "2022-08-16T12:55:44.086192Z"
        },
        "start": "2022-08-19T20:22:31Z",
        "end": "2022-08-19T22:22:35Z",
        "created_at": "2022-08-16T20:22:39.543856Z",
        "movie": 2
    },
    {
        "id": 3,
        "screen": {
            "id": 1,
            "theatre": {
                "id": 1,
                "name": "Theatre1",
                "created_at": "2022-08-16T12:54:50.265952Z"
            },
            "name": "SCREEN1",
            "created_at": "2022-08-16T12:54:53.133181Z"
        },
        "start": "2022-08-20T14:10:10Z",
        "end": "2022-08-20T16:10:28Z",
        "created_at": "2022-08-17T11:08:02.172662Z",
        "movie": 1
    },
    {
        "id": 4,
        "screen": {
            "id": 1,
            "theatre": {
                "id": 1,
                "name": "Theatre1",
                "created_at": "2022-08-16T12:54:50.265952Z"
            },
            "name": "SCREEN1",
            "created_at": "2022-08-16T12:54:53.133181Z"
        },
        "start": "2022-08-20T14:10:10Z",
        "end": "2022-08-20T16:10:28Z",
        "created_at": "2022-08-17T11:08:51.181231Z",
        "movie": 2
    },
    {
        "id": 6,
        "screen": {
            "id": 1,
            "theatre": {
                "id": 1,
                "name": "Theatre1",
                "created_at": "2022-08-16T12:54:50.265952Z"
            },
            "name": "SCREEN1",
            "created_at": "2022-08-16T12:54:53.133181Z"
        },
        "start": "2022-08-19T14:10:10Z",
        "end": "2022-08-19T16:10:28Z",
        "created_at": "2022-08-17T17:40:57.367734Z",
        "movie": 2
    },
    {
        "id": 7,
        "screen": {
            "id": 1,
            "theatre": {
                "id": 1,
                "name": "Theatre1",
                "created_at": "2022-08-16T12:54:50.265952Z"
            },
            "name": "SCREEN1",
            "created_at": "2022-08-16T12:54:53.133181Z"
        },
        "start": "2022-08-19T16:11:10Z",
        "end": "2022-08-19T17:10:28Z",
        "created_at": "2022-08-17T17:46:54.952885Z",
        "movie": 2
    }
]