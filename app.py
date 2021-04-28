import os
from flask import Flask, request
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()
DATABASE_URI = os.getenv('DATABASE_URI')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/', methods=['GET'])
def hello_world():
   if request.method == 'GET':
      return "Hello World"

@app.route('/test')
def test_route():
   return "TEST ROUTE"

@app.route('/test')
@app.route('/test/another/<int:user_id>', methods=['GET', 'POST'])
def another_test_route(user_id):
   print(user_id)
   return "ANOTHER TEST ROUTE"


if __name__ == '__main__':
    app.debug = True
    app.run()


# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass

#     # a simple page that says hello
#     @app.route('/hello')
#     def hello():
#         return 'Hello, World!'

#     return app
