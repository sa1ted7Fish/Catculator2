import time

from DataGen import DataGenerator
from RandomData import *

dg = DataGenerator()

rawSql = "insert into warehouse (" \
         "goods_id, " \
         "user_id, " \
         "goods_name, " \
         "category, " \
         "sub_category, " \
         "unit_price, " \
         "count, " \
         "total_price, " \
         "purchase_date, " \
         "is_consumable, " \
         "create_time, " \
         "update_time" \
         ") values (" \
         "{goodsId}, " \
         "{userId}, " \
         "{goodsName}, " \
         "{category}, " \
         "{subCategory}, " \
         "{unitPrice}, " \
         "{count}, " \
         "{totalPrice}, " \
         "{purchaseDate}, " \
         "{isConsumable}, " \
         "{createTime}, " \
         "{updateTime})"

start = "2020-01-01"
end = "2024-12-31"
c = 0
sum = 37

t0 = time.time()

for i in range(sum):
    cate = randomCategory()
    createTime = randomDatetime(start, end)
    unitPrice = randomPrice(5, 80)
    count = random.randint(1, 10)
    totalPrice = unitPrice * count

    sql = rawSql.format(
        goodsId="\'" + randomGoodsId() + "\'",
        userId="\'" + randomUserId() + "\'",
        goodsName="\'" + randomGoodsName() + "\'",
        category=cate['cate'],
        subCategory=cate['subCate'],
        unitPrice=unitPrice,
        count=count,
        totalPrice=totalPrice,
        purchaseDate="\'" + randomDate(start, end) + "\'",
        isConsumable=randomIsConsumable(),
        createTime="\'" + createTime + "\'",
        updateTime="\'" + createTime + "\'"
    )

    ret = dg.insert(sql)

    if (type(ret) == int):
        c += ret
    else:
        print(ret)
print(time.time() - t0)
print(c)