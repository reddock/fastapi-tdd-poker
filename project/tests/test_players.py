# project/tests/test_summaries.py


import json


def test_create_player(test_app_with_db):
    response = test_app_with_db.post("/players/", data=json.dumps({"name": "Hannibal"}))

    assert response.status_code == 201
    assert response.json()["name"] == "Hannibal"


def test_create_player_invalid_json(test_app):
    response = test_app.post("/players/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": ["body", "payload", "name"],
                "msg": "field required",
                "type": "value_error.missing",
            }
        ]
    }


def test_read_player(test_app_with_db):
    response = test_app_with_db.post(
        "/players/", data=json.dumps({"name": "Alexandro"})
    )
    player_id = response.json()["id"]

    response = test_app_with_db.get(f"/players/{player_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == player_id
    assert response_dict["name"] == "Alexandro"
    assert response_dict["created_at"]


def test_read_summary_incorrect_id(test_app_with_db):
    response = test_app_with_db.get("/players/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Player not found"


def test_read_all_players(test_app_with_db):
    response = test_app_with_db.post(
        "/players/", data=json.dumps({"name": "Alexandro"})
    )
    player_id = response.json()["id"]

    response = test_app_with_db.get("/players/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == player_id, response_list))) == 1
