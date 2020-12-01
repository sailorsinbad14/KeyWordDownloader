# KeyWordDownloader
输入想要的关键词和参数后自动下载阿里数据管家的关键词表
使用说明:
1. 确保已有python3环境
2. MacOS用户:
  方法一: 打开终端, 输入: python + 空格 + /此脚本路径/KeywordListDownloader.py 回车运行即可
  方法二: 打开终端, 输入 chmod +x /此脚本路径/KeywordListDownloader.py, 回车运行
          接着系统提示会要管理员权限, 同意后, 将KeywordListDownloader.py 改为 KeywordListDownloader.command
          双击打开KeywordListDownloader.command 即可自动运行脚本, 无需再通过终端输入指令 (节省一个步骤)
3. Windows用户:
    因为个人时间有限, 就大致介绍一下:
    同样, 打开命令提示符 (CMD), 输入: python + 空格 + /此脚本路径/KeywordListDownloader.py 回车运行即可

PS:以后我还想把这个脚本做成可以自动从csv表格文件里批量提取关键词进行自动下载, 效率进一步提高. 等有时间再来填坑.
以上如有不懂的地方可以加我微信16624702595, 问之前请先自行谷歌, 我没有时间回答可以在网上找的到答案的问题.谢谢!

#TitleGenerator
自动将品牌词, 营销词, 属性词, 核心词, 使用场景词等合并成标题
具体做法如下:
1. 将各种所需词汇按照种类和顺序置入表格中, 将表格保存为 "rawData.cvs", 格式可参考这里带的 rawData.to_csv
2. 在此文件夹打开终端/命令提示符, 输入 python titleGenerator.py 或将其拖入, 点击回车 运行脚本
3. 脚本运行后会自动在同一目录下生成/覆盖 名为 export.csv 的表格
4. 用Excel或其他表格查看工具打开此 export.csv 文件即可查看生成的标题了. 这里要注意因为Excel的原因有些特殊符号可能被转换成乱码, 建议在记事本等工具打开, 将编码格式改为UTF-8即可
