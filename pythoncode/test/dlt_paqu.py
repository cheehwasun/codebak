from lxml import etree

# dirs=['ssq_03001-08001.html','ssq_08002-13001.html','ssq_13002-19067.html']
dirs=['dlt_07001-12001.html','dlt_12002-19067.html']

for file in dirs:

    html=etree.parse(file,etree.HTMLParser())
    serial_number=html.xpath('//table[@id="chartsTable"]/tbody/tr[position()>2 and position()<last()-6]/td[@align="center"]/text()')
    redball=html.xpath('//table[@id="chartsTable"]/tbody/child::*/td[contains(@class,"chartBall01")]/text()')
    blueball=html.xpath('//table[@id="chartsTable"]/tbody/child::*/td[contains(@class,"chartBall02")]/text()')

    redballs=[]
    for i in range(0,len(redball),5):
        redballs.append(redball[i:i+5])

    blueballs=[]
    for i in range(0,len(blueball),2):
        blueballs.append(blueball[i:i+2])


    with open('dlt.txt','a+') as f:
        for i in range(len(serial_number)):
            str1=serial_number[i]+": "+" ".join(redballs[i])+" - "+" ".join(blueballs[i])+"\r\n"
            f.writelines(str1)



