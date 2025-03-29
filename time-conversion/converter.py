import os

def timeConversion(s):
    hh, mm, ss_period = s[:-2].split(":")

    period = s[-2:]
    hh = int(hh)

    if period == 'AM':
        if hh == 12:
            hh = 00 #midgnight (12am - 00hh)
    else:
        if hh != 12:
            hh += 12
    return f"{hh:00}:{mm}:{ss_period}"

if __name__ == '__main__':
   
    s = input().strip()

    result = timeConversion(s)
    print(result)
