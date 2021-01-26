import requests
import json
import pandas as pd
from sqlalchemy import create_engine

url = 'https://leetcode-cn.com/api/problems/all/'

header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.80 Safari/537.36 ',
    'cookie': 'csrftoken=Y5TJ3qn7gaXW24QP1eNrSrk5lqrXmKKbRgAbgPAPM58L6xzrRllv9fELtrmMUIdS; '
              'gr_user_id=1d599604-093a-4701-bc40-9f0e50f3f225; _ga=GA1.2.267618807.1608274189; '
              'grwng_uid=f799f562-8bbf-4313-8b23-17ea7cf34fed; __auc=798a37b3176749cad67f8c520d4; '
              'LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
              '.eyJuZXh0X2FmdGVyX29hdXRoIjoiL3Byb2JsZW1zL2ZpbmQtdGhlLWRpZmZlcmVuY2UvIiwiX2F1dGhfdXNlcl9pZCI6IjIwNzg3OTQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjEzNWJmNjk0MWIzMGYwNmMxNmI1YjkzMjVlYzU4YWE5NjA4MWY3M2NlZGY3OWE2NzJhMWVhZGUyY2NhYjU5NmQiLCJpZCI6MjA3ODc5NCwiZW1haWwiOiIiLCJ1c2VybmFtZSI6InJpLXl1ZS10b25nLWh1aS10IiwidXNlcl9zbHVnIjoicmkteXVlLXRvbmctaHVpLXQiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS1jbi5jb20vYWxpeXVuLWxjLXVwbG9hZC91c2Vycy9yaS15dWUtdG9uZy1odWktdC9hdmF0YXJfMTYwNTQ5NjE1NS5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiX3RpbWVzdGFtcCI6MTYwODI3NDIwMS44MjUyMX0.FfH9lHLb_XzB8ba8qgUXj7yO4xOQkwfgmCG_i-xNWeY; a2873925c34ecbd2_gr_last_sent_cs1=ri-yue-tong-hui-t; _gid=GA1.2.675167000.1608534610; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1608389272,1608534609,1608545436,1608563377; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1608563377; a2873925c34ecbd2_gr_session_id=51f8c52a-5c4b-4bdf-bc27-af25cbbe8728; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=51f8c52a-5c4b-4bdf-bc27-af25cbbe8728; a2873925c34ecbd2_gr_cs1=ri-yue-tong-hui-t; a2873925c34ecbd2_gr_session_id_51f8c52a-5c4b-4bdf-bc27-af25cbbe8728=true '
}

res = requests.get(url, headers=header)
data = json.loads(res.text)
# print(data)
# print(data.keys())

stats = data['stat_status_pairs']
print(stats[0])
# exit()
num_solved, num_total = data["num_solved"], data['num_total']
ac_easy, ac_medium, ac_hard = data['ac_easy'], data['ac_medium'], data['ac_hard']

res_dic = {
    'question_id': [],
    'sp_id': [],
    'title': [],
    'status': [],
    'difficulty': [],
    'url': []
}

for stat in stats:
    cur_data = stat['stat']
    print(cur_data['question_id'], cur_data['question__title'], stat['status'], stat['difficulty']['level'])
    res_dic['question_id'].append(cur_data['question_id'])
    res_dic['sp_id'].append(cur_data['frontend_question_id'])
    res_dic['title'].append(cur_data['question__title'])
    res_dic['status'].append(stat['status'])
    res_dic['difficulty'].append(stat['difficulty']['level'])
    res_dic['url'].append(cur_data['question__title_slug'])

# # print(res_dic)
data_frame = pd.DataFrame(res_dic).set_index('question_id')
print(data_frame)

engine = create_engine('mysql+pymysql://root:540279653@localhost/my_data')
data_frame.to_sql('Leetcode', con=engine, if_exists='replace')
print('Complete...')
