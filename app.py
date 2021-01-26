# -*- coding:UTF-8 -*-
from flask import Flask
from flask import render_template
from flask import request
import utils
app = Flask(__name__, static_folder='./static')

leetcode_page_data = utils.get_leetcode_data()
leetcode_page_num = len(leetcode_page_data)


@app.route('/')
def hello_world():
    navi_dic = utils.get_navi()
    return render_template('index.html', navi_dic=navi_dic, leetcode_page=leetcode_page_num)


@app.route('/to_consumption')
def to_consumption():
    return render_template('consumption.html')


@app.route('/close')
def not_open():
    return 'constructing...'


@app.route('/time')
def get_time():
    return utils.get_time()


@app.route('/get_project')
def get_project():
    pro_list = utils.get_project_file()
    return {'data': pro_list}


@app.route('/get_article')
def get_article():
    return {'data': utils.get_article_file()}


@app.route('/to_article')
def to_article():
    idx = request.args.get('id')
    return utils.get_article_content(idx=idx)


@app.route('/get_statistics')
def get_statistics():
    return {'data': utils.get_statistics_file()}


@app.route('/password')
def get_password():
    return '这都想看？？滚！'


@app.route('/photo')
def get_photo():
    return '对不起，仅女生可见。'


@app.route('/leetcode_page')
def to_leetcode_page():
    idx = int(request.args.get('page'))
    return {'data': leetcode_page_data[idx]}


@app.route('/msg_board')
def msg_board():
    return {'data': utils.get_msg_borad()}


@app.route('/get_msg')
def get_msg():
    msg = request.args.get('msg')
    print('msg = ', msg)
    utils.save_msg(msg)
    return 'hello world'


@app.route('/to_log')
def to_log():
    return utils.get_log()


@app.route('/get_cnt')
def get_cnt():
    ip, location = request.args.get('ip').split(',')
    # print(ip, location)
    return {'data': utils.get_cnt(ip, location)}


@app.route('/get_consumption')
def get_consumption():
    return {'data': utils.parse_consumption()}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
