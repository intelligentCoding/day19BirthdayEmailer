import smtplib
import datetime as dt
import random

MY_EMAIL = "tazwiztesting2@gmail.com"
MY_PASSWORD = "pythonisbest"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(MY_EMAIL, MY_PASSWORD)
        server.sendmail(MY_EMAIL, MY_EMAIL, f"Subject:Monday Motivation\n\n{quote}")
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')
