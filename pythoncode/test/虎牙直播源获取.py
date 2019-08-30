import re
import requests
import json
from lxml import etree
  
  
class Huya_live:
  
    def __init__(self):
        # self.list_url = []
        self.id = []
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        }
  
    def get_m3u8(self):
        for id in self.id:
            url = "https://www.huya.com/" + id
            response = requests.get(url, headers=self.headers)
            html = response.text
            # title = re.findall("<title>.*|\r\n</title>", html)[0]
            html_etree = etree.HTML(html)
            title = html_etree.xpath('//h1[@id="J_roomTitle"]/text()')[0]
            title = re.sub("<title>|</title>|\r|\n", "", title)
            regex = re.compile(r"{\"status\"(.*)};")  
            # {"status":200,"msg":"","data":[] }; 正则匹配找到这个字符串
            strs = re.findall(regex, html)
  
            try:
                a = list(strs[0])
                a[4] = "{"
                str = "".join(a[4:])
                #处理成字典类型的字符串｛"data":[...] }
                str = json.loads(str)
                # 处理成json方便直接查找
                streamName = "/" + str['data'][0]['gameStreamInfoList'][1]['sStreamName']
                m3u8 = str['data'][0]['gameStreamInfoList'][1]['sHlsUrl']
                # flv = str['data'][0]['gameStreamInfoList'][1]['sFlvUrl']
                print(title)
                print(m3u8 + streamName + ".m3u8")
            except:
                print(url, "直播间没有人直播噢, 不信你去看看 网址为%s" % url)
                continue

            # self.put_write(m3u8 + streamName + ".m3u8", title)

    def get_roomId(self):
        '''
        批量获取房间号 
        ''' 
        for i in range(1, 5):
            yiqikan_Api = "https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=2135&tagAll=0&page=%d" % i
            # xingshow_api = "https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1663&tagAll=0&page=%d" % i
            response = requests.get(yiqikan_Api, headers=self.headers).text
            html = json.loads(response)
            ids = html['data']['datas']
            for id in ids:
                self.id.append(id['profileRoom'])

    def room_Id(self,str):
        self.id.append(str)
  
    def put_write(self, m3u8, title):
        str = title + "***" * 20 + m3u8 + "\n"
        with open("./虎牙直播源.txt", 'a+') as f:
            f.write(str)
  
  
if __name__ == '__main__':
    
    while True:
        room_id=input("输入房间号：")        
        huya = Huya_live()
        huya.room_Id(room_id)    
        huya.get_m3u8()