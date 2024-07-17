# from config import app, db, api
# from models import Car, User, Order
# from flask import request, jsonify, make_response
# from flask_restful import Resource
# from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
# from seller import HelloSeller, GetSellerProducts, DeleteProduct, AddProducts, GetSellerOrders
# from oauth import Register, Login
# from datetime import datetime


# # Default route
# @app.route('/')
# def home():
#     return 'Welcome to the AutoAvenue API!'


# # Get All Cars Endpoint
# class Cars(Resource):
#     def get(self):
#         try:
#             cars = Car.query.all()
#             if not cars:
#                 return make_response(jsonify({"Message": "No cars found"}), 404)
#             return make_response(jsonify([car.to_dict() for car in cars]), 200)
#         except Exception as e:
#             return make_response(jsonify({"Message": "Error retrieving cars", "Error": str(e)}), 500)


# # Place an Order Endpoint
# # class PlaceOrder(Resource):
# #     @jwt_required()
# #     def post(self):
# #         user_id = get_jwt_identity()
# #         data = request.get_json()

# #         # Validate input data
# #         required_fields = ['orderId', 'car_id', 'customerName', 'customerContact', 'deliveryAddress', 'orderDate', 'paymentMethod']
# #         for field in required_fields:
# #             if field not in data:
# #                 return make_response(jsonify({"Message": f"Missing required field: {field}"}), 400)

# #         # Convert orderDate from string to datetime
# #         try:
# #             order_date = datetime.fromisoformat(data['orderDate'])
# #         except ValueError:
# #             return make_response(jsonify({"Message": "Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)"}), 400)

# #         try:
# #             new_order = Order(
# #                 orderId=data['orderId'],
# #                 user_id=user_id,
# #                 car_id=data['car_id'],
# #                 customerName=data['customerName'],
# #                 customerContact=data['customerContact'],
# #                 deliveryAddress=data['deliveryAddress'],
# #                 orderStatus='Pending',
# #                 orderDate=order_date,  # Use the converted datetime object
# #                 paymentMethod=data['paymentMethod'],
# #                 additionalNotes=data.get('additionalNotes', '')  # Handle optional field
# #             )
# #             db.session.add(new_order)
# #             db.session.commit()
# #             return make_response(jsonify({"Message": "Order placed successfully"}), 201)
# #         except Exception as e:
# #             return make_response(jsonify({"Message": "Error placing order", "Error": str(e)}), 500)


# ######## Place an Order Endpoint(Revised Edition)
# class PlaceOrder(Resource):
#     @jwt_required()
#     def post(self):
#         user_id = get_jwt_identity()
#         data = request.get_json()

#         # Validate input data
#         required_fields = ['carCategory', 'carDescription', 'carEngine', 'carFuel', 'carImage', 'carMake', 'carMileage', 'carName', 'carPrice', 'carTransmission', 'carYear', 'customerName', 'customerContact', 'deliveryAddress', 'orderDate', 'paymentMethod']
#         for field in required_fields:
#             if field not in data:
#                 return make_response(jsonify({"Message": f"Missing required field: {field}"}), 400)

#         # Convert orderDate from string to datetime
#         try:
#             order_date = datetime.fromisoformat(data['orderDate'])
#         except ValueError:
#             return make_response(jsonify({"Message": "Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)"}), 400)

#         try:
#             new_order = Order(
#                 user_id=user_id,
#                 car_id=data['id'],  # Assuming 'id' from frontend is the car_id
#                 customerName=data['customerName'],
#                 customerContact=data['customerContact'],
#                 deliveryAddress=data['deliveryAddress'],
#                 orderStatus='Pending',
#                 orderDate=order_date,  # Use the converted datetime object
#                 paymentMethod=data['paymentMethod'],
#                 additionalNotes=data.get('additionalNotes', '')  # Handle optional field
#             )
#             db.session.add(new_order)
#             db.session.commit()
#             return make_response(jsonify({"Message": "Order placed successfully"}), 201)
#         except Exception as e:
#             return make_response(jsonify({"Message": "Error placing order", "Error": str(e)}), 500)


# # Delete an Order Endpoint
# class DeleteOrder(Resource):
#     @jwt_required()
#     def delete(self, order_id):
#         try:
#             user_id = get_jwt_identity()
#             order = Order.query.filter_by(id=order_id, user_id=user_id).first()
#             if not order:
#                 return make_response(jsonify({"Message": "Order not found"}), 404)
#             db.session.delete(order)
#             db.session.commit()
#             return make_response(jsonify({"Message": "Order deleted successfully"}), 200)
#         except Exception as e:
#             return make_response(jsonify({"Message": "Error deleting order", "Error": str(e)}), 500)


