from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Docker from interns!'


if __name__ == "__main__":
    app.run(port=8080)

# - install python 
# - dependency 
# - run the app
