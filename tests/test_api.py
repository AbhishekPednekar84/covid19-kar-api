import os
import json


def test_if_file_created():
    files = os.listdir()
    assert "gender.json" in files
    assert os.path.isfile(os.path.join(os.getcwd(), "gender.json")) is True


def test_file_contents():
    with open("gender.json") as f:
        gender_json = json.load(f)
        gender_list = []
        for item in gender_json:
            gender_list.append(item["gender"])
        assert "Female" in gender_list
        assert "Male" in gender_list
