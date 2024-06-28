# Hello, Interviewer

## 动手 
容器环境存在的问题，基础的python:3.9-alpine是不提供make命令的，有两种方式可以解决
1. 在基础镜像中安装make工具；
2. 修改Makefile如文件所示，直接使用python命令去执行单元测试(本次使用的方法)。

## 思考题
1. 准备好的单元测试存在问题，只判断了返回的字符串的长度，并没有判断不同的时间范围是否能够返回正确的字符串。
2. 增加了返回值不能为空的测试以及不同时间范围内的测试用例，命名更规范。

## 运行结果
```bash
my-ubuntu 23:00:01:~/code/ds-recruit-main/python$ sudo make dev-tests
[sudo] lb 的密码： 
docker-compose build
[+] Building 0.1s (6/6) FINISHED                                                                                                                                                                                     docker:default
 => [recruit internal] load build definition from Dockerfile                                                                                                                                                                   0.0s
 => => transferring dockerfile: 113B                                                                                                                                                                                           0.0s
 => [recruit internal] load metadata for python:3.9-alpine                                                                                                                               0.0s
 => [recruit internal] load .dockerignore                                                                                                                                                                                      0.0s
 => => transferring context: 2B                                                                                                                                                                                                0.0s
 => [recruit 1/2] FROM python:3.9-alpine                                                                                                                                                 0.0s
 => CACHED [recruit 2/2] WORKDIR /srv                                                                                                                                                                                          0.0s
 => [recruit] exporting to image                                                                                                                                                                                               0.0s
 => => exporting layers                                                                                                                                                                                                        0.0s
 => => writing image sha256:6a305d00d932d981e399edfc9b2917d3a8c9e68a239318b81834bfd04c6a2784                                                                                                                                   0.0s
 => => naming to docker.io/recruit/python                                                                                                                                                                                      0.0s
docker-compose --compatibility up -d --remove-orphans
 Container recruit_python  Running
docker-compose exec recruit python -m unittest tests/*.py
.....
----------------------------------------------------------------------
Ran 5 tests in 0.002s

OK
```