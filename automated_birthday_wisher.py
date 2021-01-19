##################### Extra Hard Starting Project ######################

from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "tazwiztesting2@gmail.com"
MY_PASSWORD = "pythonisbest"
# check if today's date is one of birthday in the file
# get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Now we will read from birthday's file where all the birthdays are stored.
data = pandas.read_csv("birthdays.csv")

# create birthday dictionary comprehension

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# check if today is one of birthday
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    # pick a random letter
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    # replace [name] in the letter with person name.
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new_contents = contents.replace("[NAME]", birthday_person["name"])
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(MY_EMAIL, MY_PASSWORD)
        server.sendmail(MY_EMAIL, birthday_person["email"], f"Subject:Happy Birthday\n\n{new_contents}")
        server.close()
        print('Email sent!')
    except:
        print('Something went wrong...')
