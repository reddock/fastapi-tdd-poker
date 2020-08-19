# project/tests/test_summaries.py


import json


def test_create_event(test_app_with_db):
    response = test_app_with_db.post("/events/", data=json.dumps(
        {
            "name": "Novemddb",
            "location": "Onlindde",
            "day_time": "2020-08-19 11:53:54.396682"
        }
    ))

    assert response.status_code == 201
    assert response.json()["name"] == "Novemddb"
    assert response.json()["location"] == "Onlindde"
    assert response.json()["day_time"] == "2020-08-19T11:53:54.396682"
