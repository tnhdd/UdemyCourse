import random
import smtplib
import datetime as dt
import time

now = dt.datetime.now()
weekday = now.weekday()

my_email = "thebadbatet@gmail.com"
password = "sqatuywsksijcgbv"


# import datetime as dt
# now = dt.datetime.now()

def send_email():
    while True:
        # print("Sent an email")

        with open("quotes.txt") as quotes:
            lines = quotes.readlines()
            quote = random.choice(lines)
            print(quote)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="thebadbatet@yahoo.com",
                                msg=f"Subject: Monday Motivation\n\n {quote}")
        time.sleep(10)


send_email()
