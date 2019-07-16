FROM nginx:1.12
MAINTAINER chenqiao "chenqiao1003@126.com"
# set timezome
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone