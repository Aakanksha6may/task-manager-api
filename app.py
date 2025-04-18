from flask import Flask
from config import Config
from models import db, bcrypt
from flask_jwt_extended import JWTManager
from auth import auth_bp
from routes import task_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(task_bp)

@app.route('/')
def home():
    return {"message": "Welcome to the Task Manager API"}

if __name__ == '__main__':
    app.run(debug=True)
