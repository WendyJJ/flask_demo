import os

# from .functions import get_database_config


# flask项目路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 静态文件夹路径
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# 前端网页文件夹路径
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

DATABASE = {
    'database': 'mysql',
    'driver': 'pymysql',
    'host': '127.0.0.1',
    'port': '3306',
    'user': '用户名',
    'password': '密码',
    'name': '数据库名',
}

SQLALCHEMY_DATABASE_URI = get_database_config(DATABASE)

# 上传文件夹路径
UPLOAD_DIRS = os.path.join(STATIC_DIR, 'upload')
UPLOAD_AVATAR_DIRS = os.path.join(UPLOAD_DIRS, 'user')
UPLOAD_HOUSE_IMAGE_DIRS = os.path.join(UPLOAD_DIRS, 'house')