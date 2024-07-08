from flask import Flask
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
import os
from flask_cors import CORS
from flask_session import Session
from flask_jwt_extended import JWTManager
import cloudinary
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv



load_dotenv()


# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'sqlite:///autoavenue.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = ' befjuyk//t[trht]'
app.config['SESSION_TYPE'] = 'filesystem'
SECRET_KEY = app.config['SECRET_KEY'] = 'bjhjh43j554h63%#@n32@#' 
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'hgcfyi876tgh')

# cloudinary.config( 
#   cloud_name = 'dol3eg0to',
#   api_key = '843678846326154',
#   api_secret = 'qWeEH2FpH50S8ctME2xpv-tLKtI'
# )

# cloudinary.config( 
#     cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
#     api_key = os.getenv('CLOUDINARY_API_KEY'),
#     api_secret = os.getenv('CLOUDINARY_API_SECRET')
# )

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

# Initialize SQLAlchemy
db = SQLAlchemy(metadata=metadata)
db.init_app(app)
migrate = Migrate(app, db)

# Initialize Flask-RESTful and JWT
api = Api(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# Enable CORS
CORS(app)
Session(app)
