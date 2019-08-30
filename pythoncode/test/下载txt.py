import re
import requests
import json
from lxml import etree
from subprocess import call  
  
class Down_txt:
  
    def __init__(self):
        # self.list_url = []
        self.id = []
        self.url=[]
        self.down_url=[]
        self.headers = {
            "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        }
  
    def get_id(self):
        for url in self.url:        
            response = requests.get(url, headers=self.headers)
            html = response.text
            html_etree = etree.HTML(html)
            title = html_etree.xpath('//div[@id="articlelist"]/ul[position()>1]/li/span[2]/a/@href')
            for each in title:            	
                regex = re.compile(r"\d+")
                ids = re.findall(regex, each)
                for each in ids:
                    self.id.append(each)

    def get_url(self):
        '''
        批量获取链接
        ''' 
        for i in range(1, 3):
            url = "http://www.jimixs.com/top/3-12-%s.html" % i
            self.url.append(url)

    def mk_url(self):
        for each in self.id:
            strs="http://www.jimixs.com/down.php?bid=%s&name=NULL&backup=1" %each

            self.down_url.append(strs)

    def down_txt(self):

        for down_url in self.down_url:
            idm = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'
            call([idm, '/d',down_url, '/a'])
            
		call([idm, '/s'])


if __name__ == '__main__':

    
    txt=Down_txt()
    txt.get_url()
    txt.get_id()
    txt.mk_url()
    txt.down_txt()



