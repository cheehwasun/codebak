#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-21 13:24:08
# @Author  : kakarot (kakarotsun@163.com)
# @Link    : http://example.org
# @Version : $Id$

import pymongo
import datetime


def get_db():
    # 建立连接
    client = pymongo.MongoClient(host="10.244.25.180", port=27017)
    db = client['example']
    # 或者 db = client.example
    return db


def get_collection(db):
    # 选择集合（mongo中collection和database都是延时创建的）
    coll = db['informations']
    print db.collection_names()
    return coll


def insert_one_doc(db):
    # 插入一个document
    coll = db['informations']
    information = {"name": "quyang", "age": "25"}
    information_id = coll.insert(information)
    print information_id


def insert_multi_docs(db):
    # 批量插入documents,插入一个数组
    coll = db['informations']
    information = [{"name": "xiaoming", "age": "25"},
                   {"name": "xiaoqiang", "age": "24"}]
    # coll.insert_many(list())
    information_id = coll.insert(information)

    print information_id


def get_one_doc(db):
    # 有就返回一个，没有就返回None
    coll = db['informations']
    print coll.find_one()  # 返回第一条记录
    print coll.find_one({"name": "quyang"})
    print coll.find_one({"name": "none"})


def get_one_by_id(db):
    # 通过objectid来查找一个doc
    coll = db['informations']
    obj = coll.find_one()
    obj_id = obj["_id"]
    print "_id 为ObjectId类型，obj_id:" + str(obj_id)

    print coll.find_one({"_id": obj_id})
    # 需要注意这里的obj_id是一个对象，不是一个str，使用str类型作为_id的值无法找到记录
    print "_id 为str类型 "
    print coll.find_one({"_id": str(obj_id)})
    # 可以通过ObjectId方法把str转成ObjectId类型
    from bson.objectid import ObjectId

    print "_id 转换成ObjectId类型"
    print coll.find_one({"_id": ObjectId(str(obj_id))})


def get_many_docs(db):
    # mongo中提供了过滤查找的方法，可以通过各种条件筛选来获取数据集，还可以对数据进行计数，排序等处理
    coll = db['informations']
    # ASCENDING = 1 升序;DESCENDING = -1降序;default is ASCENDING
    for item in coll.find().sort("age", pymongo.DESCENDING):
        print item

    count = coll.count()
    print "集合中所有数据 %s个" % int(count)

    # 条件查询
    count = coll.find({"name": "quyang"}).count()
    print "quyang: %s" % count


def clear_all_datas(db):
    # 清空一个集合中的所有数据
    db["informations"].remove()


#唯一的字段 index
result=db.t1.create_index([('index',pymongo.ASCENDING)],unique=True)



# 查询选择器

# 比较

# 有关不同BSON类型值的比较，请参阅指定的BSON比较顺序。

# 名称  描述
# $eq 匹配等于指定值的值。
# $gt 匹配大于指定值的值。
# $gte    匹配大于或等于指定值的值。
# $in 匹配数组中指定的任何值。
# $lt 匹配小于指定值的值。
# $lte    匹配小于或等于指定值的值。
# $ne 匹配所有不等于指定值的值。
# $nin    不匹配数组中指定的值。
# 逻辑

# 名称  描述
# $and    用逻辑连接查询子句AND将返回符合两个子句条件的所有文档。
# $not    颠倒查询表达式的效果并返回与查询表达式不匹配的文档。
# $nor    用逻辑连接查询子句NOR返回所有不符合两个子句的文档。
# $or 用逻辑连接查询子句OR将返回符合任一子句条件的所有文档。
# 元素

# 名称  描述
# $exists 匹配具有指定字段的文档。
# $type   如果字段是指定的类型，则选择文档。
# 评估

# 名称  描述
# $mod    对字段的值执行模运算并选择具有指定结果的文档。
# $regex  选择值与指定正则表达式匹配的文档。
# $text   执行文本搜索。
# $where  匹配满足JavaScript表达式的文档。
# 地理空间

# 名称  描述
# $geoIntersects  选择与GeoJSON几何体相交的几何体。该2dsphere索引支持 $geoIntersects。
# $geoWithin  选择边界GeoJSON几何体中的几何体。该2dsphere和2D索引支持 $geoWithin。
# $near   返回接近点的地理空间对象。需要一个地理空间索引。该2dsphere和2D索引支持 $near。
# $nearSphere 返回接近球体上一个点的地理空间对象。需要一个地理空间索引。该2dsphere和2D索引支持 $nearSphere。
# 数组

