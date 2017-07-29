import requests
import pytz
import datetime


def load_attempts():
    page_number = 1
    number_of_pages = 1
    attempts = []
    while page_number <= number_of_pages:
        url = 'https://devman.org/api/challenges/solution_attempts/'
        params = {"page":page_number}
        try:
            json_data = requests.get(url, params=params).json()
        except requests.exceptions.ConnectionError as error:
            print(error)
        else:
            number_of_pages = int(json_data["number_of_pages"])
            for attempt in json_data["records"]:
                if attempt['timestamp'] is not None:
                    attempts.append(attempt)
        page_number += 1
    return attempts


def get_midnighters(attempts):
    midnighters = set()
    for attempt in attempts:
        unix_timestamp = attempt["timestamp"]
        local_timezone = pytz.timezone(attempt["timezone"])
        local_time = datetime.datetime.fromtimestamp(unix_timestamp, local_timezone)
        morning_hour = 8
        if local_time.hour < morning_hour:
            midnighters.add(attempt["username"])
    return midnighters


def main():
    print('Ищем сов...')
    midnighters = get_midnighters(load_attempts())
    print('Вот они, наши совы:')
    for owl in midnighters:
        print(owl)


if __name__ == '__main__':
    main()
