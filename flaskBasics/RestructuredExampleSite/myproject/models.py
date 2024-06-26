from myproject import db
#setup db inside the __init__ .py

#MODELS
class Puppy(db.Model):
    __tablename__='puppies'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    owner=db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name=name

    def repr(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and no owner assigned yet"
    

class Owner(db.Model):
    __tablename__='owners'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    puppy_id=db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name=name
        self.puppy_id=puppy_id

    def repr(self):
        return f"Owner name: {self.name}"
    