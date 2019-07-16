#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, os, re
from bs4 import BeautifulSoup as bs


class _filterHtml(object):

    def __init__(self):
        self.debug = 0

    def _dealJsonStr(self, str):
        str = str.replace(">", "&gt;")
        str = str.replace("<", "&lt;")
        str = str.replace(" ", "&nbsp;")
        str = str.replace("\"", "&quot;")
        str = str.replace("\'", "&#39;")
        str = str.replace("\\", "\\\\")
        str = str.replace("\n", "\\n")
        str = str.replace("\r", "\\r")
        return str

    def _dealStr(self, str):
        str = str.replace("\\n", "")
        str = str.replace("\\r", "")
        str = str.replace("\t", "")
        return str

    def filter_tags(self, htmlstr):
        # 先过滤CDATA
        re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
        re_script = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
        re_style = re.compile('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
        re_br = re.compile('<br\s*?/?>')  # 处理换行
        re_h = re.compile('</?\w+[^>]*>')  # HTML标签
        re_comment = re.compile('<!--[^>]*-->')  # HTML注释
        s = re_cdata.sub('', htmlstr)  # 去掉CDATA
        s = re_script.sub('', s)  # 去掉SCRIPT
        s = re_style.sub('', s)  # 去掉style
        s = re_br.sub('\n', s)  # 将br转换为换行
        s = re_h.sub('', s)  # 去掉HTML 标签
        s = re_comment.sub('', s)  # 去掉HTML注释
        # 去掉多余的空行
        blank_line = re.compile('\n+')
        s = blank_line.sub('\n', s)
        s = self.replaceCharEntity(s)  # 替换实体
        return s

    def replaceCharEntity(self, htmlstr):
        CHAR_ENTITIES = {'nbsp': ' ', '160': ' ',
                         'lt': '<', '60': '<',
                         'gt': '>', '62': '>',
                         'amp': '&', '38': '&',
                         'quot': '"', '34': '"', }

        re_charEntity = re.compile(r'&#?(?P<name>\w+);')
        sz = re_charEntity.search(htmlstr)
        while sz:
            entity = sz.group()  # entity全称，如&gt;
            key = sz.group('name')  # 去除&;后entity,如&gt;为gt
            try:
                htmlstr = re_charEntity.sub(CHAR_ENTITIES[key], htmlstr, 1)
                sz = re_charEntity.search(htmlstr)
            except KeyError:
                # 以空串代替
                htmlstr = re_charEntity.sub('', htmlstr, 1)
                sz = re_charEntity.search(htmlstr)
        return htmlstr


def getBaiduAnswer():
    f = open("tags.txt")
    i = 0
    for line in f:
        # 单次脚本读取关键词的个数
        if i >= 1:
            exit()

        # 关键词去首位空格，拼接url地址
        tagsInfo = line.strip()

        if tagsInfo == '':
            continue

        newUrl = url = "https://zhidao.baidu.com/search?ct=17&pn=0&tn=ikaslist&rn=10&fr=wwwt&word=%s" % str(tagsInfo)

        print("问题：")
        print(tagsInfo)
        print ("---------------------------")

        fp = requests.get(newUrl)

        soup = bs(fp.content, "html.parser")
        allHtml = soup.find_all(name='dd', attrs={'class': 'dd answer'})

        h = 1
        for row in allHtml:
            print("答案%d" % h)
            print(row.text)

            h +=1
        exit()

        i += 1

    f.close()


def main():
    print("1234")
    # getBaiduAnswer()


if __name__ == '__main__':
    main()
