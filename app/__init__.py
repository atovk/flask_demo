from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

import pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
# 加载 instance 内配置
app.config.from_pyfile('config.py')
# 现在通过app.config["VAR_NAME"]，我们可以访问到对应的变量

# 启用数据库 ORC
db = SQLAlchemy(app)

engine = create_engine(app.config.get("SQLALCHEMY_DATABASE_URI"))
# 在api.gnizama.com中添加API蓝图

