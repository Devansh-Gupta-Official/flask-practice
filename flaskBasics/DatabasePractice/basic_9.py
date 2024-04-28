#create entries into the tables

from models_9 import db, Puppy, Toy, Owner

#Creating 2 puppies
rufus=Puppy("Rufus")
fido = Puppy("Fido")

#add puppies to db
db.session.add_all([rufus,fido])
db.session.commit()

#checking..
print(Puppy.query.all())


rufus=Puppy.query.filter_by(name='Rufus').first() #give me first entry whose name is Rufus

#create owner
devansh=Owner("Devansh",rufus.id)

#give some toys to rufus
toy1 = Toy("Chew Toy", rufus.id)
toy2 = Toy("Ball", rufus.id)

db.session.add_all([devansh,toy1,toy2])
db.session.commit()


#grab rufus again
rufus=Puppy.query.filter_by(name='Rufus').first()
print(rufus)

rufus.report_toys()