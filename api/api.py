from flask import Flask
from flask_cors import CORS
from routes import routes
from seed import run_seed

app = Flask(__name__)
CORS(app, origins=["http://localhost:*"], allow_headers=["Content-Type","Access-Control-Allow-Origin"], methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])
app.register_blueprint(routes)
run_seed()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
