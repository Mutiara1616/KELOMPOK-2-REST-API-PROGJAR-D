import os

class Config:
    INSTANCE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
    if not os.path.exists(INSTANCE_PATH):
        os.makedirs(INSTANCE_PATH)
    
    # Database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(INSTANCE_PATH, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False