import datetime
from pytz import timezone
from twilio.rest import Client
from twilio.rest import Client
import os

def validate_day_and_time(year, month, day):
    nd = datetime.date(year, month, day).weekday()
    days = ['월', '화', '수', '목', '금', '토', '일']
    if '토' == days[nd]:
        return True
    return False

def send_sms():
    account = os.environ['ACCOUNT']
    token = os.environ['TOKEN']
    client = Client(account, token)

    message = client.messages.create(to=os.environ['PHONE_NUMBER'], from_=os.environ[ONLINE_PHONE_NUMBER],
                                 body="Hello th")
    print(message.sid)






current_time = datetime.datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d')
year, month, day = map(int, current_time.split('-'))    # 2022-08-06
print(validate_day_and_time(year, month, day))
if validate_day_and_time(year, month, day):
    send_sms()
