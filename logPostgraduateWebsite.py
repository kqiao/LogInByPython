
import cookielib, urllib, urllib2
import time, sys
import argparse

# 使用argparse添加命令行参数
parser = argparse.ArgumentParser(description="Login into postgraduate website")
parser.add_argument('username', help='The login username')
parser.add_argument('password', help='The login password')
args = parser.parse_args()

# Step1. 添加cookie处理器
'''注意：在追踪登录研究生信息系统会话的过程中，发现必须先登录entryUrl得到JSESSION值，
   该值在登录loginUrl中需要作为请求头进行发送。另外具体登录那个url，应该以捕获到的会话信息为准，
   而不是浏览器地址栏显示出的结果'''
entryUrl = "http://210.27.12.1:90/student/index.jsp"
loginUrl = "http://210.27.12.1:90/j_security_check"

cl = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cl))
urllib2.install_opener(opener)

urllib2.urlopen(entryUrl)	#获取临时JSESSION值
para = {'j_username' : args.username,
        'j_password' : args.password,
       }

postData = urllib.urlencode(para)

headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
req = urllib2.Request(url = loginUrl, data = postData, headers = headers)

next = urllib2.urlopen(req)		#open this page
print next.geturl()

print "Now time: ",
cur_time = time.localtime();
print time.strftime("%a, %d %b %Y %H, %H:%M:%S ", cur_time)
# time.sleep(10)	#sleep的参数单位为秒
