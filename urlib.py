from urllib import request , parse
import urllib
import http.cookiejar
import re


# with request.urlopen('http://cuiqingcai.com/927.html') as f:
#     data = f.read()
#     print('Suatus: ',f.status,f.reason)
#     for k,v in f.getheaders():
#         print('%s: %s' % (k , v))
#     print('Data:', data.decode('utf-8'))


# req =  request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))


# print('Login to weibo.cn...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode([
#     ('username',email),
#     ('password',passwd),
#     ('entry', 'mweibo'),
#     ('client_id', ''),
#     ('savestate', '1'),
#     ('ec', ''),
#     ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
# ])
# req  = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))


# response = request.urlopen("http://www.baidu.com")
# print(response.read())

# 推荐使用者方法
# requestt =request.Request("http://www.baidu.com")
# response = request.urlopen(requestt)
# print(response.read())

# post方式

#get
# values = {"username":"406243283@qq.com","password":"gao3900321"}
# # data = request.urlencode(values)
# data = urllib.parse.urlencode(values)
# url = "http://passport.csdn.net/account/login"
# geturl = url + "?"+data
# print(geturl)
# req = urllib.request.Request(geturl)
# response = urllib.request.urlopen(req)
# print(response.read())

# 加参数

# url = 'http://www.server.com/login'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'username':'cqc',  'password' : 'XXXX' }
#
# headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  ,
#                         'Referer':'http://www.zhihu.com/articles' }
# data = urllib.parse.urlencode(values)
# requestt = urllib.request.Request(url , data , headers)
# resp  = urllib.request.urlopen(requestt)
# print(resp.read())

# 设置代理
# enable_proxy = True
# proxy_header = urllib.request.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
# null_proxy_handler = urllib.request.ProxyHandler({})
# if enable_proxy:
#     opener = urllib.request.build_opener(proxy_header)
# else
#     openr = urllib.request.build_opener(null_proxy_handler)
# urllib.request.install_opener(opener)


#  获取cookie
# # 设置保存cookie的文件，同级目录下的cookie.txt
# filename = 'cookie.txt'
# #声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
# cookie = http.cookiejar.MozillaCookieJar(filename)
# #利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
# handler = urllib.request.HTTPCookieProcessor(cookie)
# #通过handler来构建opener
# opener = urllib.request.build_opener(handler)
# #创建一个请求，原理同urllib2的urlopen
# response = opener.open("http://www.baidu.com")
# #保存cookie到文件
# cookie.save(ignore_discard=True, ignore_expires=True)

# 利用获取到的cookie在进行获取网页
# cookit = http.cookiejar.MozillaCookieJar()
# cookit.load('cookie.txt',ignore_discard=True,ignore_expires=True)
# req = urllib.request.Request("http://www.baidu.com")
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookit))
# response = opener.open(req)
# print(response.read())


# 登录百度账号
# filename = "cookie.txt"
# cookie = http.cookiejar.MozillaCookieJar(filename)
# opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
# postdata = urllib.parse.urlencode({
#     'stuid':'gao300321',
#     'pwd':'3900321'
# })
# loginUrl = "http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login"
# request = opener.open(loginUrl,postdata)
# cookie.save(ignore_expires=True,ignore_discard=True)
# gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
# #请求访问成绩查询网址
# result = opener.open(gradeUrl)
# print (result.read())




# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
# pattern = re.compile(r'hello')
#
# # 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None
# result1 = re.match(pattern,'hello1')
# result2 = re.match(pattern,'helloo CQC!')
# result3 = re.match(pattern,'helo CQC!')
# result4 = re.match(pattern,'hello CQC!')
#
# if result1:
#     print(result1.group())
# else:
#     print('匹配失败')

# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
#
# print("m.string:", m.string)
# print( "m.re:", m.re)
# print ("m.pos:", m.pos)
# print ("m.endpos:", m.endpos)
# print ("m.lastindex:", m.lastindex)
# print ("m.lastgroup:", m.lastgroup)
# print ("m.group():", m.group())
# print ("m.group(1,2):", m.group(1, 2))
# print ("m.groups():", m.groups())
# print ("m.groupdict():", m.groupdict())
# print ("m.start(2):", m.start(2))
# print ("m.end(2):", m.end(2))
# print ("m.span(2):", m.span(2))
# print (r"m.expand(r'\g \g\g'):", m.expand(r'\2 \1\3'))
# m.string: hello world!
# m.re: re.compile('(\\w+) (\\w+)(?P<sign>.*)')
# m.pos: 0
# m.endpos: 12
# m.lastindex: 3
# m.lastgroup: sign
# m.group(): hello world!
# m.group(1,2): ('hello', 'world')
# m.groups(): ('hello', 'world', '!')
# m.groupdict(): {'sign': '!'}
# m.start(2): 6
# m.end(2): 11
# m.span(2): (6, 11)
# m.expand(r'\g \g\g'): world hello!





# 搜索匹配
# pattern = re.compile((r'world'))
# match = re.search(pattern,'hellworld!')
# if match:
#     print(match.group())
#     for value in match.group():
#         print(value)
# else:
#     print('没有')


# split 匹配
# pattern = re.compile(r'\d+')
# print(re.split(pattern,'one1two2three3four4'))
# print(re.findall(pattern,'one1two2three3four4'))
# for m in re.finditer(pattern,'one1two2three3four4'):
#     print (m.group()),

# pattern = re.compile(r'(\w+) (\w+)')
# s = 'i say, hello world!'
#
# print (re.sub(pattern,r'\2 \1', s))
#
# def func(m):
#     return m.group(1).title() + ' ' + m.group(2).title()
#
# print (re.sub(pattern,func, s))

# 实战
page = 1

url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    requests = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(requests)
    content = response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>(.*?)</a>.*?<div.*?'+
                         'content">(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        haveImage = re.search("img",item[3])
        if not haveImage:
            print(item[0],item[1],item[2],item[3],item[4])
    # print(response.read())
except urllib.request.URLError:
   print('错误')


# for item in items:
#     print(item[0],item[1],item[2],item[3],item[4])

# print('////////////////////////////////////////////////////////////////////////////////////////')












