import time
import random
import uuid
import string

def randomDate(start, end):
    s = tuple(map(int, start.split("-")))
    e = tuple(map(int, end.split("-")))

    a1 = s + (0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（2020-01-01 00：00：00）
    a2 = e + (23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（2021-08-31 23：59：59）

    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳

    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    return time.strftime("%Y-%m-%d", date_touple)  # 将时间元组转成格式化字符串（2020-05-21）

def randomDatetime(start, end):
    s = tuple(map(int, start.split("-")))
    e = tuple(map(int, end.split("-")))

    a1 = s + (0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（2020-01-01 00：00：00）
    a2 = e + (23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（2021-08-31 23：59：59）

    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳

    t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
    date_touple = time.localtime(t)  # 将时间戳生成时间元组
    return time.strftime("%Y-%m-%d %H:%M:%S", date_touple)  # 将时间元组转成格式化字符串（2020-05-21）

def randomPrice(lower, upper):
    return float("{:.2f}".format(random.uniform(float(lower), float(upper))))

#    10: '猫', 20: '猫粮', 30: '猫砂', 40: '生活用品', 50: '零食', 60: '健康', 70: '清洁'
#   51: '罐头', 52: '营养品', 53: '其它（零食）'
#   61: '医疗', 62: '洗澡', 63: '疫苗', 64: '驱虫', 65: '绝育'
#   71: '清洁剂', 72: '消毒剂', 73: '其它（清洁）'
def randomCategory():
    cate = random.randint(1, 7) * 10

    if (cate == 50):
        subCate = random.randint(51, 53)
    elif (cate == 60):
        subCate = random.randint(61, 65)
    elif (cate == 70):
        subCate = random.randint(71, 73)
    else:
        subCate = cate


    return {"cate": cate, "subCate": subCate}

def randomGoodsId():
    return str(uuid.uuid4())

def randomUserId():
    # return uuid.uuid4()
    return "19231d6b-24d4-40c1-a26f-500b2a1ab525"

def randomCount(count):
    return random.randint(1, count)

def randomIsConsumable():
    return random.randint(0, 1)

def randomGoodsName():
    return ''.join(random.sample(string.ascii_letters + string.digits, random.randint(5, 15)))
