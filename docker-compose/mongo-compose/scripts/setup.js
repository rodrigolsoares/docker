db.createUser(
{
    user: "svc_viamais",
    pwd: "aAtdbu3kSp30aYOyvT2f",
    roles: [
      { role: "readWrite", db: "admin" }
    ]
})



####Replica Set

docker exec -it mongo0 mongo

config={"_id":"rs0","members":[{"_id":0,"host":"mongo0:27017"},{"_id":1,"host":"mongo1:27017"},{"_id":2,"host":"mongo2:27017"}]}

rs.initiate(config)
