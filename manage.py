# coding:utf-8
from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate

from ihone import create_app,db


# 创建app,develop配置
app=create_app("develop")

# 创建manager对象
manager=Manager(app)

# 创建migrate对象关联应用程序类对象app和数据库管理类对象db
Migrate(app,db)

# 将MigrateCommand命令加入到manager对象中,这样就可以在命令行中进行数据库迁移的相关命令.
manager.add_command("db",MigrateCommand)


if __name__ == '__main__':
    manager.run()
