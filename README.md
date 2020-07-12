# Smart Manager Api

`python3` | `flask`

### 依赖包

- python-dotenv
- flask_restx
- flask-sqlalchemy

### 命令行

```shell
flask --help
```

### 运行

1.初始化数据库
```shell
flask db init
```
2.创建`admin`角色用户
```shell
flask db create-admin {name} {username} {password}
```
