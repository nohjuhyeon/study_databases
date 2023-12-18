### mongoDB functions
- insertOne()|collection에 하나의 데이터(tyep = dictionary) 추가 |db.fruits.insertOne({...})
- insertMany()|collection에 여러 개의 데이터(type = list) 추가 |db.posts.insertMany({...})
- deleteOne()|collection에 Key = "Value"인 하나의 데이터 삭제 |db.fruits.deleteOne({ Key : "Value"})
- deleteMany()|collection에 Key = "Value"인 여러 개의 데이터 삭제 |db.fruits.deleteMany({Key : "Value"})
- deleteMany()|collection의 모든 데이터 삭제 |db.fruits.deleteMany({})
- find()|collection 내의 Key = Value인 데이터 검색|db.posts.find({}, {Key : "Value})

db.posts.find({category : {$eq : "Event"}},{title : 1,category:1,likes:1}) ;

db.posts.find({$and :[{category :{ $in : ["Event", "Tech"]}}, {likes:{$gt:4}}]}, {tilte:1, category:1, likes:1})

- $eq: ==
- $ne: !=
- $gt: >
- $gte: >=
- $lt: <
- $lte: <=
- $in: in 
- $and: and
- $or: or
- $nor: nor
- $not: not