# 名称  描述
# $all    匹配包含查询中指定的所有元素的数组。
# $elemMatch  如果数组字段中的元素匹配所有指定的$elemMatch条件，则选择文档。
# $size   如果数组字段是指定的大小，则选择文档。
# 按位

# 名称  描述
# $bitsAllClear   匹配一组位位置均具有值的数值或二进制值0。
# $bitsAllSet 匹配一组位位置均具有值的数值或二进制值1。
# $bitsAnyClear   匹配数值或二进制值，其中一组位位置中的任何位具有值0。
# $bitsAnySet 匹配数值或二进制值，其中一组位位置中的任何位具有值1。
# 评论

# 名称  描述
# $comment    向查询谓词添加注释。
# 投影算子

# 名称  描述
# $   投影与查询条件匹配的数组中的第一个元素。
# $elemMatch  投影符合指定$elemMatch条件的数组中的第一个元素。
# $meta   投影在$text操作过程中分配的文档分数。
# $slice  限制从数组投影的元素的数量。支持跳过和限制片。



查看聚集的字段
>> > db.Account.find_one({}, {"UserName": 1, "Email": 1})
{u'UserName': u'libing', u'_id': ObjectId(
    '4ded95c3b7780a774a099b7c'), u'Email': u'libing@35.cn'}


>> > db.Account.find_one({}, {"UserName": 1, "Email": 1, "_id": 0})
{u'UserName': u'libing', u'Email': u'libing@35.cn'}


查看聚集的多条记录

>> > for item in db.Account.find():
    item


>> > for item in db.Account.find({"UserName": "libing"}):
    item["UserName"]


查看聚集的记录统计
>> > db.Account.find().count()


>> > db.Account.find({"UserName": "keyword"}).count()


聚集查询结果排序
>> > db.Account.find().sort("UserName") - -默认为升序
>> > db.Account.find().sort("UserName", pymongo.ASCENDING) - -升序
>> > db.Account.find().sort("UserName", pymongo.DESCENDING) - -降序


聚集查询结果多列排序

>> > db.Account.find().sort([("UserName", pymongo.ASCENDING), ("Email", pymongo.DESCENDING)])


添加记录

>> > db.Account.insert({"AccountID": 21, "UserName": "libing"})


修改记录

>> > db.Account.update({"UserName": "libing"}, {"$set": {"Email": "libing@126.com", "Password": "123"}})


1).update()命令

db.collection.update( criteria, objNew, upsert, multi )

criteria : update的查询条件，类似sql update查询内where后面的
objNew   : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的
upsert   : 这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。
multi    : mongodb默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。

例：
db.test0.update( { "count" : { $gt : 1 } } , { $set : { "test2" : "OK"} } ); 只更新了第一条记录
db.test0.update( { "count" : { $gt : 3 } } , { $set : { "test2" : "OK"} },false,true ); 全更新了
db.test0.update( { "count" : { $gt : 4 } } , { $set : { "test5" : "OK"} },true,false ); 只加进去了第一条
db.test0.update( { "count" : { $gt : 5 } } , { $set : { "test5" : "OK"} },true,true ); 全加进去了
db.test0.update( { "count" : { $gt : 15 } } , { $inc : { "count" : 1} },false,true );全更新了
db.test0.update( { "count" : { $gt : 10 } } , { $inc : { "count" : 1} },false,false );只更新了第一条

2).save()命令

db.collection.save( x )

x就是要更新的对象，只能是单条记录。

如果在collection内已经存在一个和x对象相同的"_id"的记录。mongodb就会把x对象替换collection内已经存在的记录，否则将会插入x对象，如果x内没有_id,系统会自动生成一个再插入。相当于上面update语句的upsert=true,multi=false的情况。

例：
db.test0.save({count:40,test1:"OK"}); #_id系统会生成
db.test0.save({_id:40,count:40,test1:"OK"}); #如果test0内有_id等于40的，会替换，否则插入。


mongodb的更新操作符：

1) $inc

用法：{ $inc : { field : value } }

意思对一个数字字段field增加value，例：

> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 16, "test1" : "TESTTEST", "test2" : "OK", "test3" : "TESTTEST", "test4" : "OK", "test5" : "OK" }

