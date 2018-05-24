import sys
app = Flask(__name__)
from random import randint

def connect(name):
	conn_string = "host='nipdb.c89gwqjlynjo.us-east-2.rds.amazonaws.com' dbname='nipDB' user='nipun043' password='nikunj23'"
	conn = psycopg2.connect(conn_string)
	cursor = conn.cursor()
	cursor.execute("SELECT * FROM test WHERE test LIKE '%" + str(name) + "%'" )
	records = cursor.fetchall()
	conn.close()
	return records


@app.route('/')
def intro():
	return render_template('index.html')

@app.route('/resume',methods=['GET'])
def resume():
        return render_template('resume.html')

@app.route('/files',methods=['GET'])
def files():
        return jsonify({'Files': 'Under Construction'})


@app.route('/game', methods = ['POST'])
def game():
    name = ['Abraham','Disney','Picasso','Eliot','Stevenson','Andretti']
    n = randint(0, 5) 
    r = request.form['game']
    if r.isdigit():
        b = connect(str(name[n]))
        return str(b[0][0])
    else:
        return "Please enter your birth year"

if __name__ == '__main__':
	app.run(debug=False,port=8080,host='0.0.0.0')
