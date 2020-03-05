from redis import Redis
red = Redis(host='127.0.0.1',port=6379)    # 连接redis数据库
red.set("wt", 12)