> db.test0.update( { "_id" : 15 } , { $inc : { "count" : 1 } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 17, "test1" : "TESTTEST", "test2" : "OK", "test3" : "TESTTEST", "test4" : "OK", "test5" : "OK" }

> db.test0.update( { "_id" : 15 } , { $inc : { "count" : 2 } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 19, "test1" : "TESTTEST", "test2" : "OK", "test3" : "TESTTEST", "test4" : "OK", "test5" : "OK" }

> db.test0.update( { "_id" : 15 } , { $inc : { "count" : -1 } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : "TESTTEST", "test2" : "OK", "test3" : "TESTTEST", "test4" : "OK", "test5" : "OK" }


2) $set

用法：{ $set : { field : value } }

就是相当于sql的set field = value，全部数据类型都支持$set。例：
> db.test0.update( { "_id" : 15 } , { $set : { "test1" : "testv1","test2" : "testv2","test3" : "testv3","test4" : "testv4" } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : "testv1", "test2" : "testv2", "test3" : "testv3", "test4" : "testv4", "test5" : "OK" }

3) $unset

用法：{ $unset : { field : 1} }

顾名思义，就是删除字段了。例：
> db.test0.update( { "_id" : 15 } , { $unset : { "test1":1 } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test2" : "testv2", "test3" : "testv3", "test4" : "testv4", "test5" : "OK" }

> db.test0.update( { "_id" : 15 } , { $unset : { "test2": 0 } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test3" : "testv3", "test4" : "testv4", "test5" : "OK" }

> db.test0.update( { "_id" : 15 } , { $unset : { "test3":asdfasf } } );
Fri May 14 16:17:38 JS Error: ReferenceError: asdfasf is not defined (shell):0

> db.test0.update( { "_id" : 15 } , { $unset : { "test3":"test" } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test4" : "testv4", "test5" : "OK" }

没看出field : 1里面的1是干什么用的，反正只要有东西就行。


4) $push

用法：{ $push : { field : value } }

把value追加到field里面去，field一定要是数组类型才行，如果field不存在，会新增一个数组类型加进去。例：

> db.test0.update( { "_id" : 15 } , { $set : { "test1" : ["aaa","bbb"] } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ "aaa", "bbb" ], "test4" : "testv4", "test5" : "OK" }

> db.test0.update( { "_id" : 15 } , { $push : { "test1": "ccc" } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ "aaa", "bbb", "ccc" ], "test4" : "testv4", "test5" : "OK" }

> db.test0.update( { "_id" : 15 } , { $push : { "test2": "ccc" } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ "aaa", "bbb", "ccc" ], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }

> db.test0.update( { "_id" : 15 } , { $push : { "test1": ["ddd","eee"] } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ "aaa", "bbb", "ccc", [ "ddd", "eee" ] ], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }
5) $pushAll

用法：{ $pushAll : { field : value_array } }

同$push,只是一次可以追加多个值到一个数组字段内。例：

> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ "aaa", "bbb", "ccc", [ "ddd", "eee" ] ], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }

> db.test0.update( { "_id" : 15 } , { $pushAll : { "test1": ["fff","ggg"] } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ "aaa", "bbb", "ccc", [ "ddd", "eee" ], "fff", "ggg" ], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }

6)  $addToSet

用法：{ $addToSet : { field : value } }

增加一个值到数组内，而且只有当这个值不在数组内才增加。例：
> db.test0.update( { "_id" : 15 } , { $addToSet : { "test1": {$each : ["444","555"] } } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [
        "aaa",
        "bbb",
        "ccc",
        [
                "ddd",
                "eee"
        ],
        "fff",
        "ggg",
        [
                "111",
                "222"
        ],
        "444",
        "555"
], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }
> db.test0.update( { "_id" : 15 } , { $addToSet : { "test1": {$each : ["444","555"] } } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [
        "aaa",
        "bbb",
        "ccc",
        [
                "ddd",
                "eee"
        ],
        "fff",
        "ggg",
        [
                "111",
                "222"
        ],
        "444",
        "555"
], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }
> db.test0.update( { "_id" : 15 } , { $addToSet : { "test1": ["444","555"]  } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [
        "aaa",
        "bbb",
        "ccc",
        [
                "ddd",
                "eee"
        ],
        "fff",
        "ggg",
        [
                "111",
                "222"
        ],
        "444",
        "555",
        [
                "444",
                "555"
        ]
], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }
> db.test0.update( { "_id" : 15 } , { $addToSet : { "test1": ["444","555"]  } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [
        "aaa",
        "bbb",
        "ccc",
        [
                "ddd",
                "eee"
        ],
        "fff",
        "ggg",
        [
                "111",
                "222"
        ],
        "444",
        "555",
        [
                "444",
                "555"
        ]
], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }


7) $pop

删除数组内的一个值

用法：
删除最后一个值：{ $pop : { field : 1  } }
删除第一个值：{ $pop : { field : -1  } }

注意，只能删除一个值，也就是说只能用1或-1，而不能用2或-2来删除两条。mongodb 1.1及以后的版本才可以用，例：
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [
        "bbb",
        "ccc",
        [
                "ddd",
                "eee"
        ],
        "fff",
        "ggg",
        [
                "111",
                "222"
        ],
        "444"
], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }
> db.test0.update( { "_id" : 15 } , { $pop : { "test1": -1 } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [
        "ccc",
        [
                "ddd",
                "eee"
        ],
        "fff",
        "ggg",
        [
                "111",
                "222"
        ],
        "444"
], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }
> db.test0.update( { "_id" : 15 } , { $pop : { "test1": 1 } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ "ccc", [ "ddd", "eee" ], "fff", "ggg", [ "111", "222" ] ], "test2" : [ "ccc" ], "test4" : "testv4",
"test5" : "OK" }

8) $pull

用法：$pull : { field : value } }

从数组field内删除一个等于value值。例：
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ "ccc", [ "ddd", "eee" ], "fff", "ggg", [ "111", "222" ] ], "test2" : [ "ccc" ], "test4" : "testv4",
"test5" : "OK" }

> db.test0.update( { "_id" : 15 } , { $pull : { "test1": "ggg" } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ "ccc", [ "ddd", "eee" ], "fff", [ "111", "222" ] ], "test2" : [ "ccc" ], "test4" : "testv4", "test5"
 : "OK" }

9) $pullAll

用法：{ $pullAll : { field : value_array } }

同$pull,可以一次删除数组内的多个值。例：
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ "ccc", [ "ddd", "eee" ], "fff", [ "111", "222" ] ], "test2" : [ "ccc" ], "test4" : "testv4", "test5"
 : "OK" }

