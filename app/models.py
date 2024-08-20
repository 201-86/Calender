from app.routes import db

class user(db.Model):
    __tablename__ = "Login"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    password = db.Column(db.Text())
    def __repr__(self):
        return self.password
    
class date(db.Model):
    __tablename__ = "Date"
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text())
    year = db.Column(db.Integer())
    acc_id = db.Column(db.Integer())
    month = db.Column(db.Integer())
    day = db.Column(db.Integer())
    

    def __repr__(self):
        return self.passwords


#class Base(db.Model):
#    __tablename__ = "Base"
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.Text())
#    description = db.Column(db.Text())
#    
#    def __repr__(self):
#        return self.name

#class Topping(db.Model):
#    __tablename__ = "Topping"
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.Text())
#    description = db.Column(db.Text())
#    
#    pizzas = db.relationship('Pizza', secondary = 'PizzaTopping', back_populates = 'toppings')
#    def __repr__(self):
#        return self.name

