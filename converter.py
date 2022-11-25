import collections
import json
from typing import Any, Dict, Union
from argparse import ArgumentParser


def converter(data: Dict[Union[int, str], Any]) -> list:
    res_list = []
    q = collections.deque()
    q.append(data)
    while q:
        cur_elem = q.popleft()
        if isinstance(cur_elem, list):
            for elem in cur_elem:
                q.append(elem)
        elif isinstance(cur_elem, dict):
            for key, value in cur_elem.items():
                try:
                    q.index(key)
                except ValueError:
                    q.append(key)
                if value:
                    try:
                        q.index(value)
                    except ValueError:
                        q.append(value)
        else:
            res_list.append(cur_elem)
    return res_list


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

    result = converter(json_data)

    with open("result.txt", "w") as f:
        f.write(str(result))

    print(result)
    print("Done. See result.txt file")
