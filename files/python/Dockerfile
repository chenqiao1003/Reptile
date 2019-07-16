FROM python:3.6
MAINTAINER chenqiao "chenqiao1003@126.com"
# 设置时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ENV PATH /usr/local/bin:$PATH

COPY ./code /code 

RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install html5lib
RUN pip install lxml

WORKDIR /code

# CMD ["/bin/bash", "python -V"]