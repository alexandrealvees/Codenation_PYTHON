from datetime import datetime, timedelta


records = [

    {'source': '48-996355555', 'destination': '48-666666666',

        'end': 1564610974, 'start': 1564610674},

    {'source': '41-885633788', 'destination': '41-886383097',

        'end': 1564506121, 'start': 1564504821},

    {'source': '48-996383697', 'destination': '41-886383097',

        'end': 1564630198, 'start': 1564629838},

    {'source': '48-999999999', 'destination': '41-885633788',

        'end': 1564697158, 'start': 1564696258},

    {'source': '41-833333333', 'destination': '41-885633788',

        'end': 1564707276, 'start': 1564704317},

    {'source': '41-886383097', 'destination': '48-996384099',

        'end': 1564505621, 'start': 1564504821},

    {'source': '48-999999999', 'destination': '48-996383697',

        'end': 1564505721, 'start': 1564504821},

    {'source': '41-885633788', 'destination': '48-996384099',

        'end': 1564505721, 'start': 1564504821},

    {'source': '48-996355555', 'destination': '48-996383697',

        'end': 1564505821, 'start': 1564504821},

    {'source': '48-999999999', 'destination': '41-886383097',

        'end': 1564610750, 'start': 1564610150},

    {'source': '48-996383697', 'destination': '41-885633788',

        'end': 1564505021, 'start': 1564504821},

    {'source': '48-996383697', 'destination': '41-885633788',

        'end': 1564627800, 'start': 1564626000}

]



def classify_by_phone_number(records: list) -> list:


    records_grouped = group_by_number(records)

    records_costs_computed = compute_records_costs(records_grouped)

    cost_by_record = calculate_cost_per_source(records_costs_computed)

    record_list = list_total_records(cost_by_record)


    return record_list



def group_by_number(records: list) -> dict:

    records_classified = {}


    for record in records:

        if record['source'] not in records_classified:

            records_classified.update(

                {

                    record['source']:

                    [{

                        'destination': record['destination'],

                        'start_time': datetime.fromtimestamp(record["start"]),

                        'end_time': datetime.fromtimestamp(record["end"]),

                        'duration': calculate_call_time(record),

                        'cost': 0.00}]

                })

        else:

            records_classified[record['source']].append(

                {'destination': record['destination'],

                 'duration': calculate_call_time(record),

                 'start_time': datetime.fromtimestamp(record["start"]),

                 'end_time': datetime.fromtimestamp(record["end"])})


    return records_classified



def calculate_call_time(record: dict) -> datetime:

    start_time = datetime.fromtimestamp(record['start'])

    end_time = datetime.fromtimestamp(record['end'])


    total_time = end_time - start_time


    return total_time



def calculate_call_price(call: dict) -> float:

    def is_daytime(time: datetime) -> bool:

        if (time.hour >= 6) and (time.hour < 22):

            return True

        else:

            return False


    # Taxes:

    CONNECTION_TAX = 0.36

    MINUTE_DAYTIME_TAX = 0.09

    MINUTE_NIGHTTIME_TAX = 0.00


    # Concepts:

    MINUTE_IN_SECONDS = 60


    duration: timedelta = call['duration']

    total_minute_cost = 0.00


    if duration.days > 1:

        return 0

    else:

        qty_minutes = duration.seconds // MINUTE_IN_SECONDS

        for minute in range(qty_minutes):

            time_period = call['start_time'] + timedelta(minutes=minute)

            if is_daytime(time_period):

                total_minute_cost += MINUTE_DAYTIME_TAX

            else:

                total_minute_cost += MINUTE_NIGHTTIME_TAX


        total_price = CONNECTION_TAX + total_minute_cost


    return total_price



def calculate_cost_per_source(call_list: dict) -> dict:

    call_results = {}

    for number, calls in call_list.items():

        total = 0.00

        for call in calls:

            total += calculate_call_price(call)

        call_results.update({number: round(total, 2)})


    return call_results



def list_total_records(calculated_records: dict) -> list:

    ordered_results = dict(sorted(calculated_records.items(),

                                  key=lambda value: value[1], reverse=True))


    total_records = []


    for number, cost in ordered_results.items():

        total_records.append({'source': number, 'total': cost})


    return total_records



def compute_records_costs(call_list: dict) -> dict:

    for calls in call_list.values():

        for call in calls:

            call['cost'] = calculate_call_price(call)


    return call_list