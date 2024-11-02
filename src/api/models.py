from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Category(db.Model):
    __tablename__ = 'restaurant_category'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Category {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
    
class Ocasiones1 (db.Model):
    __tablename__ = 'ocasiones'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<Ocasiones1 {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    identification_number = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<Client {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            "last_name": self.last_name,
            "phone_number" : self.phone_number,
            "identification_number": self.identification_number,
            "is_active": self.is_active
          # do not serialize the password, its a security breach
        }    
    
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    location = db.Column(db.String(80), unique=False, nullable=False)
    phone_number = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    guests_capacity = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    image_url = db.Column(db.String(120), unique=False, nullable=False)
    latitude = db.Column(db.Numeric, nullable=True) 
    longitude = db.Column(db.Numeric, nullable=True) 
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<Restaurant {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "phone_number": self.phone_number,
            "email": self.email,
            "guests_capacity": self.guests_capacity,
            "image_url": self.image_url,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "is_active": self.is_active,
            # do not serialize the password, it's a security breach
        }

class Admin1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(80), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<Admin1 {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "name": self.name,
            "email": self.email,
            "is_active": self.is_active
            # do not serialize the password, it's a  security breach
        }

        
    

class Reservations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    occasion = db.Column(db.String(120), nullable=True)
    time = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(120), nullable=False)
    number_of_people = db.Column(db.String(120), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=True)    
    is_active = db.Column(db.Boolean(), nullable=True)

    client = db.relationship('Client', backref=db.backref('reservations', lazy=True))
    restaurant = db.relationship('Restaurant', backref=db.backref('reservations', lazy=True))

    def __repr__(self):
        return f'<Reservations {self.time}, {self.date}>'
    def serialize(self):
        return {
            "id":self.id,
            "client_id": self.client_id,
            "email_client": self.client.email if self.client else None,
            "restaurant_id": self.restaurant_id,
            "number_of_people": self.number_of_people,
            "time": self.time,
            "date":self.date,
            "occasion":self.occasion,

            
        }



