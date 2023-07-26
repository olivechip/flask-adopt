from models import db, Pet
from app import app

db.drop_all()
db.create_all()

p1 = Pet(name='Scout', species='cat', age=2, photo_url='https://www.kittyconnection.net/wp-content/uploads/2021/10/Scout.jpg')
p2 = Pet(name='Teddy', species='dog', age=6, photo_url='https://breed-assets.wisdompanel.com/dog/poodle-miniature-toy/poodle-miniature-toy3.jpg', notes='mini poodle', available=False)
p3 = Pet(name='Bear', species='cat', age=6, notes='persian', photo_url='https://www.thesprucepets.com/thmb/TU314sIYpY5NNX0trZmLBpbflb4=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/persian-cats-gallery-4121944-hero-f5c237b8c6404655afb1e1bbae219ba5.jpg', available=False)
p4 = Pet(name='Coco', species='cat', age=6, notes='persian', photo_url='https://www.dogbreedinfo.com/images11/Persiandilute%20calicoPuzzle.jpg', available=False)

db.session.add_all([p1, p2, p3, p4])
db.session.commit()