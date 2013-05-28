import cookielib, urllib, urllib2, sys
import argparse

'''如何使用argparse，进行参数传递'''
# Step1.创建一个ArgumentParser对象，可以添加description参数表示对该程序的说明
parser = argparse.ArgumentParser(description="Login into XiDian Library")
# Step2.使用parser.add_argument添加参数
parser.add_argument("username", help="The login username")
parser.add_argument("password", help="The login password")
# Step3.解析参数，将存入的参数放入args中
args = parser.parse_args()


'''如何模拟登陆一个网站'''
entryUrl = " http://202.117.122.8/patroninfo/ "
# Step1.设置cookie处理器：1）得到cookieJar对象；2）HTTPCookieProcessor安装hanlder;3)安装打开器
cl = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cl))
urllib2.install_opener(opener)

# Step2.使用urlopen打开URL之前，创建postData，使用urllib.urlencode()进行编码
para = {'code' : args.username,
        'pin' : args.password,
       }
postData = urllib.urlencode(para)

# Step3.使用post方法打开url地址。返回一个文件类对象，但是具有两个额外操作geturl()和info()
next = urllib2.urlopen(entryUrl, postData)

print next.geturl()
print next.info()
print "----------------------"

'''如何转换一个字符串的格式'''
# Step1.获取当前系统的编码sys.getfilesystemcoding()
type = sys.getfilesystemencoding()
# Step2.对字符串先解编码decode，在用系统编码格式进行encode
print next.read().decode("UTF_8").encode(type)