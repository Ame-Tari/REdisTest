from redis import StrictRedis



if __name__ == '__main__':
    # 创建一个StricRedis对象,链接redis数据库
    try:
        sr = StrictRedis()
        # 添加一个key,为name, value itheima
        res = sr.set('name', 'itheima')
        # 修改name的值
        res = sr.set('name', 'none')
        # 获取name的值
        res = sr.get('name')
        print(res)
    except Exception as e:
        print(e)