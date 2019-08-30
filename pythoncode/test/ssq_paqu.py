from lxml import etree

dirs=['ssq_03001-08001.html','ssq_08002-13001.html','ssq_13002-19067.html']
# dirs=['dlt_07001-12001.html','dlt_12002-19067.html']

for file in dirs:

    html=etree.parse(file,etree.HTMLParser())
    serial_number=html.xpath('//tbody[@id="tdata"]/child::*/td[@align="center"]/text()')
    redballs=html.xpath('//tbody[@id="tdata"]/child::*/td[contains(@class,"chartBall01")]/text()')
    blueball=html.xpath('//tbody[@id="tdata"]/child::*/td[contains(@class,"chartBall02")]/text()')

    redball=[]
    for i in range(0,len(redballs),5):
        redball.append(redballs[i:i+5])

    with open('ssq.txt','a+') as f:
        for i in range(len(serial_number)):
            str1=serial_number[i]+": "+" ".join(redball[i])+" - "+blueball[i]+"\r\n"
            f.writelines(str1)



