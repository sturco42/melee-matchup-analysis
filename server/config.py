from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_bcrypt import Bcrypt
import os
# from os import environ
from dotenv import load_dotenv

app = Flask(__name__,
            static_url_path='',
            static_folder='../client/build',
            template_folder='../client/build'
            )

load_dotenv()
# uri = os.getenv("DATABASE_URL")  # or other relevant config var
# if uri.startswith("postgres://"):
#     uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# this maybe needs to be empty
app.secret_key = os.environ.get('SECRET_KEY')

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app, prefix='/api')

CORS(app)

bcrypt = Bcrypt(app)