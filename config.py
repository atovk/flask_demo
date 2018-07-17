DEBUG = False
SQLALCHEMY_ECHO = False

BCRYPT_LEVEL = 13  # 配置Flask-Bcrypt拓展
MAIL_FROM_EMAIL = "robert@a2vk.com"  # 设置邮件来源

SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_POOL_TIMEOUT = 30
SQLALCHEMY_POOL_RECYCLE = 5
SQLALCHEMY_MAX_OVERFLOW = 0

# 数据库连接
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '132456'
HOST = '10.1.100.109'
PORT = '3306'
DATABASE = 'test'
# 这个连接字符串变量名是固定的具体 参考 flask_sqlalchemy  文档 sqlalchemy 会自动找到flask配置中的 这个变量
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME,
                                                                       PASSWORD, HOST, PORT, DATABASE)