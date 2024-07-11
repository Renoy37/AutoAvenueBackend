import cloudinary.uploader
from config import app, db
from models import User, Car, Order
from datetime import datetime

def seed_data():
    # Clear existing data
    db.session.query(Order).delete()
    db.session.query(Car).delete()
    db.session.query(User).delete()
    db.session.commit()

    # Create sample users
    users_data = [
        {
            "username": "John Wells",
            "email": "johnseller@gmail.com",
            "password": "password123",
            "role": "seller"
        },
        {
            "username": "Perry Nice",
            "email": "perrycustomer@gmail.com",
            "password": "password123",
            "role": "customer"
        }
    ]

    users = []
    for user_data in users_data:
        user = User(
            username=user_data["username"],
            email=user_data["email"],
            role=user_data["role"]
        )
        user.password_hash = user_data["password"]
        users.append(user)

    db.session.add_all(users)
    db.session.commit()

    # Fetch users for setting relationships
    seller1 = User.query.filter_by(username="John Wells").first()
    customer1 = User.query.filter_by(username="Perry Nice").first()

    # Create sample cars
    cars_data = [
        {
            "carImage": "https://carsguide-res.cloudinary.com/image/upload/f_auto,fl_lossy,q_auto,t_default/v1/editorial/volkswagen-golf-gti-my20-1001x565-(1).jpg",
            "carMake": "Volkswagen",
            "carName": "Golf",
            "carYear": 2024,
            "carPrice": "$30,000",
            "carCategory": "Hatchback",
            "carMileage": "30,000 miles",
            "carEngine": "2000cc / 180HP",
            "carTransmission": "Automatic",
            "carFuel": "Petrol",
            "carDescription": "The Volkswagen Golf GTI is a popular hatchback known for its sporty performance and comfortable driving experience.",
            "seller_id": seller1.id
        },
        {
            "carImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSoCwgY0ftYiWRXfoJC8fzcsYUt1O1_0cW0LQ&s",
            "carMake": "Toyota",
            "carName": "Camry",
            "carYear": 2023,
            "carPrice": "$25,000",
            "carCategory": "Saloon",
            "carMileage": "25,000 miles",
            "carEngine": "2500cc / 200HP",
            "carTransmission": "Automatic",
            "carFuel": "Diesel",
            "carDescription": "The Toyota Camry is a reliable and spacious sedan, perfect for daily commuting with its fuel-efficient diesel engine.",
            "seller_id": seller1.id
        },
        {
            "carImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGehkFifyb2YeT0pphotnSMRZLxaEPD62gcA&s",
            "carMake": "Jeep",
            "carName": "Trackhawk",
            "carYear": 2022,
            "carPrice": "$20,000",
            "carCategory": "SUV",
            "carMileage": "20,000 miles",
            "carEngine": "1800cc / 150HP",
            "carTransmission": "Manual",
            "carFuel": "Petrol",
            "carDescription": "The Jeep Trackhawk is a powerful SUV designed for off-road adventures, equipped with a manual transmission for enthusiast drivers.",
            "seller_id": seller1.id
        },
        {
            "carImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1FqI_eUmJFC2QjNLHkdiEzE5KEpp9lkq-oQ&s",
            "carMake": "Volkswagen",
            "carName": "Passat",
            "carYear": 2023,
            "carPrice": "$28,000",
            "carCategory": "Wagon",
            "carMileage": "18,000 miles",
            "carEngine": "2200cc / 190HP",
            "carTransmission": "Automatic",
            "carFuel": "Petrol",
            "carDescription": "The Volkswagen Passat is a versatile wagon known for its spacious interior and smooth automatic transmission.",
            "seller_id": seller1.id
        },
        {
            "carImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxySXPleRuUDHVknh5gNcW2XLR2fiTafIk1g&s",
            "carMake": "Toyota",
            "carName": "Vellfire",
            "carYear": 2023,
            "carPrice": "$27,500",
            "carCategory": "Minivan",
            "carMileage": "22,000 miles",
            "carEngine": "2000cc / 180HP",
            "carTransmission": "Automatic",
            "carFuel": "Petrol",
            "carDescription": "The Toyota Vellfire is a luxurious minivan, offering ample space and comfort with its automatic transmission and powerful engine.",
            "seller_id": seller1.id
        },
        {
            "carImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0XVrlRCKN8-S7TnbXwiJGE3HJ1XHaJg09cg&s",
            "carMake": "Volkswagen",
            "carName": "Touareg",
            "carYear": 2022,
            "carPrice": "$24,000",
            "carCategory": "SUV",
            "carMileage": "28,000 miles",
            "carEngine": "3000cc / 250HP",
            "carTransmission": "Automatic",
            "carFuel": "Diesel",
            "carDescription": "The Volkswagen Touareg is a robust SUV known for its powerful diesel engine and luxurious features, perfect for adventurous drives.",
            "seller_id": seller1.id
        },
        {
            "carImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvidpwAU6rzIHLNEJqoVz9SO4x8xtRStDyVQ&s",
            "carMake": "BMW",
            "carName": "3 Series",
            "carYear": 2023,
            "carPrice": "$22,500",
            "carCategory": "Sedan",
            "carMileage": "15,000 miles",
            "carEngine": "1800cc / 150HP",
            "carTransmission": "Manual",
            "carFuel": "Petrol",
            "carDescription": "The BMW 3 Series is a classic sedan known for its sporty performance and elegant design, featuring a manual transmission for enthusiasts.",
            "seller_id": seller1.id
        },
        {
            "carImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZRtmihezmTPDqhJr8ogQy40fsPhRy_SM6-g&s",
            "carMake": "Ford",
            "carName": "Ranger",
            "carYear": 2024,
            "carPrice": "$32,000",
            "carCategory": "Pickup",
            "carMileage": "10,000 miles",
            "carEngine": "3500cc / 300HP",
            "carTransmission": "Automatic",
            "carFuel": "Petrol",
            "carDescription": "The Ford Ranger is a robust pickup truck with powerful engine options, perfect for both work and leisure activities.",
            "seller_id": seller1.id
        },
        {
            "carImage": "https://truckandfreight.co.za/wp-content/uploads/2022/08/Lead-Image-Faw-JH6-420-HP-004_880x500.jpeg",
            "carMake": "Scania",
            "carName": "MAN",
            "carYear": 2022,
            "carPrice": "$18,000",
            "carCategory": "Trucks",
            "carMileage": "25,000 miles",
            "carEngine": "1500cc / 120HP",
            "carTransmission": "Manual",
            "carFuel": "Petrol",
            "carDescription": "The Scania MAN is a powerful truck designed for heavy-duty transport, featuring a manual transmission and robust engine.",
            "seller_id": seller1.id
        },
        {
            "carImage": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTeVWN3P5cyChBEBSAOMzq94SZKbNw-7cyoRw&s",
            "carMake": "Mazda",
            "carName": "Atenza",
            "carYear": 2023,
            "carPrice": "$26,000",
            "carCategory": "Wagon",
            "carMileage": "20,000 miles",
            "carEngine": "2000cc / 180HP",
            "carTransmission": "Automatic",
            "carFuel": "Petrol",
            "carDescription": "The Mazda Atenza is a stylish wagon offering a comfortable ride and efficient automatic transmission, perfect for family travels.",
            "seller_id": seller1.id
        }
        # Add more cars as needed...
    ]

    cars = []
    for car_data in cars_data:
        # Upload image to Cloudinary
        upload_result = cloudinary.uploader.upload(car_data["carImage"])
        car_data["carImage"] = upload_result["url"]

        car = Car(
            carImage=car_data["carImage"],
            carMake=car_data["carMake"],
            carName=car_data["carName"],
            carYear=car_data["carYear"],
            carPrice=car_data["carPrice"],
            carCategory=car_data["carCategory"],
            carMileage=car_data["carMileage"],
            carEngine=car_data["carEngine"],
            carTransmission=car_data["carTransmission"],
            carFuel=car_data["carFuel"],
            carDescription=car_data["carDescription"],
            seller_id=car_data["seller_id"]
        )
        cars.append(car)

    db.session.add_all(cars)
    db.session.commit()

    # Create sample orders
    orders_data = [
        {
            "orderId": "ORD123456",
            "customerName": "John Doe",
            "customerContact": "john.doe@example.com",
            "deliveryAddress": "123 Main St, Springfield, IL",
            "car_id": cars[0].id,
            "orderStatus": "Pending",
            "orderDate": datetime.strptime("2024-06-30", "%Y-%m-%d"),
            "paymentMethod": "Credit Card",
            "additionalNotes": "Please include floor mats.",
            "user_id": customer1.id
        },
        {
            "orderId": "ORD123457",
            "customerName": "Jane Smith",
            "customerContact": "jane.smith@example.com",
            "deliveryAddress": "456 Elm St, Springfield, IL",
            "car_id": cars[1].id,
            "orderStatus": "Confirmed",
            "orderDate": datetime.strptime("2024-06-29", "%Y-%m-%d"),
            "paymentMethod": "Bank Transfer",
            "additionalNotes": "Delivery after 5 PM.",
            "user_id": customer1.id
        },
        {
            "orderId": "ORD123458",
            "customerName": "Michael Brown",
            "customerContact": "michael.brown@example.com",
            "deliveryAddress": "789 Oak St, Springfield, IL",
            "car_id": cars[2].id,
            "orderStatus": "Pending",
            "orderDate": datetime.strptime("2024-06-28", "%Y-%m-%d"),
            "paymentMethod": "PayPal",
            "additionalNotes": "Express delivery requested.",
            "user_id": customer1.id
        },
        # Add more orders as needed...
    ]

    orders = []
    for order_data in orders_data:
        order = Order(
            orderId=order_data["orderId"],
            customerName=order_data["customerName"],
            customerContact=order_data["customerContact"],
            deliveryAddress=order_data["deliveryAddress"],
            car_id=order_data["car_id"],
            orderStatus=order_data["orderStatus"],
            orderDate=order_data["orderDate"],
            paymentMethod=order_data["paymentMethod"],
            additionalNotes=order_data["additionalNotes"],
            user_id=order_data["user_id"]
        )
        orders.append(order)

    db.session.add_all(orders)
    db.session.commit()
    
    print("Data cleared and added successfully to the database")

if __name__ == "__main__":
    with app.app_context():
        seed_data()
