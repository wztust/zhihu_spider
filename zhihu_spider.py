import requests
import pandas as pd
import time

# url = 'https://www.zhihu.com/api/v4/members/Talyer-Wei/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset=40&limit=20'
headers = { 'cookie' : '_zap=48b7efb1-99a0-4d6f-ad05-d060ca7868bc; __DAYU_PP=fU2RFnRFmFqeqJ7y3Inyffffffff866c1a423dce; d_c0="AMBg2DKYjQ2PTqA5IUzqYHWFmqiHVPuB5sI=|1525620547"; _xsrf=bw8eqKvxgz9oPLr39WNboEPzLNyTbCxl; z_c0="2|1:0|10:1546680985|4:z_c0|92:Mi4xdmlwdkJ3QUFBQUFBd0dEWU1waU5EU1lBQUFCZ0FsVk5tY2dkWFFCbXg4bWpBOVRkYmNTczk3d3RUR2UyT0RjMGFR|a5fe88abaa960d4fc88e55e24f2bba0316a0793358771d4debdeedea4bd168b1"; tst=r; __gads=ID=b3dea12a8e8fcac8:T=1557422736:S=ALNI_MZ5r22ZK0ZpWsvpD3GvocZk8bAPcA; q_c1=9b12c61a269a4553aa507ad104554da9|1557666332000|1517637916000; tgw_l7_route=578107ff0d4b4f191be329db6089ff48',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74'
            }
user_data = []
def get_User_Data(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/Talyer-Wei/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
        r = requests.get(url,headers=headers).json()['data']
        user_data.extend(r)
        print('正在获取第{}页的数据'.format(i+1))
        time.sleep(0.9)
if __name__ == '__main__':
    get_User_Data(100)
    df = pd.DataFrame(user_data)
    df.to_excel('user_data.xlsx')







