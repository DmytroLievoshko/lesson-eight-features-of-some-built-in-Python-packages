import argparse
from datetime import datetime

import creating_list_of_colleagues
from get_birthdays_per_week import get_birthdays_per_week


parser = argparse.ArgumentParser(description='Happy Birthday')
parser.add_argument('--new_list', '-new', default='0',
                    help='create a new list')

if __name__ == '__main__':

    args = parser.parse_args()
    make_new_list = int(args.new_list)

    if make_new_list:
        creating_list_of_colleagues.make_file_colleagues()

    list_of_colleagues = []
    with open('colleagues', 'r') as fh:
        lines = fh.readlines()
        for line in lines:
            line = line.strip()
            if line:
                name, birthday = line.split(' ')
                list_of_colleagues.append(
                    {name: datetime.strptime(birthday, '%Y-%m-%d')})

    get_birthdays_per_week(list_of_colleagues)