> db.test0.update( { "_id" : 15 } , { $pullAll : { "test1": [ "ccc" , "fff" ] } } );
> db.test0.find( { "_id" : 15 } );
{ "_id" : { "floatApprox" : 15 }, "count" : 18, "test1" : [ [ "ddd", "eee" ], [ "111", "222" ] ], "test2" : [ "ccc" ], "test4" : "testv4", "test5" : "OK" }


10) $ 操作符

$是他自己的意思，代表按条件找出的数组里面某项他自己。呵呵，比较坳口。看一下官方的例子：

> t.find()
{ "_id" : ObjectId("4b97e62bf1d8c7152c9ccb74"), "title" : "ABC",  "comments" : [ { "by" : "joe", "votes" : 3 }, { "by" : "jane", "votes" : 7 } ] }

> t.update( {'comments.by':'joe'}, {$inc:{'comments.$.votes':1}}, false, true )

> t.find()
{ "_id" : ObjectId("4b97e62bf1d8c7152c9ccb74"), "title" : "ABC",  "comments" : [ { "by" : "joe", "votes" : 4 }, { "by" : "jane", "votes" : 7 } ] }

需要注意的是，$只会应用找到的第一条数组项，后面的就不管了。还是看例子：

> t.find();
{ "_id" : ObjectId("4b9e4a1fc583fa1c76198319"), "x" : [ 1, 2, 3, 2 ] }
> t.update({x: 2}, {$inc: {"x.$": 1}}, false, true);
> t.find();

还有注意的是$配合$unset使用的时候，会留下一个null的数组项，不过可以用{$pull:{x:null}}删除全部是null的数组项。例：
> t.insert({x: [1,2,3,4,3,2,3,4]})
> t.find()
{ "_id" : ObjectId("4bde2ad3755d00000000710e"), "x" : [ 1, 2, 3, 4, 3, 2, 3, 4 ] }
> t.update({x:3}, {$unset:{"x.$":1}})
> t.find()
{ "_id" : ObjectId("4bde2ad3755d00000000710e"), "x" : [ 1, 2, null, 4, 3, 2, 3, 4 ] }

{ "_id" : ObjectId("4b9e4a1fc583fa1c76198319"), "x" : [ 1, 3, 3, 2 ] }

