import pymysql
import requests
import json
import pandas as pd
from sqlalchemy import create_engine
import time

url = 'https://wx.tenpay.com/cgi-bin/mmpayweb-bin/balanceuserrolllist?classify_type=0&count=20&csrf_token' \
      '=frrIgsLs2nWc8PJSF2tq3G49mQcliIHv&exportkey=AydfWw%2BD5krvp2oHGsXc%2BOM%3D&sort_type=1 '

header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.80 Safari/537.36 ',
    'cookie': 'balanceuserroll_encryption=N0h+9YeXmGmdJlIn5/KYAzou5HcHV1nV0rbXysSrsXf+XT7LYeca8o1TFuybLJClOu4jFe5PkMA'
              '+7HZ0FJAN/t85K6OLe6YpvKLS1L7R+gi5aXg8rtb2l+G7ItDUAcUR8KYBP8dqSDFqfK6BdGW19A==; '
              'wxp_log_uid=BgAAyPUJfS%2BNxHrAgmcVakOr7fkizrqkUVssrw0%3D '
}


def get_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='540279653',
        db='my_data',
        charset='utf8'
    )
    cursor = conn.cursor()
    return conn, cursor


def close_connection(conn, cursor):
    conn.close()
    cursor.close()


def check_latest_info():
    sql = 'select trans_id from transaction order by trans_id desc limit 1'

    conn, cursor = get_connection()
    cursor.execute(sql)
    res = cursor.fetchall()
    close_connection(conn, cursor)
    return res


def transform_info(info_list):
    title, timestamp, fee = info_list[0], info_list[1], info_list[2]

    # parse title
    new_title = ''
    key_word = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '（', '）', ' ', '-', '_', '：', '.'}
    for s in title:
        if s not in key_word:
            new_title += s
    info_list[0] = new_title

    # parse time
    new_time = time.localtime(int(timestamp))
    formatTime = time.strftime("%Y-%m-%d %H:%M:%S", new_time)
    info_list[1] = formatTime

    # parse fee
    fee = '%.2f' % (fee / 100)
    info_list[2] = fee

    return info_list


res = requests.get(url, headers=header)
# print(res.text)
data = json.loads(res.text)['record']
info_list = ['title', 'timestamp', 'fee', 'fee_attr', 'remaining_balance']
data_dic = {
    'trans_id': [],
    'title': [],
    'fee': [],
    'type': [],
    'time': [],
    'balance': []
}

latest = check_latest_info()
# print(latest[0][0])

for idx, trans in enumerate(data):
    if trans['timestamp'] == latest[0][0]:
        break
    cur_info = [trans[i] for i in info_list]
    parse_info = transform_info(cur_info)

    data_dic['trans_id'].append(trans['timestamp'])
    data_dic['title'].append(parse_info[0])
    data_dic['time'].append(parse_info[1])
    data_dic['fee'].append(parse_info[2])
    data_dic['type'].append(parse_info[3])
    data_dic['balance'].append(parse_info[4])

data_frame = pd.DataFrame(data_dic).set_index('trans_id')
print(data_frame)

engine = create_engine('mysql+pymysql://root:540279653@localhost/my_data')
data_frame.to_sql('transaction', con=engine, if_exists='append')
print('Complete...')

