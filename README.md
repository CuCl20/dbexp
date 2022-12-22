# DatabaseExp
实现了部分功能。 
## 配置方式 
1. 将项目pull到本地
2. 在本地mysql创建用于本项目的空数据库，并在settings.py中配置
3. 在项目根目录执行命令用于数据迁移
```
python manage.py makemigrations
python manage.py migrate
```
4. 在项目根目录执行命令，运行项目
```
python manage.py runserver
```
环境需求在requirements.txt中。 

| 待实现功能     |      当前状态      | 
| ---           | ---         | 
|  过期未支付订单处理     |  功能未实现   | 
