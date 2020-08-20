from datetime import datetime
from datetime import datetime
from datetime import timedelta
import pandas as pd


records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def same_day(call):
    start_day = datetime.fromtimestamp(records[call]['start'])
    end_day = datetime.fromtimestamp(records[call]['end'])
    if start_day.day == end_day.day:
        return True
    else:
        return False


def calculate_call(line):
    minute = 60
    permanent_tariff = 0.36
    call_rate = 0.09
    hour_start_call = datetime.fromtimestamp(records[line]['start']).hour
    hour_end_call = datetime.fromtimestamp(records[line]['end']).hour
    call_time = int((records[line]['end'] - records[line]['start']) / minute)
    if (hour_start_call >= 6 and hour_end_call < 22):
        call_cost = (call_time * call_rate) + permanent_tariff
    else:
        call_cost = permanent_tariff
    return round(call_cost, 2)


def sum_result(dict):
    resposta = pd.DataFrame(dict)
    df = pd.DataFrame(resposta.groupby('source')['total'].sum().sort_values(ascending=False)).reset_index()
    new_result = []
    for item in range(len(df)):
        line_result = {}
        line_result['source'] = df.source[item]
        line_result['total'] = round(df.total[item], 2)
        new_result.append(line_result)
    return new_result


def classify_by_phone_number(records):
    result = []
    for call in range(len(records)):
        source = records[call]['source']
        if same_day(call):
            result_line = {}
            result_line['source'] = source
            result_line['total'] = calculate_call(call)
            result.append(result_line)
    return sum_result(result)



