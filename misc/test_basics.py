"""Testing Basics 1/2

Test covers 1) output or 2) control flow

"""
import pytest
import requests


def compose_earnest_text():
    json_response = requests.get(f"https://randomuser.me/api/").json()  # IO
    (result,) = json_response["results"]
    if result.get("gender") != "female":
        return
    else:
        print("=== See Text Below ===")  # IO
        print(f'Hey {result["name"]["first"]}, will you date geeks?')  # IO


# output
def test_compose_earnest_text_return_none():
    assert compose_earnest_text() == None


# output + doesnt actually prove female only
def test_compose_earnest_text_female_only(mocker):
    mock_get = mocker.patch("requests.get", autospec=True)
    mock_get.return_value.json.return_value = {"results": [{"gender": "male"}]}
    assert compose_earnest_text() == None


# output + control flow
def test_compose_earnest_text_not_for_males(mocker):
    mock_print = mocker.patch("builtins.print")
    mock_get = mocker.patch("requests.get", autospec=True)
    mock_get.return_value.json.return_value = {"results": [{"gender": "male"}]}
    assert compose_earnest_text() == None
    mock_print.assert_not_called()


def test_compose_earnest_text_for_females_only(mocker):
    mock_print = mocker.patch("builtins.print")
    mock_get = mocker.patch("requests.get", autospec=True)
    mock_get.return_value.json.return_value = {
        "results": [{"gender": "female", "name": {"first": "Sara"}}]
    }
    assert compose_earnest_text() == None
    assert mock_print.call_args_list == [
        mocker.call("=== See Text Below ==="),
        mocker.call("Hey Sara, will you date geeks?"),
    ]


@pytest.fixture()
def mock_request_and_print(mocker):
    mock_print = mocker.patch("builtins.print")
    mock_get = mocker.patch("requests.get", autospec=True)
    return mock_print, mock_get


def test_compose_earnest_text_for_femaless_only(mocker, mock_request_and_print):
    mock_print, mock_get = mock_request_and_print
    mock_get.return_value.json.return_value = {
        "results": [{"gender": "female", "name": {"first": "FemaleName!"}}]
    }
    assert compose_earnest_text() == None
    assert mock_print.call_args_list == [
        mocker.call("=== See Text Below ==="),
        mocker.call("Hey FemaleName!, will you date geeks?"),
    ]


# control flow only for no male condition
def test_compose_earnest_text_not_for_maless(mock_request_and_print):
    mock_print, mock_get = mock_request_and_print
    mock_get.return_value.json.return_value = {"results": [{"gender": "male"}]}
    compose_earnest_text()  # remove redundant assertion for return
    mock_print.assert_not_called()
