import json
import requests
import sys

# https://github.com/fawazahmed0/currency-api
URL_BASE = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/'


def print_json(obj):
    print(json.dumps(obj, indent=4))


def get_date_or_latest_param(year=None, month=None, day=None):
    result = 'latest'

    if day or month or year:
        result = f'{year if year else "2021"}-{month if month else "01"}-{day if day else "01"}'

    return result


def get_currencies(time_=get_date_or_latest_param()):
    url = URL_BASE + f'{time_}/currencies.json'
    result = requests.get(url).json()

    with open('currencies/currencies.json', 'w') as f:
        json.dump(result, f, indent=4)

    return result


def get_from_currencies(from_, time_=get_date_or_latest_param()):
    url = URL_BASE + f'{time_}/currencies/{from_}.json'
    result = requests.get(url).json()

    with open(f'currencies/{from_}.json', 'w') as f:
        json.dump(result, f, indent=4)

    return result


def get_from_to_currencies(from_, to_, time_=get_date_or_latest_param()):
    url = URL_BASE + f'{time_}/currencies/{from_}/{to_}.json'
    result = requests.get(url).json()

    with open(f'currencies/{from_}_{to_}.json', 'w') as f:
        json.dump(result, f, indent=4)

    return result


def convert(amount, from_, to_, time_=get_date_or_latest_param()):
    try:
        amount = float(amount)
    except ValueError:
        return 0
    return round(amount * get_from_to_currencies(from_, to_, time_)[to_], 2)


if __name__ == '__main__':
    argv = sys.argv

    if len(argv) == 3:
        print_json(get_from_to_currencies(argv[1], argv[2]))
    elif len(argv) == 4:
        print(convert(argv[1], argv[2], argv[3]), argv[3])
    elif len(argv) == 1:
        while True:
            inp = input('\nchoice time:\n(1) - specific date\n(2) - latest\n> ')
            inp_time = None

            if inp in ['1']:
                inp_time = input('\ninput date (year-month-day):\n> ')
                inp_time = inp_time.split('-')
                inp_time = get_date_or_latest_param(inp_time[0], inp_time[1], inp_time[2])
                break

            if inp in ['2']:
                inp_time = get_date_or_latest_param()
                break

        while True:
            inp = input('\n(1) - all currencies\n(2) - one valute\n(3) - get currency\n(4) - convert\n> ')

            if inp in ['1']:
                print_json(get_currencies(inp_time))
                break
            if inp in ['2']:
                print_json(get_from_currencies(input('\ninput valute:\n> '), inp_time))
                break
            if inp in ['3']:
                print_json(get_from_to_currencies(input('\nfrom:\n> '), input('\nto:\n> '), inp_time))
                break
            if inp in ['4']:
                print_json(convert(input('\namount:\n> '), input('\nfrom:\n> '), input('\nto:\n> '), inp_time))
                break


# დავით ჩინჩალაძე
