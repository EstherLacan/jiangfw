# -*- coding: UTF-8 -*-

from my_sql_conn import DbFunctions

"""
权限：66
预置权限表数据
"""



white_list = 'admin'
white_list_array = white_list.split(",")
white_list_array = sorted(set(white_list_array), key=white_list_array.index)  # 去重
print(white_list_array)
print 'white_list_array size is ' + str(len(white_list_array))


def initAllAppKey():
    """
    预置所有appkey权限
    """
    appkeys = queryAppKey()
    appkey_list = []
    for white_user in white_list_array:
        for appkey in appkeys:
            appkey_row = []
            appkey_row.append(white_user)
            appkey_row.append(appkey[0])
            appkey_row.append("20180320000000")
            appkey_list.append(appkey_row)
    insertPermissionList(appkey_list)
    print 3


def queryAppKey():
    """
    查询appkey
    """
    db = DbFunctions("localhost", "root", "Root@123", "db")
    result = db.mysql_qry("select appkey from table", 1)
    appkey_list = []
    for app_key in result:
        if app_key not in appkey_list:
            appkey_list.append(app_key)
    print(appkey_list)
    print 'result size is ' + str(len(appkey_list))
    return appkey_list


def insertPermissionList(rows):
    """
    插入权限
    """
    db = DbFunctions("localhost", "root", "Root@123", "db")
    db.insert_by_many('table', rows)
    # print(result)


if __name__ == '__main__':
    initAllAppKey()
