#Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

def timeConversion(s):
    # Write your code here
    s = s.split(":")

    if "AM" in s[2]:
        s[2]=s[2].replace('AM','')
        if int(s[0]) == 12:
            s[0]=s[0].replace('12','00')

    if "PM" in s[2]:
        s[2]=s[2].replace('PM','')
        if s[0] != '12':
            s[0]=str(int(s[0])+12)

    return(':'.join(s));