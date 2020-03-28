from datetime import datetime as dt

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code or entered_code is False or correct_code is False:
        return False
    if  dt.strptime(current_date, "%B %d, %Y") > dt.strptime(expiration_date, "%B %d, %Y"):
        return False
    else:
        return True
