FROM registry.cn-qingdao.aliyuncs.com/imaxu/python-nginx-flask-uwsgi:1.0

COPY ./app /app
WORKDIR 	/app
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple flask flask_script pymysql flask_sqlalchemy requests apscheduler
