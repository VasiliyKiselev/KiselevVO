import json
def task() -> float:
    summ = 0
    with open('input.json', 'r') as file:
        data = json.load(file)
        for values in data:
            summ += values['score'] * values['weight']
    return round(summ, 3)
print(task())
