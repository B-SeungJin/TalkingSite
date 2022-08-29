from flask import Flask
from sub_blueprint import test

app = Flask(__name__)
app.register_blueprint(test.page_ab, url_prefix = '/talk')

# http://localhost:8080/talk/talk1
if __name__ == '__main__' :
    app.run(host='0.0.0.0', port='8080')