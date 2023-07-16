from flask import Flask, render_template, request, redirect
from weather import GetReport


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/search')
def city_report():
    city = request.args.get('city')

    if city == '':
        return redirect('/')
    
    wdata = GetReport(city)
    # wdata.getDummy()
    wdata.getResponse()

    return render_template('city_report.html', data=wdata.getData())


if __name__ == '__main__':
    app.run(debug=False)