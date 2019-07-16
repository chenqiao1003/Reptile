# 简单的网页爬虫
============================
## pyhon 爬取百度页面内容 
```bash
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, os, re, sys, json
from bs4 import BeautifulSoup as bs

class findBaiduAQ(object):

    def __init__(self, problem=''):
        self.debug = 0
        self.problem = problem

    def getBaiduAnswer(self):

        # 关键词去首位空格，拼接url地址
        tagsInfo = self.problem.strip()

        if tagsInfo == '':
            exit()

        newUrl = url = "https://zhidao.baidu.com/search?ct=17&pn=0&tn=ikaslist&rn=10&fr=wwwt&word=%s" % str(tagsInfo)

        fp = requests.get(newUrl)

        soup = bs(fp.content, "html.parser")
        allHtml = soup.find_all(name='dd', attrs={'class': 'dd answer'})

        data = []
        for row in allHtml:
            data.append(str(row))

        print json.dumps(data, ensure_ascii=False)

def main(flag=''):
    re = findBaiduAQ(problem=flag)
    re.getBaiduAnswer()


if __name__ == '__main__':
    flag = str(sys.argv[1])
    main(flag)

```

## 搭建环境
> 运行
```bash
cd Reptile/files
docker-compse up -d
```

> 容器说明
- nginx 独立一个容器
- php + python2.7 + compose 共用一个容器


> 版本说明
- PHP: php:7.2-fpm
- Nginx: nginx:1.12
- Docker-compose: 最新版
- Python: python2.7


> 宿主机端口说明
- 9011 php容器
- 6011 nginx容器

