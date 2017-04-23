#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore import client
from aliyunsdksts.request.v20150401 import AssumeRoleRequest

# 构建一个 Aliyun Client, 用于发起请求
# 构建Aliyun Client时需要设置AccessKeyId和AccessKeySevcret
# STS是Global Service, API入口位于杭州, 这里Region填写"cn-hangzhou"
clt = client.AcsClient('Foyg239CwfwKh6VQ','gnDXbtD95v2ZxsYXk9qAA4gNfIXrj4','cn-hangzhou')

# 构造"AssumeRole"请求
request = AssumeRoleRequest.AssumeRoleRequest()
# 指定角色
request.set_RoleArn('acs:ram::1756420699686453:role/jfwwriter')
# 设置会话名称，审计服务使用此名称区分调用者
request.set_RoleSessionName('jfw-001')

# 发起请求，并得到response
response = clt.do_action(request)

print response
