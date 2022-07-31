from datetime import datetime, timedelta
from typing import List

DAY_OF_WEEK = {0: 'monday', 1: 'tuesday', 2: 'wednesday',
               3: 'thursday', 4: 'friday', 5: 'saturday', 6: 'sunday'}


def get_birthdays_per_week(list_of_colleagues: List[dict]):
    naw = datetime.now().date()
    check_date = naw + timedelta(days=7 - naw.weekday())
    weekday = 0

    congratulations_on_monday = []
    while weekday < 7:
        list_of_birthday = []
        for colleague in list_of_colleagues:
            for name, birthday in colleague.items():
                if birthday.day == check_date.day and birthday.month == check_date.month:
                    list_of_birthday.append(name)

        if weekday < 5:
            print(f"{DAY_OF_WEEK[weekday]}: {', '.join(list_of_birthday)}")
        else:
            congratulations_on_monday.extend(list_of_birthday)

        weekday += 1
        check_date = check_date + timedelta(days=1)

    if len(congratulations_on_monday) > 0:
        print(f"{DAY_OF_WEEK[0]}: {', '.join(congratulations_on_monday)}")
