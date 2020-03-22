from flask import Flask,session
from datetime import datetime
from flask import render_template
from flask import Blueprint,jsonify
from flask import request
import requests

import time
app = Flask(__name__)

# app.secret_key = 'SET_ME_BEFORE_USE_SESSION'
#
# @app.route('/')
# def hello_world():
#     return render_template("index.html")
#
#
# # @app.route('/write_session')
# # def write_session():
# #     session["key_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    # 将当前时间保存到session中
# #     return session["key_time"]                                            # 返回当前时间
#
#
# @app.route('/write_session')
# def write_session():
#     session["key_time"] = time.time()    # 将当前时间保存到session中
#     return session.modified              # 因为之前进行了session设置，所以此处返回Ture
#
#
# @app.route('/read_session')
# def read_session():
#     return session.get("key_time")     # 获取上次调用writeSession时写入的时间，并返回


@app.route("/api/post_callback", methods=["POST"])
def post_callback():
    """
    接收回调
    :return:
    """
    try:
        data = request.headers
        print(data)
        return 'success'
    except:
        return jsonify({'errorCode': '929', 'msg': 'Required parameter missing or parameter error'})


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=7779,
        debug=True
    )


