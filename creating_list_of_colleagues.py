import random
from datetime import datetime, timedelta

VOWEL_LIST = ['a', 'e', 'i', 'o', 'u', 'y']
CONSONANTS_LIST = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k',
                   'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
MINYEAR = 1950
MAXTIMEDELTADAY = 18300


def make_random_name():
    return random.choice(CONSONANTS_LIST).upper() + random.choice(VOWEL_LIST) + random.choice(CONSONANTS_LIST)


def make_random_birthday():
    first_date = datetime(year=MINYEAR, month=1, day=1)
    birthday = first_date + timedelta(random.randint(0, MAXTIMEDELTADAY))
    return birthday.strftime('%Y-%m-%d')


def make_file_colleagues(file_name: str = 'colleagues', quantity: int = 1000):

    with open(file_name, 'w') as fh:
        i = 1
        while i <= quantity:
            fh.write(make_random_name() + ' ' + make_random_birthday() + '\n')
            i += 1
