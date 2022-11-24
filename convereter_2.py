import json
from argparse import ArgumentParser

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

    with open(args.filename, "r") as f:
        json_data = json.loads(f.read())

    args = parser.parse_args()

    result_data = (
        str(json_data)
        .replace("{", "")
        .replace("}", "")
        .replace("[", "")
        .replace("]", "")
        .replace(": ", ",")
        .replace(", ", ",")
        .replace("'", "")
    )
    result_data = list(set(result_data.split(",")))[1:]
    with open("result.txt", "w") as f:
        f.write(str(result_data))

    print(result_data)
    print("Done. See result.txt file")
