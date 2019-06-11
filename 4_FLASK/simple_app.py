from flask import Flask
from flask import request
app = Flask(__name__)

#Route
@app.route('/')
def index(name='Mundo', lastname='!!!!!!!'):
    name = request.args.get('name', name)
    lastname = request.args.get('lastname', lastname)
    return "Holas {} {}".format(name, lastname)

app.run(debug=True, port=8000, host='0.0.0.0')
