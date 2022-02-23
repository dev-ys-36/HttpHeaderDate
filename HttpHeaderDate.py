import urllib.request as urlRQ
import datetime
import time

def header_date(url):

    rq = urlRQ.urlopen(url).headers['Date'][5:-4] # 23 Feb 2022 16:18:14 => GMT

    months = {
        'Jan':'01',
        'Feb':'02',
        'Mar':'03',
        'Apr':'04',
        'May':'05',
        'Jun':'06',
        'Jul':'07',
        'Aug':'08',
        'Sep':'09',
        'Oct':'10',
        'Nov':'11',
        'Dec':'12'

    }

    year = int(rq[7:11])
    month = int(months[rq[3:6]])
    day = int(rq[:2])
    hour = int(rq[12:14])
    minute = int(rq[15:17])
    second = int(rq[18:])

    """msg1 = '* <' + url + '> server request time - zone'
    msg2 = '* ' + rq[7:11] + '년 ' + rq[3:6] + '월 ' + rq[:2] + '일 ' + rq[12:14] + '시 ' + rq[15:17] + '분 ' + rq[18:] + '초'

    print(msg1)
    print(msg2)

    KST = datetime.timezone(datetime.timedelta(hours=9))
    time = datetime.datetime(year, month, day, hour, minute, second, tzinfo=KST)"""

    server_name = '* <' + url + '> request time = '
    times = datetime.datetime(year, month, day, hour, minute, second) + datetime.timedelta(hours=9)

    return server_name + str(times)

while(True):

    print(header_date('http://sugang.suwings.syu.ac.kr/'))

    time.sleep(1)