### application.yml常规配置

``````
server:
  port: 8090
  servlet:
    context-path: /

spring:
  datasource:
    driver-class-name: com.mysql.cj.jdbc.Driver
    url: jdbc:mysql://localhost:3306/cs?useUnicode=true&characterEncoding=UTF-8&useSSL=false&serverTimezone=Asia/Shanghai&allowPublicKeyRetrieval=true
    username: root
    password: root

  security:
    user:
      name: test
      password: qwerty

  redis:
    host: 127.0.0.1
    port: 6379
``````



