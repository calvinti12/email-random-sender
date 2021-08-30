import os
import config
import random
import time
import datetime
from pytz import timezone
from log import Log
from spreadsheet_manager.google_ss import google_shets
from email_manager.sender import Email_manager

def main (): 

    # Logs instance
    logs = Log (os.path.join (os.path.basename(__file__)))

    # Calculate times
    tz = timezone('US/Eastern')

    start_hour = int(config.get_credential("start_hour"))
    end_hour = int(config.get_credential("end_hour"))
    random_hour = random.randrange(start_hour, end_hour + 1)
    random_minute = random.randrange(1, 3)

    # Get current times
    current_datetime = datetime.datetime.now(tz)
    current_time_delta = datetime.timedelta(hours=current_datetime.hour, 
                                      minutes=current_datetime.minute)
    current_datetime_tz = datetime.datetime.now()
    current_time_delta_tz = datetime.timedelta(hours=current_datetime.hour, 
                                      minutes=current_datetime.minute)

    # Calculate time diference
    time_diff = current_datetime.hour - current_datetime_tz.hour

    # Set send times
    send_time = datetime.datetime(year=current_datetime.year, 
                                  month=current_datetime.month,
                                  day=current_datetime.day,
                                  hour=random_hour + time_diff, 
                                  minute=random_minute, 
                                  tzinfo=tz)
    send_time_delta = datetime.timedelta(hours=send_time.hour, 
                                      minutes=send_time.minute)
    
    # Wait and debugs
    wait_time = (send_time_delta - current_time_delta).seconds

    logs.info(f"Currenttime: {current_time_delta}")
    logs.info(f"Send time: {send_time_delta}")
    logs.info(f"Wait time: {wait_time}")
    logs.info(f"Waiting for time {send_time_delta} for send the email", print_text=True)

    # time.sleep(wait_time)

    # Get data from google sheet
    sheet_link = config.get_credential("sheet_link")
    gss = google_shets(sheet_link)
    data = gss.get_data()
    
    # Get random sentence 
    english_header = config.get_credential("english_header")
    japanese_header = config.get_credential("japanese_header")
    random_sentence = random.randrange(0, len (data))
    english = data[random_sentence][english_header]
    japanese = data[random_sentence][japanese_header]

    # Get data for send email
    email = config.get_credential("from_email")
    password = config.get_credential("password")
    to_email = config.get_credential("to_email")
    subject = f"Daily learning: {english}"
    body = japanese
    logs.info(f"from email: {email}")
    logs.info(f"password: {password}")
    logs.info(f"to email: {to_email}", print_text=True)
    logs.info(f"subject: {subject}", print_text=True)
    logs.info(f"body: {body}")

    # Send email
    sender = Email_manager(email, password)
    sender.send_email(receivers=[to_email], 
                      subject=subject, 
                      body=body)

if __name__ == "__main__":
    main()