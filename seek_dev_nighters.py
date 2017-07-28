import requests
import pytz
import datetime


def load_attempts():
    attempts = []
    for page_index in range(1, 11):
        url = 'https://devman.org/api/challenges/solution_attempts/'
        params = {"page":str(page_index)}
        try:
            json_data = requests.get(url, params=params).json()
        except requests.exceptions.ConnectionError as error:
            print(error)
        else:
            for attempt in json_data["records"]:
                if attempt['timestamp'] is not None:
                    attempts.append(attempt)
    return attempts


def get_midnighters(attempts):
    for attempt in attempts:
        unix_timestamp = attempt["timestamp"]
        local_timezone = pytz.timezone(attempt["timezone"])
        local_time = datetime.datetime.fromtimestamp(unix_timestamp, local_timezone)
        if local_time.hour < 8:
            print("%s сдал работу в %s" % (attempt["username"], local_time.__format__("%H:%M")))


def main():
    print('Ищем сов...')
    get_midnighters(load_attempts())


if __name__ == '__main__':
    main()
