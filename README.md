# DatabaseExp
暂时只搭建了大概的形状，功能均未实现。 
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
|  新值订单     |  html界面施工中，功能未实现   | 
|  订单修改   |   html界面未实现，功能未实现  | 
|   已有订单查看   |  html界面未实现，功能未实现   | 
|   已有订单查询   |  html界面未实现，功能未实现   | 
