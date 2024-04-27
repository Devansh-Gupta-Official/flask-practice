#CREATE, READ, UPDATE AND DELETE
#CAN ONLY RUN THIS SCRIPT ONCE AS AFTER THIS DATABASE CHANGES

from basic_sql_9 import db, Puppy

#CREATE
my_puppy=Puppy("Rufus",5)
db.session.add(my_puppy)
db.session.commit()

#READ
#can introduce ORM(Object relational mapper) options
all_puppies = Puppy.query.all() #list of puppy objects in the table
print(all_puppies)

#select by id
puppy1 = Puppy.query.get(1)
print(puppy1.name)

#filter by name
puppy_frankie = Puppy.query.filter_by(name="Frankie")   #produce some sql code for us
print(puppy_frankie.all())

#UPDATE
first_puppy=Puppy.query.get(1)
first_puppy.age=10
db.session.add(first_puppy)
db.session.commit()

#DELETE
second_puppy=Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

#print all puppies to check changes
all_puppies=Puppy.query.all()
print(all_puppies)