# # Add Resources to API
# api.add_resource(Register, '/api/register')
# api.add_resource(Login, '/api/login')
# api.add_resource(HelloSeller, '/seller')
# api.add_resource(Cars, '/api/cars')
# api.add_resource(PlaceOrder, '/api/orders')
# api.add_resource(DeleteOrder, '/api/orders/<int:order_id>')
# api.add_resource(GetSellerProducts, '/shop/products/api')
# api.add_resource(DeleteProduct, '/shop/products/del/api/<int:product_id>')
# api.add_resource(AddProducts, '/shop/addproducts/api')
# api.add_resource(GetSellerOrders, '/api/shop.orders')



# if __name__ == '__main__':
#     app.run(port=5555, debug=True)

from config import app, db, api
from models import Car, User, Order
from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from seller import HelloSeller, GetSellerProducts, DeleteProduct, AddProducts, GetSellerOrders
from oauth import Register, Login
from datetime import datetime
from flask_cors import CORS, cross_origin



# Default route
@app.route('/')
def home():
    return 'Welcome to the AutoAvenue API!'


# Get All Cars Endpoint
class Cars(Resource):
    @cross_origin(allow_headers=['Content-Type'])
    def get(self):
        try:
            cars = Car.query.all()
            if not cars:
                return make_response(jsonify({"Message": "No cars found"}), 404)
            return make_response(jsonify([car.to_dict() for car in cars]), 200)
        except Exception as e:
            return make_response(jsonify({"Message": "Error retrieving cars", "Error": str(e)}), 500)


# Place an Order Endpoint (Revised Edition)
class PlaceOrder(Resource):
    @cross_origin()
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()

        # Validate input data
        required_fields = ['carCategory', 'carDescription', 'carEngine', 'carFuel', 'carImage', 'carMake', 'carMileage', 'carName', 'carPrice', 'carTransmission', 'carYear', 'customerName', 'customerContact', 'deliveryAddress', 'orderDate', 'paymentMethod']
        for field in required_fields:
            if field not in data:
                return make_response(jsonify({"Message": f"Missing required field: {field}"}), 400)

        # Convert orderDate from string to datetime
        try:
            order_date = datetime.fromisoformat(data['orderDate'])
        except ValueError:
            return make_response(jsonify({"Message": "Invalid date format. Use ISO format (YYYY-MM-DDTHH:MM:SS)"}), 400)

        try:
            new_order = Order(
                user_id=user_id,
                car_id=data['car_id'],  # Assuming 'car_id' from frontend
                customerName=data['customerName'],
                customerContact=data['customerContact'],
                deliveryAddress=data['deliveryAddress'],
                orderStatus='Pending',
                orderDate=order_date,  # Use the converted datetime object
                paymentMethod=data['paymentMethod'],
                additionalNotes=data.get('additionalNotes', '')  # Handle optional field
            )
            db.session.add(new_order)
            db.session.commit()
            return make_response(jsonify({"Message": "Order placed successfully"}), 201)
        except Exception as e:
            return make_response(jsonify({"Message": "Error placing order", "Error": str(e)}), 500)


# Delete an Order Endpoint
class DeleteOrder(Resource):
    @cross_origin()
    @jwt_required()
    def delete(self, order_id):
        try:
            user_id = get_jwt_identity()
            order = Order.query.filter_by(id=order_id, user_id=user_id).first()
            if not order:
                return make_response(jsonify({"Message": "Order not found"}), 404)
            db.session.delete(order)
            db.session.commit()
            return make_response(jsonify({"Message": "Order deleted successfully"}), 200)
        except Exception as e:
            return make_response(jsonify({"Message": "Error deleting order", "Error": str(e)}), 500)


# CORS handling for OPTIONS requests
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:5173')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/api/orders', methods=['OPTIONS'])
def handle_orders_options():
    return build_cors_preflight_response()

def build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "http://localhost:5173")
    response.headers.add('Access-Control-Allow-Headers', "Content-Type,Authorization")
    response.headers.add('Access-Control-Allow-Methods', "GET,PUT,POST,DELETE,OPTIONS")
    return response

# Add Resources to API
api.add_resource(Register, '/api/register')
api.add_resource(Login, '/api/login')
api.add_resource(HelloSeller, '/api/seller')
api.add_resource(Cars, '/api/cars')
api.add_resource(PlaceOrder, '/api/orders')
api.add_resource(DeleteOrder, '/api/orders/<int:order_id>')
api.add_resource(GetSellerProducts, '/api/shop/products')
api.add_resource(DeleteProduct, '/api/shop/products/<int:product_id>')
api.add_resource(AddProducts, '/api/shop/addproducts')
api.add_resource(GetSellerOrders, '/api/shop/orders')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
