from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Car, Order
from config import db
from flask_restful import Resource
import cloudinary.uploader
from werkzeug.exceptions import HTTPException
from sqlalchemy.exc import SQLAlchemyError
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

seller_bp = Blueprint('seller_bp', __name__)

# Get Seller Products Endpoint
class GetSellerProducts(Resource):
    @jwt_required()
    def get(self):
        try:
            seller_id = get_jwt_identity()
            logger.debug(f"Fetching products for seller ID: {seller_id}")

            products = Car.query.filter_by(seller_id=seller_id).all()
            logger.debug(f"Fetched products: {products}")

            if not products:
                return make_response(jsonify({"Message": "No products present"}), 404)

            return make_response(jsonify([product.to_dict() for product in products]), 200)

        except SQLAlchemyError as e:
            logger.error(f"Database error: {e}")
            return make_response(jsonify({"Message": "Database error occurred", "Error": str(e)}), 500)

        except HTTPException as e:
            logger.error(f"HTTP error: {e}")
            return make_response(jsonify({"Message": "HTTP error occurred", "Error": str(e)}), e.code)

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return make_response(jsonify({"Message": "An unexpected error occurred", "Error": str(e)}), 500)

# Add New Product Endpoint
class AddProducts(Resource):
    @jwt_required()
    def post(self):
        try:
            seller_id = get_jwt_identity()
            if 'file' not in request.files:
                return make_response(jsonify({"Message": "No file part in the request"}), 400)
            
            file = request.files['file']
            if file.filename == '':
                return make_response(jsonify({"Message": "No file selected for uploading"}), 400)
            
            upload_result = cloudinary.uploader.upload(file)
            image_url = upload_result['url']
            
            data = request.form
            new_product = Car(
                carImage=image_url,
                carMake=data['carMake'],
                carName=data['carName'],
                carYear=data['carYear'],
                carPrice=data['carPrice'],
                carCategory=data['carCategory'],
                carMileage=data['carMileage'],
                carEngine=data['carEngine'],
                carTransmission=data['carTransmission'],
                carFuel=data['carFuel'],
                carDescription=data['carDescription'],
                seller_id=seller_id
            )
            db.session.add(new_product)
            db.session.commit()
            return make_response(jsonify({"Message": "Product added successfully"}), 201)
        except Exception as e:
            db.session.rollback()
            logger.error(f"Error adding product: {e}")
            return make_response(jsonify({"Message": f"Error adding product: {str(e)}"}), 500)

# Delete Product Endpoint
class DeleteProduct(Resource):
    @jwt_required()
    def delete(self, product_id):
        try:
            seller_id = get_jwt_identity()
            product = Car.query.filter_by(id=product_id, seller_id=seller_id).first()
            if not product:
                return make_response(jsonify({"Message": "Product not found"}), 404)
            
            # Delete the product (Car) and let cascade handle associated Orders
            db.session.delete(product)
            db.session.commit()
            
            return make_response(jsonify({"Message": "Product deleted successfully"}), 200)
        
        except Exception as e:
            db.session.rollback()
            logger.error(f"Error deleting product: {e}")
            return make_response(jsonify({"Message": f"Error deleting product: {str(e)}"}), 500)

# Get Seller Orders Endpoint
class GetSellerOrders(Resource):
    @jwt_required()
    def get(self):
        try:
            seller_id = get_jwt_identity()
            orders = Order.query.join(Car).filter(Car.seller_id == seller_id).all()
            
            if not orders:
                return make_response(jsonify({"Message" : "No orders available"}))
            return make_response(jsonify([order.to_dict() for order in orders]), 200)
            
        except Exception as e:
            logger.error(f"Error retrieving seller orders: {e}")
            return make_response(jsonify({"Message": f"Error retrieving seller orders: {str(e)}"}), 500)

# Hello Seller Endpoint
class HelloSeller(Resource):
    def get(self):
        hello = 'Hello Seller'
        return make_response(hello, 200)
