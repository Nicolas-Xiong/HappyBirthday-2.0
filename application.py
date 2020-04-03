# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 07:37:07 2020

@author: Nicolas Xiong
"""

from flask import Flask
from flask import render_template
import datetime 
import os
import sys




#兼容处理
WIN = sys.platform.startswith('win') 
if WIN:  # 如果是 Windows 系统，使用三个斜线    
    prefix = 'sqlite:///' 
else:  # 否则使用四个斜线    
    prefix = 'sqlite:////'


app=Flask(__name__)
 
app.secret_key='d'     #按错误提示加的密钥
app.config['DEBUG']=True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = datetime.timedelta(seconds=1)

#从环境变量中读取密钥，如果没有读取到，则使用默认值
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')




@app.route('/index', methods=['GET'])
def index():     
    return render_template('index.html')

@app.route('/', methods=['GET'])
def demo():     
    return render_template('demo.html')



























