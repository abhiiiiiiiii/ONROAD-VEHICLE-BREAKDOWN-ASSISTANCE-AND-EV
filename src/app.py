from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from src.coding import web_app  
from src.webservice import api_app  

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdef'

# Register Blueprints
app.register_blueprint(web_app)
app.register_blueprint(api_app, url_prefix='/api')

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/breakdowndb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Flask-Migrate for DB migrations

if __name__ == '__main__':
    app.run(debug=True, port=5001)
