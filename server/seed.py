from config import db, app
from models import User, Car, Order
from datetime import datetime

with app.app_context():
    # Drop all tables in the database
    db.drop_all()
    # Create all tables in the database
    db.create_all()

    # Create some users
    user1 = User(username='Rob', email='Rob@gmail.com', role='seller')
    user1.password_hash = 'seller'  # Set the password for the seller
    user2 = User(username='Ben', email='Ben@gmail.com', role='customer')
    user2.password_hash = 'customer'  # Set the password for the customer

    # Add the users to the session and commit to the database
    db.session.add_all([user1, user2])
    db.session.commit()

    # Create some cars and associate them with the seller
    car1 = Car(carImage='car1.jpg', carMake='Toyota', carName='Corolla', carYear=2020, carPrice='20000', carCategory='Sedan', carMileage='10000', carEngine='1.8L', carTransmission='Automatic', carFuel='Gasoline', carDescription='A reliable car', seller_id=user1.id)
    car2 = Car(carImage='car2.jpg', carMake='Honda', carName='Civic', carYear=2019, carPrice='18000', carCategory='Sedan', carMileage='15000', carEngine='2.0L', carTransmission='Manual', carFuel='Gasoline', carDescription='A sporty car', seller_id=user1.id)

    # Add the cars to the session and commit to the database
    db.session.add_all([car1, car2])
    db.session.commit()

    # Create some orders and associate them with the customer and the cars
    order1 = Order(orderId='ORD001', user_id=user2.id, car_id=car1.id, customerName='John Doe', customerContact='1234567890', deliveryAddress='123 Main St', orderStatus='Pending', orderDate=datetime.utcnow(), paymentMethod='Credit Card', additionalNotes='Deliver ASAP')
    order2 = Order(orderId='ORD002', user_id=user2.id, car_id=car2.id, customerName='Jane Doe', customerContact='0987654321', deliveryAddress='456 Elm St', orderStatus='Pending', orderDate=datetime.utcnow(), paymentMethod='PayPal', additionalNotes='Call before delivery')

    # Add the orders to the session and commit to the database
    db.session.add_all([order1, order2])
    db.session.commit()

# Notify that the database seeding is complete
print("Database has been cleared and seeded successfully.")
