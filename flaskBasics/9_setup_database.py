from basic_sql_9 import db,Puppy

#SETU DATABASE
#creates all tables  model->db table
db.create_all()

sam = Puppy("Sammy",3)
frank = Puppy("Frankie",4)

#these will be null as we havent added to database yet
print(sam.id)
print(frank.id)

db.session.add_all([sam,frank])  #add objects in a list

#adding objects individually
# db.session.add(sam)
# db.session.add(frank)

db.session.commit()   #saving changes to database

print(sam.id)
print(frank.id)







