import os
import sys

from dotenv import load_dotenv
load_dotenv('C:\Python37\workspace\AirdukaLottery\conn\.env')

AT_SMS_KEY = os.environ.get("AT_SMS_KEY")

print(AT_SMS_KEY)