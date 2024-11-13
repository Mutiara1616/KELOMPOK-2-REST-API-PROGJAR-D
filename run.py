from App import create_app
from App.extensions import db
import os

app = create_app()

if __name__ == '__main__':
    instance_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)
        
    with app.app_context():
        db.create_all()
    app.run(debug=True)