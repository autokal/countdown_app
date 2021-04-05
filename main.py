# Project countdown app ,
# infos for module in google and python doc
import datetime as datetime_module

user_input = input('enter your goal with a deadline seperated by colon\n')

# learn english:12.08.2021
input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]
today_date = datetime_module.datetime.today()

# convert string in to date // 10.07.21 matches to '%d.%m.%y' -> look up in doc
deadline_date = datetime_module.datetime.strptime(deadline, '%d.%m.%Y')

# calculate how many days from now till deadline
time_till = deadline_date - today_date
hours_till = int(time_till.total_seconds() / 60 / 60)

print(f'Dear user! Time remaining for your goal:  {goal} is {time_till.days} days')
print(f'{time_till.days} are {hours_till} hours!!')


