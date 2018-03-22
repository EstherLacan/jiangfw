# -*- coding: UTF-8 -*-

import MySQLdb


class DbFunctions(object):
    """
    数据库连接
    """

    def __init__(self, server, username, password, dbname):
        self.server = server
        self.username = username
        self.password = password
        self.dbname = dbname
        self.db = None
        self.cur = None

    def connection_open(self):
        self.db = MySQLdb.connect(host=self.server, user=self.username, passwd=self.password, db=self.dbname)
        self.cur = self.db.cursor()

    def connection_close(self):
        self.db.close()

    def mysql_qry(self, sql, bool):  # 1 for select and 0 for insert update delete
        self.connection_open()
        try:
            self.cur.execute(sql)
            if bool:
                return self.cur.fetchall()
            else:
                self.db.commit()
                return True
        except MySQLdb.Error, e:
            try:
                print "Mysql Error:- " + str(e)
            except IndexError:
                print "Mysql Error:- " + str(e)
        self.connection_close()

    def mysql_insert(self, table, fields, values):
        sql = "INSERT INTO " + table + " (" + fields + ") VALUES (" + values + ")";
        return self.mysql_qry(sql, 0)

    def mysql_update(self, table, values, conditions):
        sql = "UPDATE " + table + " SET " + values + " WHERE " + conditions
        return self.mysql_qry(sql, 0)

    def mysql_delete(self, table, conditions):
        sql = "DELETE FROM " + table + " WHERE " + conditions
        return self.mysql_qry(sql, 0)

    def mysql_select(self, table):
        sql = "SELECT * FROM " + table
        return self.mysql_qry(sql, 1)

    def insert_by_many(self, tablname, rows):
        try:
            # sql = 'INSERT INTO t_uba_permission_list values(%s,%s,%s)'
            # 批量插入
            sql = 'INSERT INTO ' + tablname + ' values(%s,%s,%s)'
            self.connection_open()
            self.cur.executemany(sql, rows)
            self.db.commit()
        except Exception as e:
            print e
            self.db.rollback()

        self.connection_close()
        print '[insert_by_many executemany] total:', len(rows)


        # db = DbFunctions("100.109.35.184", "root", "Wad_1234!", "uba_db")
        # result = db.mysql_qry("",1)
