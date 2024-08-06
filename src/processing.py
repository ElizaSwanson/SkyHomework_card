from typing import Any, List, Dict


def filter_by_state(
    state_dict: list[dict[str, str | Any]], state_status: str = "EXECUTED"
) -> list[dict[str, str | Any]]:
    filtered_dict = []
    for data in state_dict:
        if data.get("state") == state_status:
            filtered_dict.append(data)
    return filtered_dict


print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)


def sort_by_date(state_dict: list[dict[str, Any]], reversed_list: bool = True) -> list[dict[str, Any]]:
    """в этой функции происходит сортировка словарей по дате"""
    sorted_list = sorted(
        state_dict,
        key=lambda new_list: new_list["date"],
        reverse=reversed_list,
    )
    return sorted_list


print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
