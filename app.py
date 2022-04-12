from flask import Flask

from routes import color
import time 

def create_app():
    app = Flask(__name__)
    app.register_blueprint(color, url_prefix="")
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
