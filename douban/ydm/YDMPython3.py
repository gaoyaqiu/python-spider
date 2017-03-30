# -*- coding: cp936 -*-

import sys
import os
from ctypes import *

# 下载接口放目录 http://www.yundama.com/apidoc/YDM_SDK.html
# 错误代码请查询 http://www.yundama.com/apidoc/YDM_ErrorCode.html
# 所有函数请查询 http://www.yundama.com/apidoc

print('>>>正在初始化...')

YDMApi = windll.LoadLibrary('/Users/gaoyaqiu/git/python-spider/douban/ydm/yundamaAPI-x64.dll')

# 1. http://www.yundama.com/index/reg/developer 注册开发者账号
# 2. http://www.yundama.com/developer/myapp 添加新软件
# 3. 使用添加的软件ID和密钥进行开发，享受丰厚分成

appId = 1   # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
appKey = b'1'     # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！

print('软件ＩＤ：%d\r\n软件密钥：%s' % (appId, appKey))

# 注意这里是普通会员账号，不是开发者账号，注册地址 http://www.yundama.com/index/reg/user
# 开发者可以联系客服领取免费调试题分

username = b'1'
password = b'1'

if username == b'test':
	exit('\r\n>>>请先设置用户名密码')
	
####################### 一键识别函数 YDM_EasyDecodeByPath #######################

print('\r\n>>>正在一键识别...')

# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
codetype = 3000

# 分配30个字节存放识别结果
result = c_char_p(b"                              ")    

# 识别超时时间 单位：秒
timeout = 60

# 验证码文件路径
filename = b'/Users/gaoyaqiu/Downloads/python-test/test/captcha.png'

# 一键识别函数，无需调用 YDM_SetAppInfo 和 YDM_Login，适合脚本调用
captchaId = YDMApi.YDM_EasyDecodeByPath(username, password, appId, appKey, filename, codetype, timeout, result)

print("一键识别：验证码ID：%d，识别结果：%s" % (captchaId, result.value))

################################################################################


########################## 普通识别函数 YDM_DecodeByPath #########################

print('\r\n>>>正在登陆...')

# 第一步：初始化云打码，只需调用一次即可
YDMApi.YDM_SetAppInfo(appId, appKey)

# 第二步：登陆云打码账号，只需调用一次即可
uid = YDMApi.YDM_Login(username, password)

if uid > 0:

    print('>>>正在获取余额...')
    
    # 查询账号余额，按需要调用
    balance = YDMApi.YDM_GetBalance(username, password)
    
    print('登陆成功，用户名：%s，剩余题分：%d' % (username, balance))

    print('\r\n>>>正在普通识别...')

    # 第三步：开始识别
    
    # 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype = 3000

    # 分配30个字节存放识别结果
    result = c_char_p(b"                              ")

    # 验证码文件路径
    filename = b'/Users/gaoyaqiu/Downloads/python-test/test/captcha.png'

    # 普通识别函数，需先调用 YDM_SetAppInfo 和 YDM_Login 初始化
    captchaId = YDMApi.YDM_DecodeByPath(filename, codetype, result)

    print("普通识别：验证码ID：%d，识别结果：%s" % (captchaId, result.value))
    
else:
    print('登陆失败，错误代码：%d' % uid)

################################################################################

print('\r\n>>>错误代码请查询 http://www.yundama.com/apidoc/YDM_ErrorCode.html')

input('\r\n测试完成，按回车键结束...')
