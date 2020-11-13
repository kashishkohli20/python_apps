import datetime

# function to print header
def print_header():
    print('---------------------------------')
    print('                birthday countdown app')
    print('---------------------------------')

# function to take user input of their birthday
def input_date():
    year = int(input('What year were you born in?[YYYY] '))
    month = int(input('What month were you born in?[MM] '))
    day = int(input('What day were you born on?[DD] '))

    return datetime.datetime(year, month, day)

# function to calculate the number of days
def calculate_days(b_date):
    now = datetime.datetime.now()
    print(now)
    date2 = datetime.datetime(now.year, b_date.month, b_date.day)
    dt = date2 - now
    days = int(dt.total_seconds() / 60 / 60 / 24)
    return days

# function to print birthday information
def print_birthday_info(days):
    if days < 0:
        print('Your birthday has passed this year {} days ago'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days'.format(days))
    else:
        print('Happy birthday!!!!')

# main function to initialise app
def main():
    print_header()
    b_date = input_date()
    print('It seems your birthday is on {}'.format(b_date))
    days = calculate_days(b_date)
    print_birthday_info(days)

main()