#!/usr/bin/env python
url1='https://hz-mydata.alibaba.com/self/excelDownload.do?&iName=excel/download/vip/kwIndex/searchWords&terminalType='

url2 = '&dateType=' #7d 30d

url3 = '&countryId=' #US

url4 = '&queryRaw='

url_end='&nd='

##TESTING##
# 终端  MOBILE, MOB, MO, MB, YD, Mobile, MBL, YIDONG, Other


#TESTED OK#
 # 日期 7天 30天
 # 空格 %20
 # 终端  PC,
 #地区 US, PE 使用2位国家码

endWhile=''
while (endWhile ==''):

# 输入
    inputText = input("输入关键词:\n")
    # inputTerminal = input ('Enter Terminal Type:\n')
    inputTerminal= 'TOTAL'

    inputDays = input('时间范围 (输入 7d 或 30d):\n')
    inputCountryID = input('输入ISO-3166 2位国家码 (例如美国为US, 全部国家填 TOTAL):\n')

    newText = inputText.replace(' ', '%20')

    url_combined = url1 + inputTerminal + url2 + inputDays + url3 + inputCountryID + url4 + newText + url_end + inputDays
    print(url_combined)

    import webbrowser
    webbrowser.open(url_combined)
    endWhile = input('按回车继续, 退出请按其他键!')
