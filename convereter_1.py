import json
from typing import Any, Dict, Union
from argparse import ArgumentParser


def converter(cur_element: [int, list, dict], result: dict) -> dict:
    if isinstance(cur_element, list):
        for elem in cur_element:
            converter(elem, result)
    elif isinstance(cur_element, dict):
        for key, value in cur_element.items():
            if key not in result:
                result[key] = ""
            if value:
                converter(value, result)
    else:
        if cur_element not in result:
            result[cur_element] = cur_element
    return result


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        dest="filename",
        help="Преобразовать json файл в список",
        metavar="FILE",
        required=True,
    )

    args = parser.parse_args()

    result_dict = dict()

    with open(args.filename, "r") as f:
        json_data = json.loads(f.read())

    result = list(converter(json_data, result_dict).keys())

    with open("result.txt", "w") as f:
        f.write(str(result))

    print(result)
    print("Done. See result.txt file")
