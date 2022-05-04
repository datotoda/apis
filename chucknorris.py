import json
import requests
import sys
import sqlite3

# https://api.chucknorris.io/
URL_BASE = 'https://api.chucknorris.io/jokes/'
DB = 'database.db'


def print_json(obj):
    print(json.dumps(obj, indent=4))


def get_categories():
    url = URL_BASE + 'categories'
    result = requests.get(url)

    return result, result.json()


def get_random():
    url = URL_BASE + 'random'
    result = requests.get(url)

    return result, result.json()


def get_random_by_category(category):
    url = URL_BASE + f'random?category={category}'
    result = requests.get(url)

    return result, result.json()


if __name__ == '__main__':
    argv = sys.argv

    # con ცვლადს ვანიჭებ ბაზის ფაილთან კავშირის ობიექტს
    con = sqlite3.connect(DB)
    # con ცვლადის row_factory-ად ვაყენებ sqlite3.Row
    con.row_factory = sqlite3.Row
    # cur ცვლადს ვანიჭებ კავშირის კურსორის ო
    cur = con.cursor()

    # ვქმნი jokes ცხრილს შესაბამისი სვეტებით
    cur.execute('''CREATE TABLE IF NOT EXISTS "jokes" ("joke_id" INTEGER, "created_at" TEXT, "icon_url" TEXT, 
    "id" TEXT, "updated_at" TEXT, "url" TEXT, "value" TEXT, PRIMARY KEY("joke_id" AUTOINCREMENT));''')

    response, joke = get_random()

    print(f'Response:\nstatus code: {response.status_code}\nheaders:')
    headers = dict(response.headers)
    print('Date:', headers['Date'])
    print('Content Type:', headers['Content-Type'])

    print('\nJoke:')
    print(joke['value'])

    if input('\nDo you want full json? (y / n)\n> ') in ['y', 'yes', 'save']:
        print_json(joke)

    if input('\nDo you want to save? (y / n)\n> ') in ['y', 'yes', 'save']:
        # თუ მომხმარებელი დაეთანხმება შენახვაზე, მაშინ ცხრილში შეინახება request-დან დაბრუნებული მონაცემები
        cur.execute('INSERT INTO jokes (created_at, icon_url, id, updated_at, url, value) VALUES(?, ?, ?, ?, ?, ?);',
                    tuple(joke[i] for i in ["created_at", "icon_url", "id", "updated_at", "url", "value"]))

    # ბაზაში შეტანილი ცვლილებები ინახება საბოლოოდ
    con.commit()
    # იხურება ბაზასთან კავშირი
    con.close()


# დავით ჩინჩალაძე
