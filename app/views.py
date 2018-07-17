from flask import Blueprint, render_template
from . import app
from . import engine
import time

app = app


@app.route('/apis')
def list_apis():
    date1 = time.time()
    conn = engine.connect()
    tables = conn.execute("select keeprate from che300_car_keeprate where series_id = '54'and province_id ='1' and usage_year =1.0 and car_status = '0'")

    date2 = time.time()
    print(date2 - date1)
    # for row in tables:
    #     print(row)
    conn.close()
    tables.close()
    return "调用完成！"
