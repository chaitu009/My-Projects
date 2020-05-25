from flask import Flask, render_template
import analyt

app = Flask(__name__)

data = analyt.getdata('https://api.rootnet.in/covid19-in/unofficial/covid19india.org/statewise/history')
df_main = analyt.getdf(data)
latest=data[len(data)-1]

@app.route('/')
def hello_world():
    return render_template('Home.html',data = data)
@app.route('/statewise')
def statewise():
    return render_template('statewise.html',data=data ,latest = latest)

@app.route('/statewise/<state>', methods = ['GET'])
def drilldown(state):
    return render_template('statewisefurther.html', data=data, statename=state )
if __name__ == '__main__':
    app.run(debug=True)