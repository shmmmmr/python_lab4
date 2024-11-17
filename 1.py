# TODO решите задачу
import json


def task() -> float:
    json_file_path = "D:\input.json"
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    total_sum = 0.0

    for item in data:
        score = item.get("score", 0.0)
        weight = item.get("weight", 0.0)

        total_sum += score * weight

    total_sum = round(total_sum, 3)

    return total_sum



print(task())