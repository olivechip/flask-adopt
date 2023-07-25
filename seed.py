from models import db, Pet
from app import app

db.drop_all()
db.create_all()

p1 = Pet(name='scout', species='cat', age=2)
p2 = Pet(name='teddy', species='dog', age=6, notes='mini poodle', available=False)
p3 = Pet(name='bear', species='cat', age=6, notes='persian', available=False)
p4 = Pet(name='coco', species='cat', age=6, notes='persian', available=False)

db.session.add_all([p1, p2, p3, p4])
db.session.commit()