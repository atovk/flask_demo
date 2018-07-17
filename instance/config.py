# 私有环境配置文档 在 根config 之后加载
DEBUG = True
SQLALCHEMY_ECHO = True

SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
# 数据库连接
DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '132456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'test'
# 这个连接字符串变量名是固定的具体 参考 flask_sqlalchemy  文档 sqlalchemy会自动找到flask配置中的 这个变量
SQLALCHEMY_DATABASE_URI = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'.format(DIALECT, DRIVER, USERNAME,
                                                                       PASSWORD, HOST, PORT, DATABASE)
