import json
import re

import requests
import sqlalchemy
import pandas as pd


if __name__ == '__main__':
    # 建立连接
    engine = sqlalchemy.create_engine("mysql+pymysql://sqlname:password@localhost:3306/fund")


    url = 'http://fund.eastmoney.com/js/fundcode_search.js'
    r = requests.get(url)
    cont = re.findall('var r = (.*])', r.text)[0]  # 提取list
    ls = json.loads(cont)  # 将字符串个事的list转化为list格式
    fund = pd.DataFrame(ls, columns=['fundcode', 'fundsx', 'name', 'category', 'fundpy'])  # list转为DataFrame
    fund.to_sql('fund_all',con=engine,index=False,if_exists='replace')
    fund.to_csv("fund_all.csv",index=False,encoding='gbk')
    print('写入成功！！！')


