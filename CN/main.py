# 作者John Stonty QQ:1844063767 遇到问题欢迎联系

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import config # 导入配置文件

# 注意！有必要的话请自行Google如何selenium指定chromedrive路径
# 以下内容适用于与chromedrive在同路径 如有不同需求请酌情修改

# 设置浏览器启动参数
options = Options()
options.add_argument('--headless') #让chrome在headless模式下工作
options.add_argument("--window-size=1440,900") #设置chrome访问的分辨率
options.add_argument('--disable-gpu') #禁用gpu以防出现bug(来自官方文档)
options.add_argument('--hide-scrollbars') #隐藏滚动条以防止一些页面get不到
options.add_argument('--blink-settings=imagesEnabled=false') #禁用图片以加快加载速度
options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"') #设置chrome UA以访问到正确版式的目标站点(防止不同浏览器跳转至不同站点导致无法找到元素)

# 定义初始化过程 传入变量YouTube直播间ID
def init(targetID): 
    driver = webdriver.Chrome(chrome_options=options) #定义浏览器并使浏览器应用参数(写在全局里的话其他文件import的时候就会启动selenium的监听服务)
    wait = WebDriverWait(driver,300,0.01,None) #定义显示等待的过程[目标为driver(上文定义的),在300秒内每10ms检查一次是否检查到元素,如果检查到了就停止等待并继续,如果未检查到则抛出None]
    driver.get('http:\\www.gmail.com') #调用chrome访问网站http:\\www.gmail.com以到达Google账户登陆页
    driver.find_element_by_id('identifierId').send_keys(config.username) #用id查找用户名输入框元素并输入预设的用户名
    driver.find_element_by_css_selector('[class="RveJvd snByac"]').click() #用class查找下一步按钮元素并点击
    #wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
    driver.implicitly_wait(1) #这边一定要用隐式等待暂停1s...上面注释的显式等待会带来一个很玄学的bug:有时可以而有时会导致找不到密码输入框元素
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(config.password) #用xpath查找密码输入框元素并输入预设的密码
    driver.find_element_by_css_selector('[class="RveJvd snByac"]').click() #用class查找下一步(完成)按钮元素并点击
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="loading"]/div[2]/div[4]')))  #调用显式等待过程等待gmail收件箱加载完毕(确认账户已登录)(通过xpath)
    driver.get('https://www.youtube.com/watch?v='+targetID) #通过传入变量访问指定的YouTube直播间
    wait.until(EC.presence_of_element_located((By.ID, "chatframe"))) #调用显式等待过程等待在指定的YouTube直播间的实时聊天加载完毕(通过id)
    driver.switch_to_frame("chatframe") #切换到实时聊天的frame
    return "inited" #返回成功信息...可以用while!=true等待成功

# 定义向YouTube直播间发送指定消息的过程 传入变量要发送的消息
def sendMessages(Message):
    driver = webdriver.Chrome(chrome_options=options) #定义浏览器并使浏览器应用参数(写在全局里的话其他文件import的时候就会启动selenium的监听服务)
    driver.find_element_by_xpath('//div[@id="input"]').send_keys(str(Message)) #用xpath查找实时聊天输入框元素并输入传入的消息(别问我为什么要str消息值 鬼知道用这个模块的人是怎么想的 以免他们的时候碰到未知的bug)
    driver.find_element_by_xpath('//yt-icon-button[@class="style-scope yt-button-renderer"]').click() #用xpath查找发送按钮元素并点击
    # print("done.") #这是调试信息 返回已完成发送指定消息的过程

# 定义停止监听&关闭headless chrome的过程
def stop():
    webdriver.Chrome(chrome_options=options).quit() #停止监听&关闭headless chrome(我觉得这里只用一次就没有必要再用变量定义浏览器了)