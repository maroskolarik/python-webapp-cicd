from flask import Flask

webapp = Flask(__name__)


@webapp.route('/')
def home():
    return "2024-02-21-1433"


if __name__ == '__main__':
    webapp.run(debug=True)
