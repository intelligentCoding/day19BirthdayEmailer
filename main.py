import smtplib
import datetime as dt

MY_PASSWORD = "pythonisbest"
MY_EMAIL = "tazwiztesting2@gmail.com"


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(MY_EMAIL, MY_PASSWORD)
    server.sendmail(MY_EMAIL, "kashif@mailinator.com", "Hellooo")
    server.close()

    print('Email sent!')
except:
    print('Something went wrong...')

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(MY_EMAIL, MY_PASSWORD)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs="kaaf_kaaf@hotmail.com",
#         msg=f"Subject:Monday Motivation\n\nhellooooo"
#     )


# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
#
# connection.sendmail(from_addr=my_email, to_addrs="kaaf_kaaf@hotmail.com", msg="Hello")
#
# connection.close()

