import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        # 数据库驱动  Database driver
        'ENGINE': 'django.db.backends.sqlite3',
        # 如果是mysql等数据库 这里应该是数据库名
        # Replace it with Database Name if use other DATABASES
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = (
    'db',
)

# 强烈建议修改并 保护好它
# SECURITY WARNING: keep the secret key used in production secret,recommended to modify it!!
SECRET_KEY = '6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa'
