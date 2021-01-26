import time
import os
import pymysql
import smtplib
from email.mime.text import MIMEText


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


def query(sql, *args):
    conn, cursor = get_connection()
    cursor.execute(sql, *args)
    res = cursor.fetchall()
    close_connection(conn, cursor)
    return res


def get_time():
    return time.strftime('%Y-%m-%d %X')


def get_project_file():
    file_path = './static/file/project/'
    pro_list = []
    pro_names = os.listdir(file_path)
    pro_names.sort()
    for pro_name in pro_names:
        cur_dic = {}
        if pro_name != '.DS_Store':
            cur_dic['name'] = pro_name
            for file in os.listdir(file_path+pro_name):
                if file.endswith('.pdf'):
                    cur_dic['report'] = file_path + pro_name + '/' + file
                elif file.endswith('.zip'):
                    cur_dic['src_code'] = file_path + pro_name + '/' + file
            pro_list.append(cur_dic)
    # print(pro_list)
    return pro_list


def get_article_file():
    file_path = './static/file/article/'
    art_names = os.listdir(file_path)
    art_names.sort()
    if '.DS_Store' in art_names:
        art_names.remove('.DS_Store')
    res = ''
    for index, art_name in enumerate(art_names):
        if art_name != '.DS_Store':
            res += '<li class="project_list"><a class="project_list" href="/to_article?id=' + str(index+1) + '">' + art_name[:-4] + '</a></li> '
    return '<ul>' + res + '</ul>'


def get_article_content(idx):
    file_path = './static/file/article/'
    cur_file = None
    for art in os.listdir(file_path):
        if art.startswith(str(idx) + '.'):
            cur_file = art
    with open(file_path + cur_file, 'r') as f:
        content = f.read()
        f.close()
    return content.replace('\n', '\n<br>')


def get_navi():
    navi_dic = {
        '我的主页': 'http://www.zhenghui.tech',
        '百度一下，你就知道': 'https://www.baidu.com/',
        'github': 'https://github.com/bupt-zhenghui?tab=repositories',
        'Kaggle': 'https://www.kaggle.com/',
        '北邮人论坛': 'https://bbs.byr.cn/',
        '题库-力扣（LeetCode）': 'https://leetcode-cn.com/problemset/all/',
        '在线翻译_有道': 'http://fanyi.youdao.com/',
        '李宏毅2020机器学习': 'https://www.bilibili.com/video/BV1JE411g7XF?from=search&seid=664638880959715412',
        'ModelArts': 'https://console.huaweicloud.com/modelarts/?region=cn-north-4#/notebook',
        '北京邮电大学邮箱': 'https://mail.bupt.edu.cn/cgi-bin/frame_html?sid=yNd8kDP0Ht1PfVYJ,'
                        '2&sign_type=&r=d9b06432533848e8770afdf9b35cb228',
        'BYRBT::登录': 'https://bt.byr.cn/login.php',
        '斗鱼-直播平台': 'https://www.douyu.com/',
        'EI检索': 'https://www.engineeringvillage.com/search/quick.url',
        'Youtube': 'https://www.youtube.com/',
        'QMPlus': 'https://qmplus.qmul.ac.uk/course/view.php?idnumber=BUPT-Home',
        '吴恩达GANs教程': 'https://www.bilibili.com/video/BV1b54y1k7bY?from=search&seid=4951365797172491570',
        '莫烦PyTorch': 'https://www.bilibili.com/video/BV1Vx411j7kT?from=search&seid=2555523775255016335',
        'Google Scholar': 'https://scholar.google.com/',
        '阿里巴巴矢量图标库': 'https://www.iconfont.cn/',
        'nice算法组': 'http://wiki.niceprivate.com/pages/viewpage.action?pageId=10490410',
        'nice邮箱': 'http://mail.oneniceapp.com/alimail/',
        '美餐': 'https://meican.com/preference/user'
    }
    return navi_dic


def get_leetcode_data():
    sql = 'select question_id, title, status, difficulty, url from Leetcode where status="ac" order by question_id;'
    res = query(sql)
    # print(res)
    res_list = []
    color = ['white', 'aqua', 'red']
    for i in range(len(res)):
        cur_dic = {
            'id': int(res[i][0]) % 1000,
            'title': res[i][1],
            'status': True if res[i][2] == 'ac' else False,
            'difficulty': color[res[i][3]-1],
            'url': res[i][4]
        }
        res_list.append(cur_dic)
    page_num = len(res_list) // 40 + 1
    page_data = []
    for i in range(page_num):
        if i == page_num - 1:
            page_data.append(pre_processing_leetcode_data(res_list[40*i:]))
        else:
            page_data.append(pre_processing_leetcode_data(res_list[40*i:40*(i+1)]))
    return page_data


def pre_processing_leetcode_data(batch_data):
    res = ''
    for data in batch_data:
        cur_res = '<a href="https://leetcode-cn.com/problems/' + data['url'] + ' "target="_blank">' \
                '<li class="leetcode_list" style="color:' + data['difficulty'] + '">'
        if data['status']:
            cur_res += '<img style="width:1rem;height:1rem;top:1rem" src="../static/img/ac.png">'
        else:
            cur_res += '&emsp;&nbsp;'
        cur_res += str(data['id']) + '. ' + data['title'] + '</li></a>'
        res += cur_res
    return '<ul style="padding:0;margin-top:1.5rem;font-size:1rem">' + res + '</ul>'


