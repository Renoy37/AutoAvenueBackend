from config import db, bcrypt, SECRET_KEY
from datetime import datetime, timedelta
import jwt
import cloudinary.uploader
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property

class User(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password_hash = db.Column(db.String(250), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    orders = db.relationship('Order', backref='user', lazy=True)

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Cannot view password')

    @password_hash.setter
    def password_hash(self, password):
        hashed_password = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = hashed_password.decode('utf-8')
        
    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    def generate_token(self, expires_in=1800):
        exp = datetime.utcnow() + timedelta(seconds=expires_in)
        payload = {
            'user_id': self.id,
            'exp': exp
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token
    
    serialize_rules = ('-_password_hash', '-orders.user')

class Car(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    carImage = db.Column(db.String(255), nullable=False)
    carMake = db.Column(db.String(50), nullable=False)
    carName = db.Column(db.String(50), nullable=False)
    carYear = db.Column(db.Integer, nullable=False)
    carPrice = db.Column(db.String(50), nullable=False)
    carCategory = db.Column(db.String(50), nullable=False)
    carMileage = db.Column(db.String(50), nullable=False)
    carEngine = db.Column(db.String(50), nullable=False)
    carTransmission = db.Column(db.String(50), nullable=False)
    carFuel = db.Column(db.String(50), nullable=False)
    carDescription = db.Column(db.String(280), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    orders = db.relationship('Order', backref='car', lazy=True, cascade='all, delete')

    
    def upload_image(self, image):
        upload_result = cloudinary.uploader.upload(image)
        self.carImage = upload_result['url']
    
    serialize_rules = ('-orders.car',)

class Order(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    orderId = db.Column(db.String(50), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    car_id = db.Column(db.Integer, db.ForeignKey('car.id'), nullable=False)
    customerName = db.Column(db.String(50), nullable=False)
    customerContact = db.Column(db.String(100), nullable=False)
    deliveryAddress = db.Column(db.String(255), nullable=False)
    orderStatus = db.Column(db.String(50), nullable=False)
    orderDate = db.Column(db.DateTime, default=datetime.utcnow)
    paymentMethod = db.Column(db.String(50), nullable=False)
    additionalNotes = db.Column(db.String(255))
    
    serialize_rules = ('-user.orders', '-car.orders')

