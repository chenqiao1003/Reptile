dockerFile手动搭建nginx php python容器环境环境
============================

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