def get_statistics_file():
    file_path = './static/file/statistics/'
    sta_names = os.listdir(file_path)
    sta_names.sort()
    if '.DS_Store' in sta_names:
        sta_names.remove('.DS_Store')
    # print(sta_names)
    res = ''
    for index, sta_name in enumerate(sta_names):
        res += '<li class="project_list">' + sta_name[:-4] + '<a style="color:aqua" class="default" href=' \
            '"../static/file/statistics/' + sta_name + '">[' + sta_name.split('.')[-1] + ']</a></li>'
    return '<ul>' + res + '</ul>'


def get_msg_borad():
    return '''
        <textarea id="msg" class="msg_board" rows="12" cols="70">
            Any useful advice would be appreciated!
            You can leave your contact information if you want to~
        </textarea>
        <a onclick="clear_msg()"><button class="clear_btn">清空</button></a>
        <button class="submit_btn" onclick="fetch_msg()">提交</button>
    '''


def save_msg(msg):
    file_path = './static/msg_board.txt'
    with open(file_path, 'a+') as f:
        f.write('\n' + msg + '\n')
    f.close()
    print('Save message successfully!')
    send_email(msg)


def send_email(msg):
    # smtp = smtplib.SMTP()
    # smtp.connect('smtp.qq.com', 25)
    smtp = smtplib.SMTP_SSL('smtp.qq.com')
    smtp.ehlo('smtp.qq.com')
    smtp.login(540279653, 'dnxpmxbzswvnbbeg')
    text = MIMEText(msg, 'plain', 'utf-8')
    smtp.sendmail('540279653@qq.com', 'wangzhenghui@bupt.edu.cn', text.as_string())
    smtp.quit()
    print('Complete...')


def get_log():
    res = ''
    file_path = './static/log.txt'
    with open(file_path) as f:
        line = f.readline()
        while line:
            res += line + '<br>'
            line = f.readline()
    f.close()
    return res


def create_table():

    sql = '''
        create table access_info(
        cnt int not null,
        ip char(20),
        location char(50),
        time char(20))
    '''
    conn, cursor = get_connection()
    cursor.execute(sql)
    print('Create table successfully!')
    close_connection(conn, cursor)


def insert_table(cnt, ip, location, time):
    sql = 'insert into access_info values (%s, %s, %s, %s)'
    conn, cursor = get_connection()
    cursor.execute(sql, (cnt, ip, location, time))
    conn.commit()
    print('Insert table successfully!')
    close_connection(conn, cursor)


def get_cnt(ip, location):
    txt_path = './static/cnt.txt'
    cnt = None

    if not os.path.exists(txt_path):
        create_table()
        cnt = 1
        with open(txt_path, 'w') as f:
            f.write(str(cnt))
        f.close()

    else:
        with open(txt_path, 'r') as f:
            line = f.readline()
            cnt = int(line) + 1
        f.close()
        with open(txt_path, 'w') as f:
            f.write(str(cnt))
        f.close()
        insert_table(cnt, ip, location, get_time())
    return cnt


def get_daily_consumption():
    sql = 'select * from transaction order by trans_id desc'
    res = query(sql)
    res_dic = {}
    for trans in res:
        cur_date = trans[4].split(' ')[0]
        if trans[3] == 'negtive':
            if cur_date not in res_dic:
                res_dic[cur_date] = [trans[2], [[trans[1], trans[2], trans[4].split(' ')[1]]]]
            else:
                cur_val = float(res_dic[cur_date][0]) + float(trans[2])
                res_dic[cur_date][0] = '%.2f' % cur_val
                res_dic[cur_date][1].insert(0, [trans[1], trans[2], trans[4].split(' ')[1]])
    # for res in res_dic.items():
    #     print(res)
    return res_dic


def parse_consumption():
    trans_dic = get_daily_consumption()
    top_val = 10
    pre_html = '''
        <table class="table" border="2" style="top:{}px">
        <tr><th colspan="3">{}</th></tr>
        <tr><td colspan="3" align="center">消费总额：{}(元)</td></tr>
        <tr><th style="width:500px">消费用途</th><th>消费金额(元)</th><th>消费时间</th></tr>
    '''
    table_html = '<tr><td>{}</td><td>{}</td><td>{}</td></tr>'
    post_html = '</table><br>'

    cur_html = ''
    for key, value in trans_dic.items():
        cur_html += pre_html.format(top_val, key, value[0])
        top_val += 118
        for item in value[1]:
            cur_html += table_html.format(item[0], item[1], item[2])
            top_val += 28
        cur_html += post_html
    # print(cur_html)
    return cur_html


# get_time()
# get_project_file()
# get_leetcode_data()
# print(get_statistics_file())
# send_email('hello world')
# get_daily_consumption()
# parse_consumption()
