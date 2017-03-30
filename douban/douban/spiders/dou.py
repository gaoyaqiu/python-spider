# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
import urllib.request
import os


class DouSpider(scrapy.Spider):
    name = "dou"
    allowed_domains = ["douban.com"]
    # start_urls = ['http://douban.com/']

    header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

    def start_requests(self):
        # 请求登陆页
        return [Request('https://accounts.douban.com/login', meta = {'cookiejar': 1}, callback = self.parse)]
    def parse(self, response):
        # 判断是否存在验证码
        captcha_image = response.xpath("//img[@id='captcha_image']/@src").extract()
        print(captcha_image)
        if len(captcha_image) > 0:
            print('有验证码, 等待识别...')
            # 将验证码下载到本地
            local_path = '/Users/gaoyaqiu/Downloads/python-test/test/captcha.png'
            urllib.request.urlretrieve(captcha_image[0], filename = local_path)
            # 方法1: 通过半自动人工处理
            #captcha_value = input('请输入/Users/gaoyaqiu/Downloads/python-test/test/中captcha.png的验证码内容! ')
            # 方法2: 通过接口实现全自动处理-1 (这里使用的是云打码的api,因他们接口不提供mac版本,所以这里例子只能在windows中使用)
            # 使用注意: 需要将YDMPython3.py 中的账号信息替换成自己的账号
            '''
            cmd = 'python3.5 /Users/gaoyaqiu/git/python-spider/douban/ydm/YDMPython3.py'
            r = os.popen(cmd)
            captcha_value = r.read()
            '''

            # 方法3: 通过接口实现全自动处理-2 (这里使用的是云打码的http api python2.7)
            cmd = 'python2.7 /Users/gaoyaqiu/git/python-spider/douban/ydm/YDMHTTP.py'
            r = os.popen(cmd)
            read_result = r.read().split()
            cid = read_result[0]
            if int(cid) > 0:
                captcha_value = str(read_result[1])
                print('当前验证码识别结果为: cid: %s, result: %s' % (cid, captcha_value))
                params = {
                    'captcha-solution': captcha_value,
                    'redir': 'https://www.douban.com/people/156127818/',  # 登陆成功之后的重定向地址,可是自己主页地址
                    'form_email': '账号',
                    'form_password': '密码'
                }
            else:
                print('识别验证码出错cid: ' + cid)
        else:
            params = {
                'redir': 'https://www.douban.com/people/156127818/',
                'form_email': '账号',
                'form_password': '密码'
            }

        print('登陆中。。。')
        # 开始登陆
        return [FormRequest.from_response(response,
                                          # 设置cookie
                                          meta = {'cookiejar': response.meta['cookiejar']},
                                          # 设置header信息
                                          headers = self.header,
                                          # 设置post表单提交数据
                                          formdata = params,
                                          callback = self.next
                                          )]
    def next(self, response):
        # 登陆成功之后查看title信息,确认是跳转成功
        title = response.xpath("/html/head/title/text()").extract()
        print(title)

